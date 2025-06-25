# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1308, 984)
        self.sendStop = QPushButton(Widget)
        self.sendStop.setObjectName(u"sendStop")
        self.sendStop.setGeometry(QRect(120, 40, 91, 24))
        self.sendStart = QPushButton(Widget)
        self.sendStart.setObjectName(u"sendStart")
        self.sendStart.setGeometry(QRect(10, 40, 101, 24))
        self.comboPortNumber = QComboBox(Widget)
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.addItem("")
        self.comboPortNumber.setObjectName(u"comboPortNumber")
        self.comboPortNumber.setGeometry(QRect(220, 40, 131, 22))
        self.plainTextEditReport = QPlainTextEdit(Widget)
        self.plainTextEditReport.setObjectName(u"plainTextEditReport")
        self.plainTextEditReport.setGeometry(QRect(20, 110, 1261, 851))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.plainTextEditReport.setFont(font)
        self.comboBaud = QComboBox(Widget)
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.addItem("")
        self.comboBaud.setObjectName(u"comboBaud")
        self.comboBaud.setGeometry(QRect(360, 40, 191, 22))
        self.pushClear = QPushButton(Widget)
        self.pushClear.setObjectName(u"pushClear")
        self.pushClear.setGeometry(QRect(570, 40, 75, 24))
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 1141, 22))
        self.pushSend = QPushButton(Widget)
        self.pushSend.setObjectName(u"pushSend")
        self.pushSend.setGeometry(QRect(1160, 10, 75, 24))
        self.sendFileButton = QPushButton(Widget)
        self.sendFileButton.setObjectName(u"sendFileButton")
        self.sendFileButton.setGeometry(QRect(920, 40, 81, 24))
        self.pushEcho = QPushButton(Widget)
        self.pushEcho.setObjectName(u"pushEcho")
        self.pushEcho.setGeometry(QRect(20, 90, 241, 24))
        self.pushSave = QPushButton(Widget)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setGeometry(QRect(1144, 80, 111, 24))

        self.retranslateUi(Widget)

        self.comboPortNumber.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.sendStop.setText(QCoreApplication.translate("Widget", u"Stop", None))
        self.sendStart.setText(QCoreApplication.translate("Widget", u"Start", None))
        self.comboPortNumber.setItemText(0, QCoreApplication.translate("Widget", u"COM1", None))
        self.comboPortNumber.setItemText(1, QCoreApplication.translate("Widget", u"COM2", None))
        self.comboPortNumber.setItemText(2, QCoreApplication.translate("Widget", u"COM3", None))
        self.comboPortNumber.setItemText(3, QCoreApplication.translate("Widget", u"COM4", None))
        self.comboPortNumber.setItemText(4, QCoreApplication.translate("Widget", u"COM5", None))
        self.comboPortNumber.setItemText(5, QCoreApplication.translate("Widget", u"COM6", None))
        self.comboPortNumber.setItemText(6, QCoreApplication.translate("Widget", u"COM7", None))

        self.comboBaud.setItemText(0, QCoreApplication.translate("Widget", u"115200", None))
        self.comboBaud.setItemText(1, QCoreApplication.translate("Widget", u"57600", None))
        self.comboBaud.setItemText(2, QCoreApplication.translate("Widget", u"38400", None))
        self.comboBaud.setItemText(3, QCoreApplication.translate("Widget", u"19200", None))
        self.comboBaud.setItemText(4, QCoreApplication.translate("Widget", u"9600", None))

        self.pushClear.setText(QCoreApplication.translate("Widget", u"Clear", None))
        self.lineEdit.setText(QCoreApplication.translate("Widget", u"0.89486742, -0.003822158, -0.75105205, -1.3965429, -1.7378376, -2.1130203, -2.2132096, -2.2033471, -2.0241906, -1.5914581, -1.0499022, -0.57789108, -0.3131374, -0.20084404, -0.18379899, 0.016525057, 0.50921179, 0.77751147, 0.75067496, 0.78843003, 0.77137524, 0.73257374, 0.67985885, 0.62183591, 0.60469296, 0.58129958, 0.65998204, 0.63413413, 0.63558912, 0.76050608, 0.76912011, 0.73457027, 0.72108854, 0.75040232, 0.62612794, 0.51689273, 0.54554218, 0.50588773, 0.5258932, 0.49186076, 0.52836623, 0.62282844, 0.58039006, 0.54824181, 0.50770483, 0.51204975, 0.40906504, 0.31038144, 0.36845009, 0.38137005, 0.33419976, 0.18130539, 0.20183031, 0.2933171, 0.27945872, 0.29958438, 0.21474396, 0.18456487, 0.13197654, 0.057778811, 0.018044803, -0.071802363, 0.005535548, 0.066041, 0.042362944, 0.05525463, -0.005126899, -0.051986345, -0.015207146, -0.0094131254, 0.02094263, 0.092754939, 0.00073659051, -0.071986495, 0.070326647, 0.091355005, 0.028342719, 0.17460518, 0.28679751, 0.27782832, 0.31537371, 0.31602348, 0.36637824, 0."
                        "44613065, 0.41105086, 0.42461382, 0.4831252, 0.4544008, 0.46774525, 0.56968959, 0.54844061, 0.52878176, 0.63875397, 0.64354817, 0.62231549, 0.6227605, 0.57584803, 0.56640109, 0.56635399, 0.57809064, 0.61300844, 0.63278994, 0.59456305, 0.61561681, 0.72445263, 0.7123046, 0.67086495, 0.71278444, 0.66167141, 0.58293314, 0.58568763, 0.61013419, 0.69306756, 0.68844189, 0.61338458, 0.60209334, 0.42122252, 0.16604014, 0.14347481, 0.19632701, 0.16141046, 0.1275313, -0.018672703, -0.23865283, -0.3706969, -0.59290109, -0.63411579, -0.44082747, -0.5180703, -0.70243851, -0.89974628, -1.4415163, -1.8616119, -2.3213812, -2.8848769, -3.530246, -4.4125149, -3.9033308, -3.5671064, -1.5363381", None))
        self.pushSend.setText(QCoreApplication.translate("Widget", u"Send One ", None))
        self.sendFileButton.setText(QCoreApplication.translate("Widget", u"Send File", None))
        self.pushEcho.setText(QCoreApplication.translate("Widget", u"Echo ", None))
        self.pushSave.setText(QCoreApplication.translate("Widget", u"Save Results", None))
    # retranslateUi

