import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import json
import time 

st.title('Gatinos')
st.header("Choose a wav or mp3 file")
uploaded_file = st.file_uploader(" ")

client = mqtt.Client("record_aaib")


client.connect("test.mosquitto.org", 1883, 60)

if st.button('Record'):
    client.publish("AAIB-TL", payload="start1")



    


