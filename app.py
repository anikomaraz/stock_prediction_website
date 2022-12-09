import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import datetime
from datetime import date

import requests
import urllib.parse

from PIL import Image
from io import BytesIO
import json




'''
# Welcome to our stock prediction model.

On the following page we'll make you rich. You are welcome!
'''

options_8000 = pd.read_csv('nasdaq_current_list_12112012.csv')
options = list(options_8000['Name'])
options.insert(0, '')

stock_name = st.selectbox("Type in a stock name:", options, index = 1)


'''
#### You requested prediction for the following stock: 
'''

st.write(stock_name)


# get price prediction from UI
# for local running use: 
# url = "http://127.0.0.1:8000/predict"

url = 'https://gcloud-5cp25n2jkq-ew.a.run.app/predict'

params = {'stock' : stock_name}
response = requests.get(url, params = params)
stock_prediction = response.json() 


#st.write(stock_prediction)


'''
### This is what you can expect
'''

# image = requests.post("http://localhost:8079/plot", json = {'stock_prediction': stock_prediction})
image = requests.post("https://stock-prediction-r-62x2mlrora-ew.a.run.app/plot", 
                      json = {'stock_prediction': stock_prediction})


st.image(Image.open(BytesIO(image.content)), output_format='png')


st.markdown('''
            [Presentation](https://docs.google.com/presentation/d/19aNmhq5w_C1ThRsP_EZY7e-rMWd3qpLElBNvaPwczj8/edit?usp=sharing)
             
            [Project Git Repo](https://github.com/rahulvaity25/stock_prediction)
            
            [Under the hood: running two containers (Python and R) and connecting to the frontend](https://github.com/anikomaraz/stock_prediction_2containers_blogpost)
            
            aniko.maraz[at]gmail.com  -----    rahul.vaity25[at]gmail.com   -----   ruitang1996[at]gmail.com
            ''')
