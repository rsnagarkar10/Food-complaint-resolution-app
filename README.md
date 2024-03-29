[![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-brightgreen)](https://www.streamlit.io/)
[![Clarifai](https://img.shields.io/badge/Clarifai-9.10.4-blue)](https://www.clarifai.com/)
[![Python](https://img.shields.io/badge/Python-3.11.3-blue)](https://www.python.org/)

# Food Complaint Resolution
<p align="center">
  <a href="https://github.com/rsnagarkar10/Food-complaint-resolution-app"><img src="images/assets/logo.png" alt="logo.svg" height="200" width = "200"/></a>
</p>


#

<p align="center">
  <strong> User-Friendly AI-Driven Food Delivery Complaint System</strong>
</p>

![GitHub Stars](https://img.shields.io/github/stars/rsnagarkar10/Clarifai_ai_project?style=social)
![GitHub Forks](https://img.shields.io/github/forks/rsnagarkar10/Clarifai_ai_project?style=social)
![GitHub Watchers](https://img.shields.io/github/watchers/rsnagarkar10/Clarifai_ai_project?style=social)

<!-- ![](/images/cover.png) -->
<p align="center">
  <img src="images/assets/cover.png" alt="cover.png" width = "600" height = "500">
</p>

The food complaint resolution application is an AI-based customer complaint system tailored to the food delivery industry. While many food delivery companies already have a customer complaint system, it typically involves human intervention to address customer concerns.

For instance, if a customer orders pita bread and receives expired bread, filing a complaint triggers a human review process. The human evaluator assesses the complaint using metadata such as images of the bread and the complaint description. Following this evaluation, the customer may be reimbursed if the human determines that the delivered pita bread has indeed expired. However, this manual process is time-consuming and dependent on the availability of human personnel.

By utilizing the food complaint resolution application, a food delivery company can significantly reduce processing time and human effort in handling complaints. The application can swiftly process customer complaints in a matter of seconds, streamlining the resolution process.

We developed this application with ❤️, incorporating state-of-the-art AI models such as Food Item recognition, GPT-4 Turbo, and GPT-4 vision to automate complaint resolution. The user-friendly interface, created using the Streamlit library, ensures a seamless experience for users.

The system mimics human evaluation by processing complaints based on metadata like complaint descriptions and images. After analyzing the information provided by the customer, our system adheres to company policies to provide cash back to eligible customers. If a customer remains dissatisfied with the refund or after reaching the maximum attempts, the system redirects the complaint to human intervention.

### Features
    - Using AI for receiving complaints reduces human effort and time
    - User can select the item, write a description, and upload images of food for complaint
    - Complaint will only be processed when the user provides all the required inputs
    - Using the *Food Item Recognition* model to recognize the food items in the image
    - GPT4-Turbo is used to validate the selected category and image entered
    - GPT4-vision model analyzes the description
    - Cashback or discount provided based on the company's rules and regulations
    - User-friendly interface for complaint submission
    - A maximum try limit has been set
    - Once the limit is exceeded, the user will be referred to a human agent for better understanding and resolution.

### Built with
* [Clarifai's streamlit module](https://github.com/clarifai/module-template) - a template for creating a UI module with Clarifai using streamlit 
* [Food Item Recognition](https://clarifai.com/clarifai/main/models/food-item-recognition) - AI model for recognizing a wide variety of food items in images
* [GPT-4 Turbo](https://clarifai.com/openai/chat-completion/models/gpt-4-turbo) - is an advanced language model (LLM)
* [GPT-4 vision](https://clarifai.com/openai/chat-completion/models/gpt-4-vision) - extends GPT-4's capabilities that can understand and answer questions about images

## Installation

To install and run Food Complaint Resolution locally, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rsnagarkar10/Food-complaint-resolution-app.git

    ```

2. **Install the packages:**

    ```bash
        pip install -r requirements.txt
    
    ```

3. **Run the Application**
<br>Make sure to update the .env_example with your CLARIFAI_PAT or provide PAT through UI on application
    ```bash
        streamlit run app.py
    
    ```

## Usage
Food Complaint Resolution simplifies the complaint process using the streamlit library. Users select their issue, share details, and upload photos. Our system swiftly processes complaints, providing real-time updates on the processing stage and response (% cashback). After maximum attempts, if unsatisfied, users are redirected to human intervention. Efficient and user-friendly, it blends automated resolution with personalized human assistance. 

### Visuals
![](/images/assets/app_tour.png)
As the user fills in all input fields the processing will start:
![](/images/assets/Input.png)
After Processing is done user can see the results:
![](/images/assets/output.png)

### Where to ask for help?
Open a discussion or stop by our [discord](https://discord.gg/n58UfpCX) server

## Contributing 

Contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute to the Food Complaint Resolution App, 

Clone this repo locally and commit your code on a separate branch.
If you're making core changes please write unit tests for your code, and check that everything works by running the following before opening a pull-request

or 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b yourBranchName`)
3. Make changes and make sure everything is working fine
4. Commit your Changes (`git commit -m 'Add message here'`)
5. Push to the Branch (`git push origin yourBranchName`)
6. Open a Pull Request

## Team Members
This software is written by the mutual effort of diverse team members :
**Team Leader [Indar Kumar](https://www.linkedin.com/in/indarkarhana/)**,
[Inam ul Rehman](https://www.linkedin.com/in/inamulrehman/),
[Jaweria Batool](https://www.linkedin.com/in/jaweria-batool/),
[Ranjeet Nagarkar](https://www.linkedin.com/in/ranjeet-nagarkar-772060104/),
[Ayesha Mehmood](https://www.linkedin.com/in/ayesha-mehmood-9264a228b/) and
[Usman Ali](https://www.linkedin.com/in/usmaneali/).

Also, thanks to all [contributors](https://github.com/rsnagarkar10/Food-complaint-resolution-app/graphs/contributors) of the software.

### Demo
See the demo [here](https://clarifai.com/inam09/Food_Complaint_Resolution/installed_module_versions/customer-complaint-handler).
