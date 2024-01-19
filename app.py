import streamlit as st
import os
from clarifai.client.model import Model
import cv2
from urllib.request import urlopen
import numpy as np
from clarifai.modules.css import ClarifaiStreamlitCSS
from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont
import base64
from dotenv import load_dotenv

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

load_dotenv()
import os

# Passing the key values
clarifai_pat = os.getenv("CLARIFAI_PAT")


# 1. Function to choose food item for complaint 
def chooseFoodItem():
    global selected_option
    st.subheader("Please select the item for which you want to raise the complaint:")
    options = ['Pita Gyro', 'Coke 250 ml', 'Choco chip cookie']
    selected_option = st.radio("Select an option:", options)
    st.write(f"You selected: {selected_option}")


# 2. Input description and food images from user
def takeComplaintImgs():
    
    st.subheader(f"Enter your complaint and upload the images of damaged {selected_option}:")
    description = st.text_area("Enter your complaint:", height=100)
    
    uploaded_file = st.file_uploader("Choose a image", type = ['jpg', 'png'])
    
    if uploaded_file is not None:   
        food_item_img = uploaded_file.getvalue()
        st.image(food_item_img)
        st.write("Image Uploaded Successfully")
        return food_item_img
    else:
        st.write("Please upload the image in jpg or png formate")


# 5. Recognize the food items in the picture
def foodItemRecognition(food_img):

    PAT = clarifai_pat
    USER_ID = 'clarifai'
    APP_ID = 'main'

    MODEL_ID = 'food-item-recognition'
    MODEL_VERSION_ID = '1d5fd481e0cf4826aa72ec3ff049e044'

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=food_img
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    food_items = []

    print("Predicted concepts:")
    for concept in output.data.concepts:
        print("%s %.2f" % (concept.name, concept.value))
        if concept.value > 0.10:
            food_items.append(concept.name)
    # Uncomment this line to print the full Response JSON
    print(output)


# 6. Using GPT4-Turbo to test the input and image  
def image_item_test(img_itm_names, input_item_names):
    prompt = "What’s the future of AI?"

    # Setting the inference parameters
    inference_params = dict(temperature=0.2, max_tokens=103)

    # Using the model GPT-4-Turbo for predictions
    # Passing the image-url and inference parameters
    model_prediction = Model("https://clarifai.com/openai/chat-completion/models/gpt-4-turbo").predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)

    # Output
    print(model_prediction.outputs[0].data.text.raw)


def main():
    st.set_page_config(page_title="Interactive Media Creator", layout="wide")
    st.title("Food Complaint Resolution System!")

    with st.sidebar:
        chooseFoodItem() 
        food_item_img = takeComplaintImgs()
       

    col1, col2 = st.columns(2)

    with col1:
        st.header("Recognition")
        if (food_item_img is not None):
            foodItemRecognition(food_item_img)
        
        

    # with col2:
    #     st.header("Col # 2")
    # st.title("Hello")
       

if __name__ == "__main__":
    main()