# Object Tracking & Detection Applications

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

## Overview
This repository contains two AI-powered applications developed using **Python**, **OpenCV**, and **Streamlit**:

1. **Object Tracking Application** - Tracks moving objects in a video using OpenCV’s background subtraction (MOG2) method and highlights them with bounding boxes.
2. **Object Detection Application** - Detects objects in images/videos using AI models.

These applications provide an interactive way to analyze motion and object presence in different scenarios, making them ideal for research, surveillance, and automation tasks.

## Features
- **Real-time object tracking** using OpenCV’s background subtraction.
- **Interactive web-based UI** built with Streamlit.
- **Video processing support** for object tracking.
- **Customizable detection parameters**.
- **Easy-to-use interface** that requires no prior coding knowledge.
- **Lightweight and fast execution**, making it efficient even on lower-end devices.
- **Flexible deployment**, as it can run locally or be hosted online with services like Streamlit Sharing.

---
## Files Overview
### 1️⃣ `app.py` - Object Tracking Application
This file contains a **Streamlit-based application** for tracking moving objects in a video. It utilizes **OpenCV’s MOG2 background subtractor** to detect motion and draws green bounding boxes around detected objects.

🔹 **Key functionalities:**
- Upload a video file.
- Process each frame and detect moving objects.
- Display real-time tracking results in the Streamlit UI.
- Uses OpenCV’s `cv2.findContours()` for detecting motion regions.
- Adjustable contour size threshold to eliminate false detections.

🔹 **How to Run:**
```sh
streamlit run app.py
```
Upload a video file, and the app will track moving objects in real-time.

🔹 **Possible Use Cases:**
- **Security and Surveillance:** Detect unauthorized movements.
- **Sports Analysis:** Track player movements in sports footage.
- **Traffic Monitoring:** Identify moving vehicles in traffic videos.

---
### 2️⃣ `Object_tracking.ipynb` - Object Tracking Implementation
This Jupyter Notebook provides a **detailed breakdown** of the tracking algorithm using OpenCV. It explains:
- How to use `cv2.createBackgroundSubtractorMOG2()` for motion detection.
- Contour-based detection to highlight moving objects.
- Frame-by-frame processing for real-time tracking.
- Ways to improve tracking performance by fine-tuning parameters.

🔹 **How to Run:**
```sh
jupyter notebook Object_tracking.ipynb
```
Follow the notebook to understand each step of the tracking implementation.

🔹 **Additional Insights:**
- Shows how to adjust learning rates for better motion detection.
- Explains the impact of noise and ways to remove it.
- Demonstrates different contour detection strategies.

---
### 3️⃣ `Object_Detection.ipynb` - Object Detection Model
This notebook focuses on **object detection in images/videos**. It likely includes:
- Using **pre-trained deep learning models** (e.g., YOLO, SSD, Faster R-CNN).
- Detecting objects in various scenes.
- Customizing detection parameters.
- Evaluating model accuracy and performance.
- Applying filters to detect specific objects.

🔹 **How to Run:**
```sh
jupyter notebook Object_Detection.ipynb
```
Explore the notebook to see how AI models detect objects in different environments.

🔹 **Practical Applications:**
- **Retail & Inventory:** Identify products on store shelves.
- **Healthcare:** Detect medical instruments in surgical videos.
- **Autonomous Vehicles:** Recognize pedestrians and traffic signs.

---
## Installation
Ensure Python (>=3.7) is installed. Install required dependencies:
```sh
pip install -r requirements.txt
```
If `requirements.txt` is unavailable, install manually:
```sh
pip install streamlit opencv-python numpy
```

## Project Structure
```
📂 project-repo
│── app.py                   # Streamlit app for object tracking
│── Object_tracking.ipynb     # Jupyter Notebook for tracking implementation
│── Object_Detection.ipynb    # Jupyter Notebook for object detection
│── requirements.txt          # List of dependencies
```

## Screenshots
![Image](https://github.com/user-attachments/assets/98bc69e2-3258-427a-9f36-ee6975723dfd)

## Author
👤 **Momen Mohammed Bhais**  
📧 Contact: [momenbhais@outlook.com](mailto:momenbhais@outlook.com)

## Contributions
Feel free to contribute! Fork the repo, make changes, and submit a pull request.

