#Imports
import imp
import datetime as dt
import time

#Check for GPIO module
if imp.find_module('RPi.GPIO') == True:
  import RPi.GPIO as GPIO
else:
  sys.exit("GPIO Module not found!")

#GPIO Pin setup
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(XXX, GPIO.OUT)
#h16 = 
#h8 = 
#h4 = 
#h2 = 
#h1 = 

#m32 = 
#m16 =
#m8 = 
#m4 = 
#m2 = 
#m1 = 


#Get time
timenow = dt.datetime.now()
hr = (timenow.hour)
mi = (timenow.minute)

#Binary

#Sleep
#sleep (0.5)
#runagain
