# This Python file uses the following encoding: utf-8
import sys
import serial
import time
import struct
import csv

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QFont
from PySide6.QtCore import QObject, QThread, Signal

class FileSendWorker(QObject):
    line_processed = Signal(str)
    finished = Signal()

    def __init__(self, ser, file_path):
        super().__init__()
        self.ser = ser
        self.file_path = file_path

    def run(self):
        try:
            with open(self.file_path, 'r') as infile:
                reader = csv.reader(infile)
                for line_num, row in enumerate(reader, start=1):
                    if len(row) < 140:
                        self.line_processed.emit(f"[WARN] Line {line_num}: Too few values. Skipping.")
                        continue

                    float_values = [float(val) for val in row[:140]]
                    for val in float_values:
                        packet = struct.pack('<f', val)
                        self.ser.write(packet)
                        time.sleep(0.001)

                    self.ser.flush()
                    response = self.ser.readline().decode(errors='ignore').strip()
                    self.line_processed.emit(f"[RX] Line {line_num}: {response}")
                    time.sleep(0.05)
        except Exception as ex:
            self.line_processed.emit(f"[ERROR] Failed: {ex}")
        self.finished.emit()


# You need to run this command beforehand to generate ui_form.py from your .ui file:
# pyside6-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
class COMPort(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.port, self.baudrate = self.get_serial_params()

        self.ser = None
        self._reading = False
        font = QFont("Consolas", 18, QFont.Bold)
        self.ui.plainTextEditReport.setFont(font)
        self.ui.plainTextEditReport.setStyleSheet("background-color: black; color: white;")

        self.ui.sendStart.clicked.connect(self.start)
        self.ui.sendStop.clicked.connect(self.stop)
        self.ui.pushClear.clicked.connect(self.clear)
        self.ui.pushSend.clicked.connect(self.send_line)
        self.ui.sendFileButton.clicked.connect(self.on_sendFileButton_clicked)
        self.ui.pushEcho.clicked.connect(self.echo)
        self.ui.pushSave.clicked.connect(self.save)

    def get_serial_params(self):
        port = self.ui.comboPortNumber.currentText().strip()
        baud = int(self.ui.comboBaud.currentText().strip())
        return port, baud

    def start(self):
        if self._reading:
            self.ui.plainTextEditReport.appendPlainText("[INFO] Already reading.")
            return

        try:
            self.port, self.baudrate = self.get_serial_params()
            self.ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
            time.sleep(2)
            self.ser.reset_input_buffer()
            self._reading = True
            buffer = ""

            self.ui.plainTextEditReport.appendPlainText("[OK] Started reading...")

            while self._reading:
                if self.ser.in_waiting:
                    data = self.ser.read(self.ser.in_waiting)
                    buffer += data.decode(errors='ignore')

                    # Normalize line endings
                    lines = buffer.replace('\r\n', '\n').replace('\r', '\n').split('\n')

                    # Keep last partial line in buffer
                    for line in lines[:-1]:
                        self.ui.plainTextEditReport.appendPlainText(line.strip())
                    buffer = lines[-1]  # incomplete line held for next loop

                QApplication.processEvents()  # Keeps UI responsive
                time.sleep(0.05)

        except serial.SerialException as e:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] {e}")
        except Exception as ex:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Unexpected: {ex}")
        finally:
            if self.ser and self.ser.is_open:
                self.ser.close()
                self.ui.plainTextEditReport.appendPlainText("[INFO] Serial port closed.")

    def stop(self):
        self._reading = False
        self.ui.plainTextEditReport.appendPlainText("[OK] Reading stopped.")

    def clear(self):
        self.ui.plainTextEditReport.clear()

    def send_floats(self, float_values: list[float], delay: float = 0.001) -> str:
        if len(float_values) != 140:
            raise ValueError(f"Expected 140 floats, got {len(float_values)}")

        self.port, self.baudrate = self.get_serial_params()

        for val in float_values:
            packet = struct.pack('<f', val)  # Little-endian 4-byte float
            self.ser.write(packet)
            time.sleep(delay)

        self.ser.flush()

        response = self.send_floats(float_values)
        self.ui.plainTextEditReport.appendPlainText(f"[RX] {response}")


    def send_text_line(self, text: str):
        float_values = [float(val) for val in text.strip().split(',') if val.strip()]
        if len(float_values) != 140:
            raise ValueError(f"Expected 140 floats, got {len(float_values)}")

        self.send_floats(float_values)

    def send_line(self):
        try:

            text = self.ui.lineEdit.text()
            self.send_text_line(text)
            self.ui.plainTextEditReport.appendPlainText(f"[TX] Sent {140} floats from GUI input")
        except Exception as ex:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Invalid float input: {ex}")

    def on_sendFileButton_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "CSV Files (*.csv);;Text Files (*.txt);;All Files (*)"
        )

        if not file_path:
            return

        if not self.ser or not self.ser.is_open:
            self.ui.plainTextEditReport.appendPlainText("[ERROR] Serial port not open.")
            return

        self.worker = FileSendWorker(self.ser, file_path)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        self.worker.line_processed.connect(self.ui.plainTextEditReport.appendPlainText)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def echo(self):
        self.port, self.baudrate = self.get_serial_params()

        if self.ser is None or not self.ser.is_open:
            try:
                self.ser = serial.Serial(self.port, self.baudrate, timeout=0.1)
                time.sleep(2)  # Allow time for MCU reset via DTR, if applicable
            except Exception as ex:
                self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Failed to open serial port: {ex}")
                return

        try:
            report_text = self.ui.plainTextEditReport.toPlainText()
            lines = report_text.splitlines()  # This preserves content safely
            for line in lines:
                line_bytes = (line + '\r\n').encode('utf-8')
                self.ser.write(line_bytes)
                time.sleep(0.01)  # Optional pacing

            self.ui.plainTextEditReport.appendPlainText(f"[TX] Echoed {len(lines)} lines.")

        except Exception as ex:
            self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Failed to echo: {ex}")


    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Report",
            "",
            "Text Files (*.txt);;All Files (*)"
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.ui.plainTextEditReport.toPlainText())
                self.ui.plainTextEditReport.appendPlainText(f"[OK] Report saved to: {file_path}")
            except Exception as e:
                self.ui.plainTextEditReport.appendPlainText(f"[ERROR] Failed to save: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = COMPort()
    widget.show()
    sys.exit(app.exec())
