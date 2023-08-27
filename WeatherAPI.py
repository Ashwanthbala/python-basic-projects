import requests

#API Key
API_KEY = "be23939565e85722c7b26d2fb50ec82d"

#API Endpoint
Base_Url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the City name: ")

request_url = f"{Base_Url}?appid={API_KEY}&q={city}"

#Making a get request to the endpoint
response = requests.get(request_url)

if response.status_code == 200:
	data = response.json()
	weather = data['weather'][0]['description']
	print(f"weather:{weather}")
	temperature = data["main"]["temp"] - 273.15
	print(f"Temperature: {temperature}")
else:
	print("An error occured")
