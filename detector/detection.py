try:
    from PIL import Image
    import streamlit as st 
    import appConfig as CONFIG
    import numpy as np 
    import tensorflow as tf
    import keras
    import os
    
except ImportError as e:
    print(f"Some Modules are missing {e}")


@st.cache(allow_output_mutation=True, show_spinner = False)
def load_model():
    model = keras.models.load_model(CONFIG.FINAL_MODEL)
    return model

class Detector:
    def __init__(self):
        if "model" not in st.session_state:
            with st.spinner('Loading model to the client session...'):
                self.model = load_model()
        else:
            self.model = st.session_state['model']
        self.result = {'class_names':['Benign', 'Malignant'],
                        'class_indices':[0, 1]
                        }
    def predict(self):
        img_arr = np.asarray(Image.open(CONFIG.IMG_IN))
        resized_input_img = tf.image.resize(img_arr, (244,244))
        final_img = np.expand_dims(resized_input_img, axis=0)
        prediction = self.model.predict(final_img)
        pred_cls_indices = np.argmax(prediction, axis=1)[0]
        self.result.update({'probabilities':list(prediction[0]), 'predicted_class_indices': pred_cls_indices,
                            'predicted_class_labels':self.result['class_names'][pred_cls_indices]})
        return self.result

    def clean_up(self):
        try:
            imgs = os.listdir(CONFIG.INFERENCE_DIR)
            [os.remove(os.path.join(CONFIG.INFERENCE_DIR, img)) for img in imgs]
        except:
            pass