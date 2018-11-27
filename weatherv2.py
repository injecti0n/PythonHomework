# Grabbing the weather
# Injecti0n
# hack4.net

from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'
# id number = 505307
weather = get(url).json()
first_record = weather['items'][0]
ambient_temp = weather['items'][0]['ambient_temp']

temperatures = []
for record in weather['items']:
    temperature = record['ambient_temp']
    temperatures.append(temperature)

timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
plt.plot(timestamps, temperatures)
## Set the axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.savefig('foo.png')
plt.show()
#info
print(first_record, "\n")
print("Ambient Temp= " , ambient_temp, "\n")
print("Temperatures : " , temperatures, "\n")
print(timestamps)