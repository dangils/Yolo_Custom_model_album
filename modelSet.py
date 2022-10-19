import torch
from glob import glob

'''
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
'''
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_path = 'static/photos/67.jpg'

results = model(img_path)


img_list = glob('static/photos/*.jpg')
# jpg 확장자를 가지는 모든 파일 저장

db = {}

for img_path in img_list:
  results = model(img_path)

  tags = set()

  for pred in results.pred[0]:
    tag = results.names[int(pred[-1])]
    tag = tag.replace('','')
    tags.add(tag)

  db[img_path] = list(tags)


