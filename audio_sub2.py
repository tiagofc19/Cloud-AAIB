
import paho.mqtt.client as mqtt
import json
from csv import writer


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))



def on_message(mqttc, obj, msg):
    topic=msg.topic
    #print(msg.payload.decode("utf-8","ignore"))
    #y = msg.payload.decode("utf-8","ignore")
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    #print("data Received type",type(m_decode))
    #print("data Received",m_decode)
    #print("Converting from Json to Object")
    m_in=json.loads(m_decode) 
    print(type(m_in))
    #if y == 'new':
    #    file = open('audios.csv', 'a')
    #    file.close()

    with open('audios.txt', 'a') as f:
        for num in m_in:
            f.write(str(num)+',')
        f.write('\n')
        f.close()

    #with open('audios.csv', 'a') as f:
    #    writer_object = writer(f)
    #    writer_object.writerow(m_in)
    #    f.close()
    
          

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
#mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
mqttc.subscribe("AAIB-LT", 0)

#rc = 0

#while rc == 0:
    #rc = mqttc.loop()
#print("rc: " + str(rc))

mqttc.loop_forever()