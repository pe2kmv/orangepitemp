import sys
import argparse

TempFile = "/sys/class/thermal/thermal_zone0/temp"

parser = argparse.ArgumentParser()
parser.add_argument('-w','--warning')
parser.add_argument('-c', '--critical')
parser.add_argument('-u', '--units')
args = parser.parse_args()

if args.warning == None or args.critical == None:
	print("Please define warning and critical threshold")
	sys.exit(3)

try:
	WarningThresh = float(args.warning)
	CritThresh = float(args.critical)
except:
	print("Thresholds should be numeric")
	sys.exit(3)

if args.units == None:
	TempUnits = "C"
else:
	TempUnits = args.units.upper()

if TempUnits != "C":
	TempUnits = "F"

TempFileOpen = open(TempFile,"r")
temperature = float(str(TempFileOpen.readlines(1))[2:7])/1000
TempFileOpen.close()

if TempUnits == "F":
	temperature = (temperature*1.8)+32

if temperature >= CritThresh:
	print("CRITICAL TEMPERATURE - " + str(temperature) + " deg " + TempUnits + "|cputemp=" + str(temperature))
	sys.exit(2)
elif temperature >= WarningThresh:
	print("TEMPERATURE WARNING - " + str(temperature) + " deg " + TempUnits + "|cputemp=" + str(temperature))
	sys.exit(1)
else:
	print("TEMPERATURE OK - " + str(temperature) + " deg " + TempUnits + "|cputemp="+ str(temperature))
	sys.exit(0)
