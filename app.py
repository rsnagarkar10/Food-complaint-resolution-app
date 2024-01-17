import streamlit as st
import os
from dotenv import load_dotenv
from clarifai.client.model import Model
import cv2
from urllib.request import urlopen
import numpy as np
from clarifai.modules.css import ClarifaiStreamlitCSS
from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

st.set_page_config(layout="wide")
st.title("Food Complaint Resolution System!")

load_dotenv()
CLARIFAI_PAT = os.getenv("CLARIFAI_PAT")



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
    description = st.text_area("Enter your complaint:")
    
    uploaded_file = st.file_uploader("Choose a image", type = ['jpg', 'png'])
    
    if uploaded_file is not None:   
        food_item_img = uploaded_file.getvalue()
        st.image(food_item_img)
        st.write("Image Uploaded Successfully")
        return food_item_img
    else:
        st.write("Please upload the image in jpg or png formate")



# 3. Function to recogonize the Food item from image
def foodItemRecognition(food_img):

    PAT = CLARIFAI_PAT
    # Specify the correct user_id/app_id pairings
    # Since you're making inferences outside your app's scope
    USER_ID = 'clarifai'
    APP_ID = 'main'
    # Change these to whatever model and image URL you want to use
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
    # print(output)
    
    
    
    
def main():

    chooseFoodItem()    
    food_img = takeComplaintImgs()
    foodItemRecognition(food_img)
    
    # Clarifai Credentials
    with st.sidebar:
        st.subheader('Add your Clarifai PAT.')
        clarifai_pat = st.text_input('Clarifai PAT:', type='password')
    if not clarifai_pat:
        st.warning('Please enter your PAT to continue!', icon='⚠️')
    else:
        os.environ['CLARIFAI_PAT'] = clarifai_pat

        detector_model = Model("https://clarifai.com/clarifai/main/models/objectness-detector")

        prediction_response = detector_model.predict_by_url(IMAGE_URL, input_type="image")

        # Since we have one input, one output will exist here
        regions = prediction_response.outputs[0].data.regions

        model_url = "https://clarifai.com/openai/chat-completion/models/gpt-4-vision"
        classes = ['Ferrari 812', 'Volkswagen Beetle', 'BMW M5', 'Honda Civic']
        threshold = 0.99

        req = urlopen(IMAGE_URL)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)  # 'Load it as it is'

        for region in regions:
            # Accessing and rounding the bounding box values
            top_row = round(region.region_info.bounding_box.top_row, 3)
            left_col = round(region.region_info.bounding_box.left_col, 3)
            bottom_row = round(region.region_info.bounding_box.bottom_row, 3)
            right_col = round(region.region_info.bounding_box.right_col, 3)

            for concept in region.data.concepts:
                # Accessing and rounding the concept value
                prompt = f"Label the Car in the Bounding Box region: ({top_row}, {left_col}, {bottom_row}, {right_col}) with one word {classes}"

                inference_params = dict(temperature=0.2, max_tokens=100, image_url=IMAGE_URL)

                # Model Predict
                model_prediction = Model(model_url).predict_by_bytes(prompt.encode(), input_type="text", inference_params=inference_params)

                concept_name = model_prediction.outputs[0].data.text.raw
                value = round(concept.value, 4)

                if value > threshold:
                    # Multipy by axis
                    top_row = top_row * img.shape[0]
                    left_col = left_col * img.shape[1]
                    bottom_row = bottom_row * img.shape[0]
                    right_col = right_col * img.shape[1]

                    cv2.rectangle(img, (int(left_col), int(top_row)), (int(right_col), int(bottom_row)), (36, 255, 12), 2)

                    # Display text
                    cv2.putText(img, concept_name, (int(left_col), int(top_row - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (36, 255, 12), 2)

        st.image(img, caption='Image with Label', channels='BGR', use_column_width=True)

if __name__ == '__main__':
    main()
