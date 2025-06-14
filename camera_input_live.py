import streamlit as st

def camera_input_live():
    img_file_buffer = st.camera_input("Take a picture")
    return img_file_buffer
