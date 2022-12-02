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
    uploaded_file = None
    with st.spinner('Wait for it...'):
        time.sleep(13)
        st.success('Done!')
#print('ola')
if uploaded_file is not None:
    print(uploaded_file)
    dataframe = pd.read_csv(uploaded_file)
    print(dataframe)
    y = dataframe.iloc[0].to_numpy()
    print('ola2')
    
    #with open(uploaded_file, 'r') as f:
    #try:
        #sig = f.readlines()[-1]
        #x = np.array(sig.split(", "))
        #y = x[:-1].astype(float)
    st.line_chart(y)  
    #except:
     #   st.line_chart([])
else:        
    with open('audios.csv', 'r') as f:
        try:
            sig = f.readlines()[-1]
            x = np.array(sig.split(", "))
            y = x[:-1].astype(float)
            #print(type(y))
            #plt.plot(y)
            st.line_chart(y)  
            st.audio(y, sample_rate=44100)  
            #
        except:
            st.line_chart([])

st_autorefresh(2000) 



    


