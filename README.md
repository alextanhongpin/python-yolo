# yolov11



Directory structure for YOLOv11:

```
├── data
│   ├── test
│   │   ├── images
│   │   └── labels
│   ├── train
│   │   ├── images
│   │   └── labels
│   └── valid
│       ├── images
│       └── labels
├── data.yaml
```

`data.yaml`:

```yaml
path: data
train: train
val: val

names:
  0: abby
  1: jeff
  2: lori
```

YOLOv11 PyTorch TXT is the format used by the YOLO11 object detection model.

Each image has one txt file with a single line for each bounding box. The format of each row is

```
class_id center_x center_y width height
```

where fields are space delimited, and the coordinates are normalized from zero to one.

Note: To convert to normalized xywh from pixel values, divide x (and width) by the image's width and divide y (and height) by the image's height.

e.g.
```
1 0.617 0.3594420600858369 0.114 0.17381974248927037
1 0.094 0.38626609442060084 0.156 0.23605150214592274
1 0.295 0.3959227467811159 0.13 0.19527896995708155
1 0.785 0.398068669527897 0.07 0.14377682403433475
1 0.886 0.40879828326180256 0.124 0.18240343347639484
```
