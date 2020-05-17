# HAND GESTURE RECOGNITION

This project implements a hand recognition and hand gesture recognition system using OpenCV on Python 2.7. A histogram based approach is used to separate out a hand from the background image. Background cancellation techniques are used to obtain optimum results. The detected hand is then processed and modelled by finding contours and convex hull to recognize finger and palm positions and dimensions. Finally, a gesture object is created from the recognized pattern which is compared to a defined gesture dictionary.

![Home](https://github.com/p-disha/Sign-Language-Trainer/blob/master/screenshots/home.png)

### Project Report:
https://drive.google.com/open?id=1jYAYSWjX-JIwSAeN7yBEIxS7x9Yzp1E8khib4W0FKqo

### Instructions to run:
```
git clone https://github.com/p-disha/Sign-Language-Trainer.git
pip install -r requirements.txt
cd flask_webapp
python app.py
```
