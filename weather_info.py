#weather api is used to find the weather of the desired location
import requests
from speak import speakclass
from plyer import notification

class weatherinfoclass():
    def weathermethod(cityparam):
      try:
        city=cityparam
        url="https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(city)
        res=requests.get(url)
        #jason format
        output=res.json()
        #ouput contains a dictionary which holds the weather information so we extract data from dictionary in output
        weather_status=output['weather'][0]['description']
        temperature=output['main']['temp']
        humidity=output['main']['humidity']
        wind_speed=output['wind']['speed']
        weather=" The weather status in "+city+" is "+ output['weather'][0]['description'] +"and temperature is"+str(output['main']['temp'])+" degree swith humidity "+str(output['main']['humidity'])+"the wind speed is "+str(output['wind']['speed'])
        print("weather_status",output['weather'][0]['description'])
        print("temperature",output['main']['temp'])
        print("humidity",output['main']['humidity'])
        print("wind_speed",output['wind']['speed'])
        # print(weather)
        #call speak method
        return  weather
        #speakclass.speakmethod(weather)
      except:
          notification.notify(title="Virtual assistant", message="Something went wrong,do check the guide ",
                              timeout=5)
          speakclass.speakmethod("location not found")
