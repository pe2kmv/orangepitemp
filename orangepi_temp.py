import sys

TempFile = "/sys/class/thermal/thermal_zone0/temp"

WarningThresh = 50
CritThresh = 70

TempFileOpen = open(TempFile,"r")

temperature = float(str(TempFileOpen.readlines(1))[2:7])/1000

if temperature >= CritThresh:
	print("CRITICAL TEMPERATURE - " + str(temperature) + " degrees C")
	sys.exit(2)
elif temperature >= WarningThresh:
	print("TEMPERATURE WARNING - " + str(temperature) + " degrees C")
	sys.exit(1)
else:
	print("TEMPERATURE OK - " + str(temperature) + " degrees C")
	sys.exit(0)
