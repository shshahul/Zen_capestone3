import easyocr as ocr
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector
from pymongo import MongoClient

st.title("Easy-OCR-Extract Business Card Data")

image = st.file_uploader(label="Upload image", type=['png', 'jpg', 'jpeg'])


@st.cache
def load_model():
    reader = ocr.Reader(['en'], model_storage_directory='.')
    return reader


reader = load_model()
result_text = []

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)

    with st.spinner("Loading information!"):
        result = reader.readtext(np.array(input_image))





        for text in result:
            result_text.append(text[1])



        #st.write(result_text)

else:
    st.write("Upload an image")





image_df = pd.DataFrame(result_text)
image_df.drop([7], axis = 0,inplace=True)
# image_df.loc[2].combine_first(image_df.loc[3])
df = image_df.rename(columns = {0:'Data'},index={0 :'Name',1:'Designation',2:'Mobile Number1',3:'Mobile Number2', 4: 'Website URL',
                             5:'Email Address', 6:"area and city", 8:"stae & Pincode",9:"company name"})
df['Data'] = df['Data'].replace(['digitals'], "selva digitals")

st.dataframe(df)

st.dataframe(df.T)

a = df.T.columns
print(a)



st.download_button("Download CSV",
                       df.to_csv(),
                       mime="text/csv")

#saving the data in MYSQL Database

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Shahul@99',
    port = '3306'
)

if mydb:
    print('sucessfully connected')
else:
    print('unsucessfully connected')

cursor = mydb.cursor()
cursor.execute('show databases')
db = cursor.fetchall()
for i in db:
    print(i)
#choosing the database

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Shahul@99',
    port = '3306',
    database = 'capestone3'
)

# mycursor = mydb.cursor()
# mycursor.execute(
#     "CREATE TABLE Businesscard_info(Name varchar(50),Designation varchar(50),Mobile Number1 int(50),Mobile Number2 int(50),"
#     "Website URL varchar(50),Email Address varchar(50),area and city varchar(50),stae & Pincode varchar(50),"
#     "company name varchar(50))")
# print("Table is created....")
# for i in a.iterrows():
#     sql = "INSERT INTO capestone3.Businesscard_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
#     mycursor.execute(sql,tuple(i))
#     print("Record inserted")
#     mydb.commit()
#
# # except Error as e:
# #             print("Error while connecting to MySQL", e)
#Updating the information to MongoDB
with st.form(key="Updating_Tweets_in_to_DataBase"):
    if st.form_submit_button(label='Update'):
        client = MongoClient('mongodb+srv://shaikshahul:shahul@cluster0.jx5r6nd.mongodb.net/?retryWrites=true&w=majority')
        db = client.Tweets_database
        collection = db.info_collection
        info_data = df.to_dict("records")


        Update = collection.insert_many(info_data)

        for i in collection.find({"Name": 'Selva'}):
            print(i)
    #Retrive the data from Database



