import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import signal

continue_reading = True
def end_read(signal , frame):
	global continue_reading
	continue_reading = False
	GPIO.cleanup()

reader = SimpleMFRC522()


try:
	while True:
		id,text = reader.read()
		print(id)
		print(text)
finally:
	signal.signal(signal.SIGINT , end_read)
	GPIO.cleanup()
