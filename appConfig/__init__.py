import os 
from pathlib import Path
import uuid
user_id = uuid.uuid4()

STATIC_DIR = Path("static")

IMAGES_DIR = os.path.join(STATIC_DIR,"images")
os.makedirs(IMAGES_DIR, exist_ok=True)
INFERENCE_DIR = os.path.join(IMAGES_DIR,"inference")
os.makedirs(INFERENCE_DIR, exist_ok=True)

IMG_IN = os.path.join(INFERENCE_DIR, f"in_{user_id}.jpg")
IMG_OUT = os.path.join(INFERENCE_DIR, f"out_{user_id}.jpg")
COLOR_IMG_OUT = os.path.join(INFERENCE_DIR, f"color_img.jpg")

ARTIFACTS = Path("artifacts")
FINAL_MODEL = os.path.join(ARTIFACTS, "model.h5")

DEVICE = 'cpu'
PORT = 80


