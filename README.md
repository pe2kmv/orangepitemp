# Orange Pi CPU temperature
Script for Nagios to get the OrangePi CPU temperature via NRPE

## Installation
Copy this script into to the NRPE plugins directory at the client computer.
````cp orangepi_temp.py /usr/lib/nagios/plugins````

Then add a suitable command to the nrpe.cfg file (usually /etc/nagios/nrpe.cfg)
