import streamlit as st
import os
from clarifai.modules.css import ClarifaiStreamlitCSS
from clarifai.client.model import Model
from io import BytesIO
import requests
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(layout="wide")
ClarifaiStreamlitCSS.insert_default_css(st)

st.title("Data Labeling using General Object Detection Model and GPT4 Vision")

def main():

    IMAGE_URL = st.text_input("Paste a Image URL below to get started!", value= "https://s3.amazonaws.com/samples.clarifai.com/black-car.jpg")

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

        # req = urlopen(IMAGE_URL)
        # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        # img = cv2.imdecode(arr, -1)  # 'Load it as it is'

        response = requests.get(IMAGE_URL)
        img = Image.open(BytesIO(response.content))

        draw = ImageDraw.Draw(img)

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
                    top_row = top_row * img.height
                    left_col = left_col * img.width
                    bottom_row = bottom_row * img.height
                    right_col = right_col * img.width

                    draw.rectangle([(int(left_col), int(top_row)), (int(right_col), int(bottom_row))],
                                   outline=(36, 255, 12), width=2)

                    # Display text
                    font = ImageFont.load_default()
                    draw.text((int(left_col), int(top_row - 15)), concept_name, font=font, fill=(36, 255, 12))

        st.image(img, caption='Image with Label', channels='BGR', use_column_width=True)

if __name__ == '__main__':
    main()
