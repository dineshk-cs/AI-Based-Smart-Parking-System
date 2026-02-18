from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

def predict_image(image_path):
    results = model(image_path)

    detections = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            xyxy = box.xyxy[0].tolist()

            detections.append({
                "class_id": cls_id,
                "confidence": conf,
                "bbox": xyxy
            })

    return detections


# test
if __name__ == "__main__":
    output = predict_image("car.jpeg")
    print(output)
