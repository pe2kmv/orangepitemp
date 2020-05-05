# Orange Pi CPU temperature
Script for Nagios to get the OrangePi CPU temperature via NRPE

## Installation
Copy this script into to the NRPE plugins directory at the client computer.

````cp orangepi_temp.py /usr/lib/nagios/plugins````

Then add a suitable command to the nrpe.cfg file (usually /etc/nagios/nrpe.cfg)

````command[check_cpu_temp]=python /usr/lib/nagios/plugins/orangepi_temp.py -w 50 -c 70 -u C````

## Usage
The script has to be called with the 'warning' and the 'critical' threshold defined. The warning threshold is marked by the '-w' argument, the critical threshold is marked by the '-c' argument. The argument '-u' is optional as this can be used to switch to Fahrenheit. Setting the '-u' argument to 'F' (withouth quotes) switches to Fahrenheit. Any other value or leaving the '-u' argument out will use the Celsius scale.

## Results
After successfull run the script replies with one of four different exit codes and the actual temperature in the units selected.
* exit(0) : OK --> no issue found
* exit(1) : WARNING --> passed warning threshold
* exit(2) : CRITICAL --> passed critical threshold
* exit(3) : UNKNOWN --> error when running script
