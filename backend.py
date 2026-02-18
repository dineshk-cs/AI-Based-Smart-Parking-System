from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import easyocr
import cv2
import os
import requests
import re
from datetime import datetime

app = Flask(__name__)

CORS(app, origins=["http://localhost:3000"])

# Load models
model = YOLO("best.pt")
reader = easyocr.Reader(['en'])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# GLOBAL LOGBOOK VARIABLE
logbook = {}


# function to clean plate text
def clean_plate(text):
    return re.sub(r'[^A-Z0-9]', '', text.upper())


# function to update logbook
def update_logbook(plate):

    now = datetime.now()

    if plate not in logbook:
        logbook[plate] = []

    records = logbook[plate]

    # check last record
    if len(records) == 0 or records[-1]["exit_time"] is not None:

        # NEW ENTRY
        records.append({
            "entry_time": now,
            "exit_time": None,
            "duration": None
        })

        return {
            "plate": plate,
            "status": "ENTRY",
            "entry_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "exit_time": None,
            "duration_hours": None
        }

    else:

        # EXIT
        entry_time = records[-1]["entry_time"]
        exit_time = now

        duration = exit_time - entry_time
        duration_hours = round(duration.total_seconds() / 3600, 2)

        records[-1]["exit_time"] = exit_time
        records[-1]["duration"] = duration_hours

        return {
            "plate": plate,
            "status": "EXIT",
            "entry_time": entry_time.strftime("%Y-%m-%d %H:%M:%S"),
            "exit_time": exit_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_hours": duration_hours
        }


@app.route("/predict", methods=["POST"])
def predict():

    # receive image
    if "image" in request.files:

        file = request.files["image"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

    elif "image_url" in request.form:

        url = request.form["image_url"]
        filepath = os.path.join(UPLOAD_FOLDER, "url.jpg")

        img_data = requests.get(url).content
        with open(filepath, "wb") as f:
            f.write(img_data)

    else:
        return jsonify({"error": "no image"})


    image = cv2.imread(filepath)

    results = model(filepath)

    responses = []

    for r in results:
        for box in r.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            plate_img = image[y1:y2, x1:x2]

            text = reader.readtext(plate_img)

            if text:

                plate = clean_plate(text[0][1])

                log_data = update_logbook(plate)

                responses.append(log_data)

    return jsonify(responses)


# endpoint to view logbook
@app.route("/logbook", methods=["GET"])
def view_logbook():

    output = {}

    for plate, records in logbook.items():

        output[plate] = []

        for r in records:

            output[plate].append({
                "entry_time": r["entry_time"].strftime("%Y-%m-%d %H:%M:%S"),
                "exit_time": r["exit_time"].strftime("%Y-%m-%d %H:%M:%S") if r["exit_time"] else None,
                "duration_hours": r["duration"]
            })

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)