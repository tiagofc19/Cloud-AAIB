import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt


st.title('Gatinos')
client.connect("test.mosquitto.org", port=8501, keepalive = 60)
client. publish("AAIB-", payload="Start")

if st.button('Record'):
    client = mqtt.Client("record_aaib")
    client.connect("test.mosquitto.org", port=8501, keepalive = 60)
    client. publish("AAIB-TL", payload="Start")