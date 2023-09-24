import requests


class Citi:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.theDataFromAPI()

    def theDataFromAPI(self):

        try:
            respond = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=Your API KEY")

        except Exception:
            print("Could be a connection error blud")
    
        self.respond_json = respond.json()
        self.temp = self.respond_json["main"]["temp"]
        self.tempMin = self.respond_json["main"]["temp_min"]
        self.tempMax = self.respond_json["main"]["temp_max"]


    def printTemp(self):
        units_sum = "C"
        if self.units == "imperial":
            units_sum = "F"
        print(f"In {self.name} It is currently:  {self.temp}° {units_sum}")
        print(f"higher temperature is : {self.tempMax}° {units_sum} ")
        print(f"lower temperature is : {self.tempMin}° {units_sum}")  


mahCity = Citi("Toronto",43.6532,-79.3832 )
mahCity.printTemp()
newcity = Citi("Dubai",25.2048,55.2708, units="imperial")
newcity.printTemp()