import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt


st.title('Gatinos')

if st.button('Record'):
    client = mqtt.Client("record_aaib")
    client.connect("test.mosquitto.org")
    client. publish("AAIB-TL", payload="Start")