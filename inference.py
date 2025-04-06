from ultralytics import YOLO


# model = YOLO('yolo11m.pt')

# Use trained weights
model = YOLO('runs/detect/train/weights/best.pt')
results = model('images/Samples/Sample-2.jpg')



for result in results:
    boxes = result.boxes
    masks = result.masks
    keypoints = result.keypoints
    probs = result.probs
    obb = result.obb
    result.show()
    result.save(filename='result.jpg')
