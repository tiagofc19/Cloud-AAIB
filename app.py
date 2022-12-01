import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt


def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    m_in=json.loads(m_decode) #decode json data
    print(type(m_in))
    print("broker 2 address = ",m_in["broker2"])


st.title('Gatinos')
y = st.header("Choose a wav or mp3 file")
uploaded_file = st.file_uploader("")

if st.button('Record'):
    client = mqtt.Client("record_aaib")
    client.connect("test.mosquitto.org")
    client. publish("AAIB-TL", payload="start")

if st.button('recieve'):
    client.on_message = on_message()
    client.loop_forever()