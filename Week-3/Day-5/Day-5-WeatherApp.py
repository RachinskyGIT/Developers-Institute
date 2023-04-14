
import pyowm
import json

# Введите свой API-ключ от OpenWeatherMap
owm = pyowm.OWM('d75f7ab4cd952d8a2a4f55e8106158d4')
# owm = pyowm.OWM('15ef23cb19e2ec7b7a0178455980af86')


# # Проверяем работоспособность ключа
# try:
#     owm.weather_at_place('London,uk')
#     print("API-ключ работает!")
# except pyowm.exceptions.api_response_error.UnauthorizedError:
#     print("API-ключ недействительный! Пожалуйста, проверьте ваш API-ключ и попробуйте снова.")


print(owm)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Tel Aviv')
weather = observation.weather


################## Делает так, чтобы команда humidity = observation.w.humidity() Брала информацию не из сервера, а из этого словаря: w={...} #####################
################## Это нужно, чтобы проверить работоспособность newplot.py, без ожидания миллион лет каждый раз, пока сервер откликнется ##################
# Convert weather data to a dictionary
weather_dict = weather.to_dict()

# Convert dictionary to JSON format
weather_json = json.dumps(weather_dict)
##################################################################################################################################################################


print(weather_json)
print("Current weather in Tel Aviv: ", weather.status)
wind = observation.weather.wind()
print("Wind speed: ", wind['speed'], ", Wind degree: ", wind['deg'])


# Get the sunrise and sunset times
sunrise_time = observation.weather.sunrise_time('iso')
sunset_time = observation.weather.sunset_time('iso')
print("Sunrise time: ", sunrise_time, ", Sunset time: ", sunset_time)


