# Celebrity Search Application
This is a Python application that allows users to search for information about celebrities and significant events related to them. The application is powered by OpenAI's Large Language Model (LLM) and integrates with Streamlit for the user interface. This is just a basic application of creating a custom LLM model using langchain. We can improve it by adding more of our custom prompts.

Features:
1) Celebrity Information: Enter the name of a celebrity to learn more about them.
2) Date of Birth: Find out the birthdate of the selected celebrity.
3) Historical Events: Discover five historical events that happened around the world on the celebrity's birthdate.

# Setup and Configuration
#Prerequisites

Before you begin, ensure you have the following installed:

Python (version 3.8 or higher)
streamlit
langchain
openai

#Installation
1) Clone the repository to your local machine
   """git clone <repository-url>
      cd Celebrity-Search"""
2) Install the required packages
   """pip install -r rquirements.txt"""
3) Set up your OpenAI API Key:
   Replace <YOUR_OPENAI_API_KEY> in the constants.py file with your actual OpenAI API Key.
4) Run the application:
   """streamlit run celebrity-search.py"""
   The application should be accessible in the web browser
# usage
1)Open the application in your web browser.
2)Enter the name of the celebrity you want to search for in the provided input field.
3)Click the search button to retrieve information about the celebrity, including their date of birth and historical events.

# Implementation Details
1) Language Model: The application uses OpenAI's large language model to generate responses based on user queries.
2) Memory Functionality: The application utilizes conversation buffer memory to store and retrieve previous conversations, enhancing the user experience by maintaining context between interactions.
3) Streamlit UI: The user interface is created using Streamlit, a popular Python library for building interactive web applications for data science and machine learning.



