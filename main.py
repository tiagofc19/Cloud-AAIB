import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import librosa
import json


def on_message(mqttc, obj, msg):
    print(msg.payload.decode('UTF-8'))
    if msg.payload.decode('UTF-8') == 'start':
        # Sampling frequency
        fs = 44100

        # Recording duration
        max_duration = 5

        # Start recorder with the given values of
        # duration and sample frequency
        recording = sd.rec(int(max_duration * fs),
                       samplerate=fs, channels=1)

        # Record audio for the given number of seconds
        sd.wait()
        file_name = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
        print(file_name)

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write(file_name + '.wav', fs, recording)

        x, sr = librosa.load(file_name + '.wav', sr = fs)

        lst = [float(val) for val in x]

        lst_json = json.dumps(lst)
        mqttc.publish('AAIB-LT', payload = lst_json)


try:
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.connect("mqtt.eclipseprojects.io")
    mqttc.subscribe("AAIB-TL", 0)

    mqttc.loop_forever()

except KeyboardInterrupt:
    print('Communication terminated.')
