##PINS
P1 = 15 #HR1
P2 = 16 #HR2
P3 = 21 #HR4
P4 = 26 #HR8
P5 = 24 #HR16
P6 = 3 #MIN1
P7 = 5 #MIN2
P8 = 8 #MIN4
P9 = 10 #MIN8
P10 = 11 #MIN16
P11 = 12 #MIN32

#Imports
import imp
import datetime as dt
import time
import RPi.GPIO as GPIO


#GPIO Pin setup
GPIO.setmode(GPIO.BOARD)
hourleds = {1 : P1, 2 : P2, 4 : P3, 8 : P4, 16 : P5}
minleds = {1 : P6, 2 : P7, 4 : P8, 8 : P9, 16 : P10, 32 : P11}

for i in hourleds:
	GPIO.setup(hourleds[i], GPIO.OUT)
for i in minleds:
	GPIO.setup(minleds[i], GPIO.OUT)
	
#mainloop
while True:
	for i in hourleds:
		GPIO.output(hourleds[i], True)
	for i in minleds:
		GPIO.output(minleds[i], True)
		
	time.sleep(0.5)
	for i in hourleds:
		GPIO.output(hourleds[i], False)
	for i in minleds:
		GPIO.output(minleds[i], False)
	time.sleep(0.5)
