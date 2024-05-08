import streamlit as st
import pandas as pd
from tensorflow import keras
from urllib.parse import urlparse
import numpy as np
import os
import re

def load_model():
    model = keras.models.load_model('Malicious_URL_Prediction.h5')
    return model

def save_to_excel(url, result):
    file_path = os.path.join("D:\\url_genie-main\\url_auth\\url_auth", 'analysis_results.xlsx')
    data = {'URL': [url], 'Result': [result]}
    df = pd.DataFrame(data)
    
    if not os.path.exists(file_path):
        df.to_excel(file_path, index=False, sheet_name='AnalysisResults')
    else:
        # Read the existing Excel file
        existing_df = pd.read_excel(file_path)
        # Concatenate the existing DataFrame with the new data
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        # Write the updated DataFrame back to the Excel file
        updated_df.to_excel(file_path, index=False, sheet_name='AnalysisResults')




with st.spinner("Loading Model...."):
    model = load_model()

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://github.com/viii1/url-auth/blob/f901de75a619b3b1d21a884b71a70813a3474046/webapp/assets/url_genie_logo.png?raw=true")

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: #14559E'>URL-Authentication</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #494848;'>Malicious URL Detection Model made using Python</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #494848;'>This program utilizes a Multilayer Perceptron Neural Network model with optimized hyper-parameters using genetic algorithms to perform malicious URL detection</p>", unsafe_allow_html=True)

def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits += 1
    return digits

def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters += 1
    return letters

def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        return -1
    else:
        return 1

def extract_features(url):
    # 'hostname_length', 'path_length', 'fd_length', 'count-', 'count@', 'count?', 'count%', 'count.', 'count=', 'count-http','count-https', 'count-www', 'count-digits','count-letters', 'count_dir', 'use_of_ip'
    hostname_length = len(urlparse(url).netloc)
    path_length = len(urlparse(url).path)
    f_length = fd_length(url)
    count_1 = url.count('-')
    count_2 = url.count('@')
    count_3 = url.count('?')
    count_4 = url.count('%')
    count_5 = url.count('.')
    count_6 = url.count('=')
    count_7 = url.count('http')
    count_8 = url.count('https')
    count_9 = url.count('www')
    count_10 = digit_count(url)
    count_11 = letter_count(url)
    count_12 = no_of_dir(url)
    count_13 = having_ip_address(url)
    output = [hostname_length, path_length, f_length, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10, count_11, count_12, count_13]
    features = np.array([output]) 
    return features

def predict(val):
    st.write(f'Classifying URL: {val}')
    with st.spinner("Classifying..."):
        input = extract_features(val)
        pred_test = model.predict(input)
        percentage_value = pred_test[0][0] * 100
        if pred_test[0] < 0.5:
            result = f'SAFE with {percentage_value:.2f}% malicious confidence'
        else: 
            result = f'MALICIOUS with {percentage_value:.2f}% malicious confidence'
        st.write(result)
        save_to_excel(val, result)

value = st.text_input("Enter URL to scan", "https://www.google.com")
submit = st.button("Classify URL")

if submit:
    predict(value)
