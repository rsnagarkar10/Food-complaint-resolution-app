<div style="display:flex;"> 

<h1 style="margin:auto"> Food Complaint Resolution System</h1>

<img src="https://cdn.discordapp.com/attachments/1194656605648719937/1198287473852301383/image.png?ex=65be5b2c&is=65abe62c&hm=b6e6a4696602cd4fd21fbaeb87c66ddcf007b345cc69c1fedd7e11151a55ca23&" alt="App logo" style="width:200px; margin-left:20px;"/>

</div>

## Introduction

Food Complaint Resolution System, powered by the cutting-edge synergy of GPT-4 Turbo, GPT-4 Vision, and a Language Model (LLM) in collaboration with Clarifai, is not just an app; it's your ultimate ally in culinary satisfaction. 
- Ever faced a dining dilemma or encountered a dish that didn't quite meet your expectations? 
Fret not! 
- Our streamlit application revolutionizes the way you express food complaints by seamlessly integrating language understanding and visual analysis. Simply submit your grievance, accompanied by a snapshot of the culinary hiccup, and let the advanced AI algorithms work their magic. Our App not only listens to your concerns but goes a step further, offering personalized resolutions in the form of enticing cashbacks or discounts.

<div style="display:flex;"> 

# Clarifai
<!-- <h1 style="margin:auto"> Clarifai </h1> -->

<img src="https://www.clarifai.com/hs-fs/hubfs/logo/Clarifai/clarifai-740x150.png?width=240" alt="Clarifai logo" style="width:200px; margin:auto 50px;"/>

</div>

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

## Contributing

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b yourBranchName`)
3. Commit your Changes (`git commit -m 'Add message here'`)
4. Push to the Branch (`git push origin yourBranchName`)
5. Open a Pull Request
