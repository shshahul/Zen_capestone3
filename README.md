# Zen_capestone3
Problem Statement:
You have been tasked with developing a Streamlit application that allows users to
upload an image of a business card and extract relevant information from it using
easyOCR. The extracted information should include the company name, card holder
name, designation, mobile number, email address, website URL, area, city, state,
and pin code. The extracted information should then be displayed in the application's
graphical user interface (GUI).
In addition, the application should allow users to save the extracted information into
a database along with the uploaded business card image. The database should be
able to store multiple entries, each with its own business card image and extracted
information.
To achieve this, you will need to use Python, Streamlit, easyOCR, and a database
management system like SQLite or MySQL. The application should have a simple
and intuitive user interface that guides users through the process of uploading the
business card image and extracting its information. The extracted information should
be displayed in a clean and organized manner, and users should be able to easily
add it to the database with the click of a button. And Allow the user to Read the data,
Update the data and Allow the user to delete the data through the streamlit UI
This project will require skills in image processing, OCR, GUI development, and
database management. It will also require you to carefully design and plan the
application architecture to ensure that it is scalable, maintainable, and extensible.
Good documentation and code organization will also be important for this project.



**#Import Requirements**

 import streamlit as st
 
 import snscrape.modules.twitter as sntwitter
 
 import pandas pd
 
 import easyocr as ocr
 
from PIL import Image

import mysql.connector

from pymongo import MongoClient

# Result

![Capture](https://user-images.githubusercontent.com/103018333/228930351-9b8d07be-bafc-4f0b-958c-3e65ab80afa4.PNG)


![Capture2](https://user-images.githubusercontent.com/103018333/228930578-568d36df-7d3b-4a2c-8a37-142b74b46276.PNG)

