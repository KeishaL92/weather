import requests

# call api


def get_weather_data(zip=None, city=None):
weatherUrl = "http://api.openweathermap.org/data/2.5/weather?units=imperial"
apiid = "b351ed55b6d002c164596cc4d454c94e" #my api code

# using zip or city
if zip is not None:
weatherUrl += "&zip="+str(zip)+",us"
else:
weatherUrl += "&q="+str(city)+",us"
weatherUrl += "&appid="+str(apiid)
r = requests.get(weatherUrl)
# return the response
return r

#data info


def display(resp):
data = resp.json()
print(f"""{data['name']} Weather Forecast:
Min. Temp : {data['main']['temp_min']} F
Max Temp : {data['main']['temp_max']} F
""")


def main():
while True:
#searching by city/zip?
choice = int(input("Please select 1 to search by zip or 2 to search by city: ))

if choice == 1:
#get valid zip
userZip = int(input("Enter valid zip code : "))
#get data
resp = get_weather_data(zCode, None)
display(resp)
except Exception as ex:
print("Invalid input. Please try again!", ex)

elif choice == 2:
userCity = input("Enter city name : ")
# mak call to fetch fetch_data
resp = get_web_data(None, cname)
display(resp)
except Exception as ex:
print("Invalid input. Please try again!", ex)



