try:
    import streamlit as st 
    from utils import FileOps
    from detector import Detector
    import appConfig as CONFIG
    from aipilot.tf.cv import GradCam
except ImportError as e:
    print(f"Some Modules are missing {e}")

def main():
    st.title("Skin Cancer Detector") 
    file_ops = FileOps()
    detector = Detector()
    gradcam = GradCam(detector.model, "conv2d", in_img_path = CONFIG.IMG_IN , out_img_path = CONFIG.IMG_OUT)
    file_ops.upload()
    if st.button("Make Prediction 🔮"):
        try:
            gradcam.get_gradcam()
            file_ops.display_prediction(CONFIG.IMG_OUT)
            
            results = detector.predict()
            file_ops.col3.write("Prediction Result 🔓")
            file_ops.col3.success(results)
            ben_prob = round(results["probabilities"][0]*100, 5)
            mal_prob = round(results["probabilities"][1]*100, 5)
            file_ops.col3.info(f"Probability of being Benign is {ben_prob} %")
            file_ops.col3.info(f"Probability of being Malignant is {mal_prob} %")
            detector.clean_up()
        except FileNotFoundError:
            file_ops.col1.error("Please upload or take a picture using camera")

if __name__ == '__main__':
    st.set_page_config(
    page_title="Skin Cancer Detection",
    page_icon="static/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded",)
    hide_streamlit_style = """
                <style>
                div.block-container{padding-top:1rem;}
                #MainMenu {visibility: hidden;}
                    
                visibility: hidden;
                
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()