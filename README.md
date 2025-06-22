
# ✅ NanoEdgeAI EKG Anomaly Detection (STM32 Standalone)

> **Note:** This demo highlights the complete NanoEdge AI Studio workflow—from model generation to embedded inference—using synthetic input data in place of physical sensors. The anomaly detection logic is streamlined to showcase firmware integration and runtime evaluation, and may yield varied results due to the nature of the test inputs. For more realistic detection performance, STMicroelectronics recommends developing with their **B-U585I-IOT02A Discovery Kit**, which provides ready-to-use onboard sensors fully compatible with NanoEdge AI Studio.

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

**To restore full STM32CubeIDE functionality, simply rename these files after cloning or downloading the repository.**

---

## 🧰 Board Compatibility

This demo is designed specifically for the **STM32H723ZG Nucleo board**. If you're working with a different STM32 variant, you may still be able to use this workflow by:

- Creating a new STM32CubeIDE project targeting your board
- Porting over the following:
  - `Core/Src/main.c`
  - All contents of `Core/Inc/`
  - `Core/lib/` (including `libneai.a`)
- Adding include paths and library references in project properties

🎥 A step-by-step YouTube guide will be published soon to walk through this process visually.

License: GPL v.2
