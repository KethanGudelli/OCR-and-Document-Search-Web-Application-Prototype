OCR and Document Search Web Application
Project Description
The OCR and Document Search Web Application is a web-based tool designed to extract text from images containing Hindi and English text using Optical Character Recognition (OCR). It allows users to upload images via a URL, processes the images using a pre-trained OCR model, and displays the extracted text. The application also features a keyword search function, enabling users to search for specific words within the extracted text. Built using Python, Huggingface Transformers, and Gradio, this project provides a simple interface for extracting and searching text from multilingual images.


Table of Contents
Project Description
Environment Setup
How to Run the Application
Usage
Dependencies
Assumptions
License
Environment Setup:
Create a Virtual Environment:
Activate the Virtual Environment:
Install Dependencies:
How to Run the Application
Run the Application:
python app.py
Access the Application: After running the command, a local URL will be provided. Open it in your browser to access the OCR and search interface
Usage
Steps:
Open the web application in your browser after running the app locally.
Enter an Image URL: Paste the URL of the image you want to process.
Enter a Keyword: Input the keyword you want to search within the extracted text.
Click Submit to view the extracted text and search results.
Supported Image Formats:
JPEG
PNG
Dependencies
The project relies on the following Python libraries:

Python 3.8 or higher
torch==2.0.1
torchvision==0.15.2
transformers==4.37.2
gradio==3.2
requests==2.31.0
numpy==1.23.5

Install these dependencies using:
pip install -r requirements.txt
Assumptions
The input images contain text in Hindi or English, and the text is legible.
The OCR model is pre-trained and optimized for both Hindi and English text extraction.
The application is currently designed as a prototype with basic functionality for extracting and searching text.
License
This project is licensed under the MIT License.
