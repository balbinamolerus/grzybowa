from time import sleep
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

broker_address = "192.168.1.200"
client = mqtt.Client()
client.username_pw_set("Raspberry_Pi", "Rpi_Raspberry_Python")
client.connect(broker_address, 1883)
client.loop_start()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)

while True:
    now = GPIO.input(17)
    print(now)
    if now == 1:
        print('alarm')
        sleep(1)
    else:
        print('xD')
        sleep(1)
