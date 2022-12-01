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
uploaded_file = st.file_uploader(" ")

client = mqtt.Client("record_aaib")


client.connect("mqtt.eclipseprojects.io", 1883, 60)

if st.button('Record'):
    client.publish("AAIB-TL", payload="start")

with open('audios.csv', 'r') as f:
    sig = f.read()
    x = np.array(sig.split(", "))
    y = x[:-1].astype(float)
    #print(type(y))
    #plt.plot(y)
    st.line_chart(y)
f.close()

st_autorefresh(interval=2000)




    


