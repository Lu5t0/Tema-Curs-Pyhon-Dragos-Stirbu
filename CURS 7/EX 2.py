bucuresti = {
  "coord": {
    "lon": 26.1063,
    "lat": 44.4323
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01n"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 286.87,
    "feels_like": 286.07,
    "temp_min": 284.2,
    "temp_max": 289.74,
    "pressure": 1022,
    "humidity": 68
  },
  "visibility": 10000,
  "wind": {
    "speed": 1.03,
    "deg": 260
  },
  "clouds": {
    "all": 0
  },
  "dt": 1666984646,
  "sys": {
    "type": 2,
    "id": 2037828,
    "country": "RO",
    "sunrise": 1666932421,
    "sunset": 1666969892
  },
  "timezone": 10800,
  "id": 683506,
  "name": "Bucharest",
  "cod": 200
}
main1 = bucuresti["main"]
temp_celsius = (f"{bucuresti["main"]["temp"] - 273.15:.1f}")
oras = bucuresti["name"]
cerul = bucuresti["weather"][0]["description"]
print(f"Temperatura in orasul {oras} este de {temp_celsius} grade celsius si cerul este {cerul}.")





