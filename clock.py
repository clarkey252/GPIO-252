import imp
#Check for GPIO module
if imp.find_module('GPIO') == True:
  import GPIO
else:
  sys.exit("GPIO Module not found!")

#GPIO Pin setup

