import requests
import base64

IN_IMG_PATH = "in.jpg" # You can give any name with the right extension
OUT_IMG_PATH = "out.jpg" 
ENDPOINT = "http://127.0.0.1/predict"

def decodeImage(base64_str, OUT_IMG_PATH):
    imgdata = base64.b64decode(base64_str)
    with open(OUT_IMG_PATH, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(IN_IMG_PATH):
    with open(IN_IMG_PATH, "rb") as f:
        return base64.b64encode(f.read())

if __name__ == '__main__':

    BASE64_STR = encodeImageIntoBase64(IN_IMG_PATH).decode("utf-8")
    response = requests.post(ENDPOINT, json={"base64_str":BASE64_STR})
    if response.status_code == 200:
        response = response.json()
        print(response)
        decodeImage(response["base64_str"], OUT_IMG_PATH)
    else :
        print(response)