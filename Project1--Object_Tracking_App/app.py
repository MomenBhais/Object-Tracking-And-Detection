import streamlit as st
import cv2
import numpy as np
import tempfile
import time


def ConvertColor(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

#set page config
st.set_page_config(page_title="Object Tracking App",
                   layout="wide",
                   page_icon="🎥",
                   initial_sidebar_state="expanded")

#header
st.title("🎥 Object Tracking Application")
st.markdown("""This application tracks moving objects in a video using OpenCV and Streamlit,
            and it uses the MOG2 background subtractor to detect moving objects,
            and drow a green rectangle around them""")

uploaded_file = st.file_uploader("Please upload a video", type=["mp4", "avi", "mov", "wmv"])



if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    tfile.close()
    
    
    captures = cv2.VideoCapture(tfile.name)
    if not captures.isOpened():
        st.error("Video file cannot be opened")
    else:
        stframe = st.empty() # Placeholder for the video frame
        back_sub = cv2.createBackgroundSubtractorMOG2() # Background subtractor
        
        while captures.isOpened():
            ret, frame = captures.read()
            if not ret:
                break
            
            fg_mask = back_sub.apply(frame) # Apply background subtractor
            
            contours, _ = cv2.findContours(fg_mask, 
                                           cv2.RETR_EXTERNAL, 
                                           cv2.CHAIN_APPROX_SIMPLE) # Find contours (moving objects)
            
            for i in contours:
                if cv2.contourArea(i) > 500: # Filter contours --> area > 500 pixels , you can change this value
                    x, y, width, height = cv2.boundingRect(i)
                    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2) # green rectangle
            
            stframe.image(ConvertColor(frame), channels="RGB") # Display the video frame
            time.sleep(0.003) # add delay to simulate the video frame rate
            
        captures.release()
        
        
        
        
        