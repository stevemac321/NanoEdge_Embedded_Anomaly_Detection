
# ✅ NanoEdgeAI Embedded Anomaly Detection (STM32 Standalone)

> **Note**: This demo illustrates the full NanoEdge AI Studio pipeline—from model generation to embedded inference—using synthetic input data in place of live sensor readings. It is validated specifically on the STM32H743Z Nucleo-144 board using the NanoEdge library generated for this hardware. The anomaly detection logic is designed to showcase firmware-level integration and runtime evaluation, and results may vary due to the nature of test inputs.
For real-world performance or sensor-based deployments, STMicroelectronics recommends their B-U585I-IOT02A Discovery Kit, which features onboard sensors and full NanoEdge compatibility.


---

## 🔧 Overview

This project demonstrates an anomaly detection workflow using:

- **STM32H723ZG Nucleo board**
- **NanoEdge AI Studio-generated static anomaly detection library**
- **Hardcoded validation arrays for embedded evaluation**

Signals are processed entirely on-chip without reliance on external data sources or runtime I/O.

---

## 📂 Project Structure

| File/Folder           | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| `Core/Src/main.c`     | Main firmware loop, NanoEdge initialization and inference    |
| `training_data.c`     | Optional training buffer (synthetic “normal” examples)       |
| `inference_data.c`    | Curated normal and anomaly datasets for validation           |
| `NanoEdgeAI.h`, `knowledge.h`, `libneai.a` | NanoEdge AI model and library files              |
| `.ioc`                | STM32CubeMX project configuration                            |

---

## ⚙️ Firmware Logic

1. NanoEdge AI is initialized on boot
2. Runtime learning is optional (`#define USE_TRAINING_MODE`)
3. Static datasets (`normal_data[]`, `anomaly_data[]`) are passed to `neai_anomalydetection_detect()`
4. Classification is based on **similarity score**:
   - `similarity == 100` → Normal  
   - `similarity < 100` → Anomaly

---

## 🧪 Dataset Design

- Input data is synthetic and embedded for demonstration purposes
- Records were trimmed to high-confidence examples through manual review
- Outlier "normal" records were reclassified as anomalies, and ambiguous examples were excluded

---

## 🛠️ Requirements

- STM32CubeIDE 1.18+
- STM32H7 HAL drivers
- NanoEdge AI Studio (for generating custom models if needed)

---

## 🚀 Running the Demo

1. Open the project in STM32CubeIDE
2. Compile and flash to a compatible STM32 board
3. Evaluate similarity scores with breakpoints, logic probes, or LED indicators

---

## 📁 Note on Project Files

Due to upload limitations on some platforms, the following files have been renamed:

- `_cproject` → rename to `.cproject`  
- `_mxproject` → rename to `.mxproject`  
- `_project` → rename to `.project`

**To restore full STM32CubeIDE functionality, simply rename these files after cloning or downloading the repository.   NanoEdge AI Studio does support other boards, however this project has only been validated on the STM32H743Z. **

---
COM Port Client–Controller Demo
This package includes a compact demonstration of serial communication between a Python-based Qt client and an embedded STM32 controller running anomaly detection. The setup showcases:
- Binary float transmission over UART (140 floats, 560 bytes total)
- Real-time inference using NanoEdge AI Studio–generated models
- A clean, testable Qt UI for sending data interactively or from file
- Integration-friendly architecture with minimal dependencies
This demo is ideal for developers exploring lightweight ML inference at the edge, or for those prototyping data-driven pipelines across a serial interface.
To get started:
- Open the .ui form in Qt Creator.
- Launch widget.py with the required modules (PySide6, pyserial, etc.).
- Flash the STM32 with the provided firmware.
- Connect and test.
  Compressed project archive: NanoEdge_Client.zip (no build artifacts included)



License: GPL v.2
