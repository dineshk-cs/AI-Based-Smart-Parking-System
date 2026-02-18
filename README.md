# AI-Based-Smart-Parking-System

🚀 Project Overview

The AI-Based Smart Parking System is a full-stack extension of an AI-driven vehicle monitoring system. It integrates deep learning-based license plate recognition with a web-based interface for real-time parking management.

The system enables users to upload vehicle images or provide image URLs, automatically detects license plates, extracts vehicle numbers, and manages entry-exit logs with accurate timestamp tracking and duration computation.

This project demonstrates complete end-to-end implementation of AI + Backend + Frontend integration.

💡 Problem Statement

Manual parking management systems:

Require human intervention

Are prone to errors

Lack automation and scalability

Do not provide real-time monitoring

This project provides a fully automated, AI-driven smart parking solution with a web interface and API-based architecture.

🧠 System Architecture
🔹 AI Layer

YOLOv8 → License plate detection

EasyOCR → Plate text extraction

OpenCV → Image preprocessing

🔹 Backend Layer

Flask REST APIs

Image handling (upload & URL input)

Entry/Exit logic management

Logbook data structure

🔹 Frontend Layer

Responsive UI (HTML, CSS, JavaScript)

Image preview functionality

Real-time prediction results display

Dynamic vehicle logbook interface

🔄 System Workflow

User uploads an image or provides an image URL.

Backend receives image via Flask API.

YOLOv8 detects the number plate.

Detected region is cropped.

EasyOCR extracts plate text.

System determines ENTRY or EXIT.

Logbook updates with timestamps and duration.

Results displayed dynamically on frontend.

🛠️ Tech Stack

AI & Processing

Python

YOLOv8 (Ultralytics)

EasyOCR

OpenCV

Backend

Flask

Flask-CORS

Frontend

HTML

CSS

JavaScript

⭐ Key Features

AI-based license plate detection

OCR-based vehicle identification

REST API architecture

Image upload & URL-based inference

Automated vehicle entry-exit logging

Real-time parking duration calculation

Interactive digital logbook

📂 Project Structure
├── backend.py              # Flask backend API
├── predict.py              # Detection logic
├── best.pt                 # Trained YOLOv8 model
├── uploads/                # Uploaded images
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── styles.css
│   └── script.js
├── requirements.txt
└── README.md

▶️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/AI-Based-Smart-Parking-System.git
cd AI-Based-Smart-Parking-System

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Backend
python backend.py

4️⃣ Open Frontend

Open index.html in your browser or integrate with Flask template rendering.

📊 Real-World Applications

Smart city parking systems

Automated campus vehicle tracking

Residential gated communities

Commercial parking management

📈 Engineering Highlights

Built complete AI-to-Web integration pipeline

Designed RESTful APIs for real-time prediction

Implemented automated state-based entry-exit logic

Developed responsive frontend with dynamic UI updates

Demonstrated scalable system architecture

🔮 Future Enhancements

Database integration (PostgreSQL / MongoDB)

Live CCTV stream processing

Admin dashboard with analytics

Payment gateway integration

Cloud deployment (AWS / Azure)
