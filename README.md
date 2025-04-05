# Facial Emotion Detection using YOLOv11

> 🧪 Object Detection-based Emotion Recognition | 🎯 YOLOv11 | 🏋️ Training + 📸 Real-time Inference

## 🔍 Overview

This project demonstrates a complete pipeline for **facial emotion detection** using **YOLOv11**, treating emotion recognition as an **object detection** task.

While traditional systems often rely on facial embeddings (like FaceNet or DeepFace), this project explores YOLOv11 as an experimental alternative — capable of both training and running real-time webcam inference.

---

## 📦 Key Features

- ⚙️ Environment setup via Jupyter notebook
- 📁 Dataset preparation for training
- 🧠 YOLOv11 model training
- 💾 Model export and storage
- 🎥 Real-time webcam detection using the trained model

---

## 🛠️ Repository Structure

```
CV-Facial-Emotion-Detection/
│
├── Facial_Emotion_Detection_using_Yolo11.ipynb   # Environment setup + training pipeline
├── inference_app/
│   └── webcam_emotion_detector.py                # Webcam-based real-time emotion detection
├── models/
│   └── best.pt                                   # Trained YOLOv11 model (downloaded/exported)
├── requirements.txt                              # Runtime-only dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sujithadr/CV-Facial-Emotion-Detection.git
cd CV-Facial-Emotion-Detection
```

---

## 🧪 Model Training (Optional)

If you'd like to train your own model:

### Step 1: Install training dependencies manually or via notebook cells

use colab to train for the GPU support

### Step 2: Run the notebook

```bash
jupyter notebook Facial_Emotion_Detection_using_Yolo11.ipynb
```

The notebook will guide you through:

- Environment setup (YOLO repo + dependencies)
- Dataset loading (e.g., FER2013)
- Training configuration
- Model training and export (`best.pt`)

---

## 🎥 Real-time Emotion Detection (Inference)

Once training is complete or if you're using a pre-trained model:

### Step 1: Install runtime dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the webcam detector

```bash
python inference_app/webcam_emotion_detector.py
```

This script:
- Loads the trained model from `models/best.pt`
- Opens the webcam
- Predicts and displays facial emotions in real time

---

## 📌 Notes

- This is an experimental project for educational use.
- Facial embeddings are generally preferred for production-level applications.
- The training notebook can be skipped if using a pre-trained model.

---

## 📚 References

- 🔗 [YOLOv11 GitHub](https://github.com/WongKinYiu/yolov11)
- 📊 [FER2013 Dataset](https://www.kaggle.com/datasets/msambare/fer2013)
- 📷 [OpenCV](https://opencv.org/)

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repo, make improvements, and open a pull request.

---

## 🧾 License

Licensed under the [MIT License](LICENSE).  By Sujith Somanunnithan

---

## 🔗 Repository

GitHub: [CV-Facial-Emotion-Detection](https://github.com/sujithadr/CV-Facial-Emotion-Detection.git)
