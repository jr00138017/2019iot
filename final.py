#!usr/bin/env python

import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

MotorPin= 3     #use PIN number
TemSenPIN = 29      #use  GPIO number
RPi_Pin = [24 , 23, 19 , 22 ]  #use PIN number
for n in range(4):
	GPIO.setup(RPi_Pin[n], GPIO.OUT)

GPIO.setup(MotorPin,GPIO.OUT)
sensor = Adafruit_DHT.DHT11

humidity, temperature = Adafruit_DHT.read_retry(sensor, __)
pwm_motor = GPIO.PWM(MotorPin, _)  
pwm_motor.start(7.5)

reader = SimpleMFRC522()
status=0    #status of door
win_stat=0  #status of window
steps=128   #the total step of stepper motor
timedelay = 0.02   #delay time control for your stepper motor


print("Welcome to Wisdom Chalet")
print("Press Ctrl-C to stop")

while True:
	pwm_motor.ChangeDutyCycle(0)
	id, text = reader.read()
	print(id)
	if (id == 109763254696  and status == 0):
		print(text)
		for a in range(10):
			pwm_motor.ChangeDutyCycle(7 + a*0.4)    # 0 degree to -90 degree
			time.sleep(0.5)
		if humidity is not None and temperature is not None:
			print('Temp={0:0.1f}*C Humidity={1:0.1f}%' .format(temperature, humidity))
		else:
			print('Failed to get reading. Try again!')
		pwm_motor.ChangeDutyCycle(0)
		if (temperature > 10  and win_stat== 0):
			for i in range(steps):
				for step in ['1100','0110','0011','1001']:
				
					for n in range(4):
						GPIO.output(RPi_pin[n], step[n]=='1')
					time.sleep(timedelay)
			win_stat=1
		status=1
	elif (id == 109763254696  and status == 1):
		print(text)
		if (win_stat==__):
                	for i in range(steps):
                                for step in ['1100','0110','0011','1001']:
                                        for n in range(4):
                                                GPIO.output(RPi_pin[n], step[n]=='1')
                                        time.sleep(timedelay)
			win_stat=0
		for a in range(10):
                        pwm_motor.ChangeDutyCycle(7-a*0.4)   # 0 degree to -90 degree
                        time.sleep(0.5)
		status=0
	else:
		print("yout rfid is wrong")
	time.sleep(timedelay)
