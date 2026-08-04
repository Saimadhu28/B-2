# 🛰️ AI-Based Building Damage Assessment Using Multi-Temporal Satellite Imagery

## 📌 Overview

This project is an AI-powered Building Damage Assessment System that analyzes
pre-disaster and post-disaster satellite images to determine the level of
building damage.

The system uses Deep Learning (Siamese Neural Networks with a CNN backbone)
to compare images captured before and after a disaster and classify the damage.

Supported damage categories include:

- No Damage
- Minor Damage
- Major Damage
- Destroyed

The system also provides Explainable AI (Grad-CAM), damage severity estimation,
multi-temporal damage progression analysis, and automatically generates a PDF
assessment report.

---

# 🎯 Objectives

- Detect building damage from satellite imagery.
- Compare pre-disaster and post-disaster images.
- Predict the damage category.
- Estimate damage severity.
- Visualize important damaged regions using Grad-CAM.
- Analyze damage progression using multiple post-disaster images.
- Generate an AI-based damage assessment report.

---

# ✨ Features

## 1. Building Damage Classification

Predicts one of the following classes:

- No Damage
- Minor Damage
- Major Damage
- Destroyed

---

## 2. Confidence Score

Displays the confidence score of the prediction.

Example:

Prediction : Major Damage

Confidence : 96.42%

---

## 3. Damage Severity Estimation

Converts model prediction into a severity percentage.

Example:

Severity : 74%

---

## 4. Explainable AI (Grad-CAM)

Highlights the image regions responsible for the prediction.

Outputs:

- Original Image
- Heatmap
- Overlay Image

---

## 5. Multi-Temporal Damage Progression Analysis

Users can upload:

- Pre-disaster image
- Day 1 post-disaster image
- Day 3 post-disaster image
- Day 7 post-disaster image
- Day 15 post-disaster image

The model predicts damage for each observation independently.

The application then compares these predictions and generates a damage timeline.

Example:

Day 1 → Minor Damage

Day 3 → Major Damage

Day 7 → Major Damage

Day 15 → Destroyed

Overall Trend:

Damage Severity Increasing

---

## 6. PDF Report Generation

Automatically generates a professional report containing:

- Prediction
- Confidence
- Damage Severity
- Grad-CAM Visualization
- Damage Timeline
- Final Assessment

---

# 🗂 Dataset

Dataset Used:

Official xView2 / xBD Challenge Dataset

Downloaded from:

https://xview2.org

Dataset Components:

- Challenge Training Set
- Additional Tier3 Training Set
- Challenge Test Set

Dataset contains:

- Pre-disaster satellite images
- Post-disaster satellite images
- Building annotations
- Damage labels

---

# 🧠 Deep Learning Pipeline

Pre Image

+

Post Image

↓

Preprocessing

↓

Siamese Neural Network

↓

Feature Comparison

↓

Damage Classification

↓

Confidence Score

↓

Severity Estimation

↓

Grad-CAM

↓

Temporal Progression Analysis

↓

PDF Report

---

# 📂 Project Structure

Building-Damage-Assessment/

├── dataset/

├── configs/

├── data/

├── models/

├── training/

├── inference/

├── reports/

├── outputs/

├── notebooks/

├── requirements.txt

└── README.md

---

# ⚙️ Technologies Used

Programming Language

- Python

Deep Learning

- PyTorch

Computer Vision

- OpenCV
- Pillow

Data Processing

- NumPy
- Pandas

Visualization

- Matplotlib

Explainable AI

- Grad-CAM

Evaluation

- Scikit-Learn

Report Generation

- ReportLab

Training Platform

- Kaggle GPU

---

# 📊 Model Output

Prediction

Major Damage

Confidence

96.52%

Severity

81%

Grad-CAM

Heatmap highlighting damaged structures

Temporal Analysis

Day 1 → Minor Damage

Day 3 → Major Damage

Day 7 → Destroyed

Overall Trend

Damage Severity Increasing

---

# 🚀 Future Improvements

Possible future enhancements include:

- Building Detection using YOLO or Mask R-CNN
- Interactive Damage Maps
- Disaster Severity Dashboard
- Cloud Deployment
- Real-Time Satellite Monitoring
- Multi-Class Segmentation
- Mobile Application

---

# 👨‍💻 Authors

Final Year B.Tech Project

Artificial Intelligence Based Building Damage Assessment System
