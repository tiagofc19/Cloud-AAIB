import streamlit as st
import pandas as pd
import numpy as np
import context 
import paho.mqtt.publish as publish


st.title('Gatinos')

if st.button('Record'):
    publish.single("AAIB-TL", "Lu gosta de gatinos", hostname="test.mosquitto.org")