# Food Complaint Resolution System
![App logo](https://cdn.discordapp.com/attachments/1194656605648719937/1198287473852301383/image.png?ex=65be5b2c&is=65abe62c&hm=b6e6a4696602cd4fd21fbaeb87c66ddcf007b345cc69c1fedd7e11151a55ca23&)

# Clarifai App Module Template

![Clarifai logo](https://www.clarifai.com/hs-fs/hubfs/logo/Clarifai/clarifai-740x150.png?width=240)

## Introduction

This is a template repository to make it easy to get started creating a UI module with Clarifai.

## Installation

To install and run the Clarifai module locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rsnagarkar10/Clarifai_ai_project.git
    ```

2. **Install the packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

## Features
    - Using AI for receiving the complaint reducing the human effort and time
    - User can select the item, write description and upload images of food for complaint
    - Complain will only be processed when user will provide all the required inputs
    - Using the *Food Item Recognition* model to recognize the food items in the image
    - GPT4-Turbo is used to validating the selected category and image entered
    - GPT4-vision model analyzes the description
    - Cashback or discount provided based on company's rules and regulations
    - User friendly interface for complaint submission
    - A maximum try limit has been set
    - Once the limit gets exceeded, user'll have to refer to the restaurant's management
<!-- Add your features here -->

## Usage
    Food-complaint-resolution uses the streamlit library to provide user ease to complain about the food he received. User can easily select the choice for which he wants to raise the complaint, write the complaint and upload the photos of food. When user will done with entering information our system automatically will use that information to process the user complaint. User can see his complaint is processing, stage and reply (%ag of cashback return to user or not) of complaint from our system. After max tries if user is not satisfied with the reply then our system will redirect the user to human. 
<!-- Add usage information here -->

## Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b yourBranchName`)
3. Commit your Changes (`git commit -m 'Add message here'`)
4. Push to the Branch (`git push origin yourBranchName`)
5. Open a Pull Request
