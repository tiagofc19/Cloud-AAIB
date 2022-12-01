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

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    m_in=json.loads(m_decode)
    print(type(m_in))
    print("broker 2 address = ",m_in["broker2"])


client.connect("test.mosquitto.org", 1883, 60)
client.on_message = on_message
client.on_subscribe = on_subscribe


sub_ready = 0

client.on_subscribe = on_subscribe
client.subscribe("AAIB-LT", 0)

if st.button('Record'):
    print("0")
    client.disconnect()
    client.connect("test.mosquitto.org", 1883, 60)
    client.publish("AAIB-TL", payload="start1")



    


