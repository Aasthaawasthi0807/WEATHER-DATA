import requests
#import os
from datetime import datetime

api_key = 'd78f9cd59dbfa26c40b1f75271ced263'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

dataDir = r"C:\Users\awast\Desktop\AASTHA\AASTHA PYTHON\Shapeai Weather Data Project.py"
dataDir_out = r"C:\Users\awast\Desktop\AASTHA\AASTHA PYTHON\Shapeai Weather Data Project.py"

sidArr = ["53463"]
fields = ["TEM", "TMN", "TMX", "PRE", "RHU", "WIN", "PRS", "SSD"]  
START = "2021-06-22"
END = "2021-12-22"


