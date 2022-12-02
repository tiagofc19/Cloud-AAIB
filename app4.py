import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import json
import time 
from streamlit_autorefresh import st_autorefresh
import matplotlib.pyplot as plt
import librosa.display
import scipy
from io import StringIO
from os import remove


st.title('AAIB - Audio Feature Extraction')
st.header("Choose or record an audio file.")
uploaded_file = st.file_uploader("Choose a .wav file.",type = ['.wav'])

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

    bytes_data = uploaded_file.getvalue()
    filename = 'uploaded_file.wav'
    try:
        with open(filename, mode='bx') as f:
            f.write(bytes_data)
        f.close()
    except FileExistsError:
        remove(filename)
        with open(filename, mode='bx') as f:
            f.write(bytes_data)
        f.close()

    y, sr = librosa.load('myfile.wav', sr=44100)
    step = 1/44100

    st.markdown("Here's the audio file you uploaded.")

    fig4 = plt.figure(figsize=(20, 5))
    plt.xlim(0, (len(y)*step))
    plt.xlabel('Time, s')
    plt.grid('on')
    librosa.display.waveshow(y, sr=sr, color='#DAF7A6')
    st.pyplot(fig4)
    

    #with open(uploaded_file, 'r') as f:
    #try:
        #sig = f.readlines()[-1]
        #x = np.array(sig.split(", "))
        #y = x[:-1].astype(float)
    #st.line_chart(y)  
    #except:
     #   st.line_chart([])
else:        
    with open('audios.csv', 'r') as f:
        try:
            # Load audio info
            sig = f.readlines()[-1]
            x = np.array(sig.split(", "))
            y = x[:-1].astype(float)
            fs = 44100
            sr = 22050
            step = 1/fs
            #t = np.arange(0, (len(y)*step), step)

            st.markdown("Listen to the audio file.")
            #Play audio
            st.audio(y, sample_rate=44100)

            st.markdown("This is what your audio file looks like.")
            # Plot audio
            #st.line_chart(y) 
            fig1 = plt.figure(figsize=(20, 5))
            plt.xlim(0, (len(y)*step))
            plt.xlabel('Time, s')
            plt.grid('on')
            librosa.display.waveshow(y, sr=sr, color='#DAF7A6')
            #fig, ax = plt.subplots(figsize=(20, 5))  
            #ax.grid('on')
            #ax.plot(t, y)
            #ax.set_xlim(0, (len(y)*step))
            #ax.set_xlabel('Time, s')
            st.pyplot(fig1)

            st.markdown("Here's the audio's spectrogram.")
            # Plot spectogram
            X = librosa.stft(y)
            Xdb = librosa.amplitude_to_db(abs(X))
            fig2 = plt.figure(figsize=(20, 5))
            librosa.display.specshow(Xdb, sr=fs, x_axis='time', y_axis='hz')
            plt.colorbar(cmap='viridis')
            st.pyplot(fig2)

            st.markdown("Here's the 1D frequency spectrum of the audio.")
            

            # Plot 1D Frequency Spectrum
            fft_spectrum = np.fft.rfft(y)
            freq = np.fft.rfftfreq(y.size, d=1./fs)
            
            #max_val = freq[-1]
            max_freq = st.slider('Select maximum frequency to plot.', 0, 2000, 1000)

            fft_spectrum_abs = np.abs(fft_spectrum)
            fig3 = plt.figure(figsize=(20, 5))
            plt.plot(freq, fft_spectrum_abs, color='#DAF7A6')
            plt.xlabel("Frequency, Hz")
            plt.ylabel("Amplitude")
            plt.xlim([0,int(max_freq)])
            plt.grid('on')
            st.pyplot(fig3)          

            freq_str = 'Most prominent frequency: '+str(round(freq[np.argmax(fft_spectrum_abs)],2))+' Hz'
            st.markdown(freq_str)


            st.balloons()

            #st_autorefresh(2000)
        except:
            st.line_chart([])

#st_autorefresh(2000)