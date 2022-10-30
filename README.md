# Yolo_Custom_model_album

### 실행 방법

```
pip version 21.3.1
pip install --upgrade pip

pip install flask
pip install torch
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
```
- pip 버전이 21.3.1 보다 낮을 경우 업그레이드
- pip install, 필요 라이브러리 설치

```
modelSet.py

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
```
- yolov5s 의 내장된 학습 모델 yolov5s 사용하여 object detection
- custom dataSet으로 학습한 pt파일로 object detection 가능

```
modelSet.py

img_list = glob('static/photos/*.jpg')
```
- 먼저 static-photos 폴더에 탐지할 이미지들을 저장 해야함 
- 해당 폴더에서 jpg 확장자 파일을 모두 가져와 objecte detection 수행

------- 

> Object detection
```
flask_app.py 실행

* Running on http://127.0.0.1:5000/ # 접속 URL
```


- 모든 레이블 클래스에 맞추어 체크 박스가 생성됨
- 선택한 체크박스의 클래스가 탐지된 사진들 확인 

<img width="941" alt="제목 없음" src="https://user-images.githubusercontent.com/74512114/198873385-267de429-be93-4888-b07c-af231633fe7e.png">

- ex) static-photos 폴더의 이미지에서 `table`이 탐지된 이미지만 출력



