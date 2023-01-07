import requests, json
timezone = "EET"
latitude = 62.5861
longitude = 23.6194

results = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = results.json()

#if we fail to access the API
if results.status_code != 200:
    print("Error accessing API.")

#get weathercode and print it out
weathercode = user["daily"]["weathercode"][0]

if weathercode == 0:
    weather = "clear sky"
elif weathercode == 1 or weathercode == 2 or weathercode == 3:
    weather = "Mainly clear, partly cloudy, and overcast"
elif weathercode == 73 or weathercode == 71 or weathercode == 75:
    weather = "Snow fall: Slight, moderate, and heavy intensity"
elif weathercode == 45 or weathercode == 48:
    weather = "Fog and depositing rime fog"
elif weathercode == 51 or weathercode == 53 or weathercode == 55:
    weather = "Drizzle: Light, moderate, and dense intensity"
elif weathercode == 56 or weathercode == 57:
    weather = "Freezing Drizzle: Light and dense intensity"
elif weathercode == 61 or weathercode == 63 or weathercode == 65:
    weather = "Rain: Slight, moderate and heavy intensity"
elif weathercode == 66 or weathercode == 67:
    weather = "Freezing Rain: Light and heavy intensity"
elif weathercode == 77:
    weather = "Snow grains"
elif weathercode == 95:
    weather = "Thunderstorm: Slight or moderate"
elif weathercode == 95 or weathercode == 99:
    weather = "Thunderstorm with slight and heavy hail"
elif weathercode == 80 or weathercode == 81 or weathercode == 82:
    weather = "Rain showers: Slight, moderate, and violent"
elif weathercode == 85 or weathercode == 86:
    weather = "Snow showers slight and heavy"
else:
    print("Error: Weathercode failed to receive information.")

max_temperature = user["daily"]["temperature_2m_max"][0]
#print max temp with a smiley
if -20 < max_temperature < 0:
    max_temp = f"😎: {max_temperature}"
if max_temperature < -20:
    max_temp = f"🥶: {max_temperature}"
if 23 > max_temperature > 0 :
    max_temp = f"🙃: {max_temperature}"
if 23 < max_temperature < 27 :
    max_temp = f"😎: {max_temperature}"
if  31 > max_temperature > 27 :
    max_temp = f"😅: {max_temperature}"
if  max_temperature > 31 :
    max_temp = f"🥵: {max_temperature}"
    
#print min temp with a smiley
min_temperature = user["daily"]["temperature_2m_min"][0]
if -20 < min_temperature < 0:
    min_temp = f"😎: {min_temperature}"
if min_temperature < -20:
    min_temp = f"🥶: {min_temperature}"
if 23 > min_temperature > 0 :
    min_temp = f"🙃: {min_temperature}"
if 23 < min_temperature < 27 :
    min_temp = f"😎: {min_temperature}"
if  31 > min_temperature > 27 :
    min_temp = f"😅: {min_temperature}"
if  min_temperature > 31 :
    min_temp = f"🥵: {min_temperature}"


    

print(weather)
print(f"Maximum temperature for today: {max_temp}    Minimum temperature for today: {min_temp}")
