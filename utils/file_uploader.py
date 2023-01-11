import streamlit as st
import numpy as np
import appConfig as CONFIG
from PIL import Image
import base64

class FileOps:
 
    def __init__(self):
        self.fileTypes = ["jpeg", "png", "jpg"]
        self.col1, self.col2, self.col3 = st.columns(3)
 
    def upload(self):
        """
        Upload Images using Streamlit
        """
        file = self.get_img_from_user()

        try:
            self.col1.image(file, width=350)
            self.save_uploadedfile(file)
            
        except:
            pass
        #    raise e
        #    st.error("Not a valid file")
        #file.close()

    def save_uploadedfile(self,uploadedfile):
        with open(CONFIG.IMG_IN,"wb") as f:
            f.write(uploadedfile.getbuffer())

    def display_prediction(self, img):
        self.img_array = np.asarray(Image.open(img))
        self.col2.write("Where model is looking at ? 🤔💭")
        self.col2.image(self.img_array, width=450)
        self.download_predictions()

    def download_predictions(self, file_label='Skin Prediction.jpg'):
        with open(CONFIG.IMG_OUT, 'rb') as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:file/txt;base64,{bin_str}" download="{file_label}"><input type="button" value="Download Prediction Result ⬇️"></a>'
        self.col2.markdown(href, unsafe_allow_html=True)

    def get_img_from_user(self):
        
        file = self.col1.file_uploader("Upload a Picture ⬆️", type=self.fileTypes, accept_multiple_files=False)
        if file is not None:
            return file 
        file = self.col1.camera_input("OR Take a picture 📷")
        if file is not None:
            return file