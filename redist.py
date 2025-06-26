"""
redist.py – Serial Distribution Tool for Inference Input

This script reads a CSV file containing 140-point signal vectors (one per line),
sends each vector over a serial connection to an STM32-based device running
NanoEdge AI inference firmware, and logs the model's similarity and status outputs.

Intended for evaluating deployed NanoEdge libraries with pre-collected signal data.
Not meant for live sensor streams or real-time analysis.
"""


import csv
import struct
import time
import serial
import re

# --- Configuration ---
SERIAL_PORT = 'COM4'
BAUDRATE = 115200
FLOAT_COUNT = 140
DELAY_PER_FLOAT = 0.001
DELAY_PER_RECORD = 0.05
TIMEOUT = 2

INPUT_FILE = 'ecg_500.csv'
NORMAL_OUTFILE = 'normal.csv'
ANOMALY_OUTFILE = 'anomaly.csv'

# --- Core functions ---
def send_floats(ser, float_values):
    for val in float_values:
        packet = struct.pack('<f', val)
        ser.write(packet)
        time.sleep(DELAY_PER_FLOAT)
    ser.flush()

def extract_similarity(response):
    match = re.search(r'similarity\s*=\s*(\d+(?:\.\d+)?)', response)
    return float(match.group(1)) if match else None

# --- Main processing ---
def main():
    with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=TIMEOUT) as ser, \
         open(INPUT_FILE, 'r') as infile, \
         open(NORMAL_OUTFILE, 'w', newline='') as normal_out, \
         open(ANOMALY_OUTFILE, 'w', newline='') as anomaly_out:

        reader = csv.reader(infile)
        normal_writer = csv.writer(normal_out)
        anomaly_writer = csv.writer(anomaly_out)

        for line_num, row in enumerate(reader, start=1):
            try:
                if len(row) < FLOAT_COUNT:
                    print(f"[WARN] Line {line_num}: Too few values. Skipping.")
                    continue

                float_values = [float(val) for val in row[:FLOAT_COUNT]]
                send_floats(ser, float_values)

                response = ser.readline().decode(errors='ignore').strip()
                print(f"[RX] Line {line_num}: {response}")

                similarity = extract_similarity(response)
                if similarity is not None:
                    if similarity >= 80:
                        normal_writer.writerow(row)
                    else:
                        anomaly_writer.writerow(row)

                time.sleep(DELAY_PER_RECORD)

            except Exception as ex:
                print(f"[ERROR] Line {line_num}: {ex}")

if __name__ == "__main__":
    main()
