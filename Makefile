inference:
	uv run inference.py

train:
	uv run yolo settings datasets_dir='/Users/alextanhongpin/Documents/go/python-yolo'
	uv run yolo detect train data=data.yaml model=yolo11m.pt epochs=100 imgsz=640
