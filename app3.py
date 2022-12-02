import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import json
import time 
from streamlit_autorefresh import st_autorefresh
import matplotlib.pyplot as plt


st.title('Gatinos')
st.header("Choose a wav or mp3 file")
#uploaded_file = st.file_uploader(" ")

client = mqtt.Client("record_aaib")

global y 

y=np.array([])

client.connect("mqtt.eclipseprojects.io", 1883, 60)

if st.button('Record'):
    client.publish("AAIB-TL", payload="start")
    with st.spinner('Wait for it...'):
        time.sleep(10)
        st.success('Done!')


f = open('audios.txt', 'r')
l = len(f.readlines())
f.close()

with open('audios.txt', 'r') as f:
    try:
        if l == 1:
            run = 0
        else: 
            run = st.slider('Record to plot', 1, l, l)-1
        sig = f.readlines()[run]
        x = np.array(sig.strip('\n').split(","))
        y = x[:-1].astype(float)
    except:
        y = np.array([0])
    f.close()

st.line_chart(y)  
st.audio(y, sample_rate=44100)     
        

#st_autorefresh(2000) 



    


