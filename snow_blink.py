import sys
import urllib2
import json
from blinkstick import blinkstick

bstick = blinkstick.find_first()

days = int(sys.argv[1])
location = int(sys.argv[2])

response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?id=%s&units=metric&cnt=14' % location)
data = json.load(response)
conditions = int(data['list'][days]['weather'][0]['id'])

print "Forecast for:	 %s" % data['city']['name']
print "Days ahead:	 %s" % days
print "Conditions:	 %s" % data['list'][days]['weather'][0]['main']
print "Max temp:        %s" % data['list'][days]['temp']['max']
print "Min temp:	 %s" % data['list'][days]['temp']['min']
print "Code:		 %s" % conditions

### Thunderstorms range 200 - 232
if conditions >= 200 and conditions <= 232:
   bstick.blink(name="red", repeats=2)
### Drizzle range 300 - 321
if conditions >= 300 and conditions <= 321:
   bstick.blink(name="blue")
### Rain range 500 - 531 
if conditions >= 500 and conditions <= 531:
   bstick.blink(name="blue", repeats=2)
### Snow  600 - 622
if conditions >= 600 and conditions <= 622:
   bstick.pulse(name="white", repeats=2)
### Atmosphere 700 - 781
### Clouds 800 - 804
if conditions >= 800 and conditions < 804:
   bstick.pulse(name="green", repeats=2)
### Extreme 900 - 906
### Additional 950 - 962


