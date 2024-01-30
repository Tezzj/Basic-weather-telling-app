import requests
import json
import win32com.client as wincom

city = input('Enter the name of the city: \n')
url = f"http://api.weatherapi.com/v1/current.json?key=06a4b645c1e64bb78fe141544242901&q={city}"
# We are using api from weatherapi.com. We have given a key provided by the site to make our api work

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)  # This will convert a string into a dictionary
print(wdic['current']['temp_c'])

# We are using text to speech module using wincom32 package
speak = wincom.Dispatch("SAPI.SpVoice")

text = (f"The current temperature in {city} is {wdic['current']['temp_c']} degree celcius "
        f"the humidity is {wdic['current']['humidity']} percent and the windspeed is {wdic['current']['wind_kph']} km/h")
speak.Speak(text)



