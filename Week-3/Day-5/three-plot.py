import matplotlib.pyplot as plt
import pytz
import datetime
import pyowm

# set up the OpenWeatherMap API
owm = pyowm.OWM('d75f7ab4cd952d8a2a4f55e8106158d4')

# set up the city and country codes
city = 'Tel Aviv'
country_code = 'IL'

# retrieve the weather observation data
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city + ',' + country_code)
weather = observation.weather

# retrieve the current humidity data
humidity = weather.humidity

# retrieve the current wind data
wind_speed = weather.wind()['speed']
wind_deg = weather.wind()['deg']

# retrieve the current temperature data
temp_dict = weather.temperature('celsius')
temp = temp_dict['temp']
feels_like = temp_dict['feels_like']
temp_min = temp_dict['temp_min']
temp_max = temp_dict['temp_max']

# set up the plot
def init_plot():
    plt.ylabel('Percentage')
    plt.title('Current Weather for ' + city)

# plot the humidity data in a bar chart
def plot_humidity():
    # create a list of the humidity value
    humidity_data = [humidity]

    # create a list of the x-axis labels
    labels = ['Humidity']

    # plot the data
    fig, ax = plt.subplots()
    ax.bar(labels, humidity_data, color='blue')

    # call the function to write the humidity on the bar chart
    write_humidity_on_bar_chart(ax, humidity_data[0])

    # style the plot
    ax.set_ylim(0, 100)

# write the humidity value on the bar chart
def write_humidity_on_bar_chart(ax, humidity_value):
    ax.text(0, humidity_value+5, str(humidity_value)+'%')

# plot the wind speed and direction in a bar chart
def plot_wind():
    # create a list of the wind speed and direction values
    wind_data = [wind_speed, wind_deg]

    # create a list of the x-axis labels
    labels = ['Wind Speed', 'Wind Direction']

    # plot the data
    fig, ax = plt.subplots()
    ax.bar(labels, wind_data, color='green')

    # call the function to write the wind speed and direction on the bar chart
    write_wind_on_bar_chart(ax, wind_data)

    # style the plot
    ax.set_ylim(0, max(wind_data)*1.2)

# write the wind speed and direction on the bar chart
def write_wind_on_bar_chart(ax, wind_data):
    ax.text(0, wind_data[0]+0.5, str(wind_data[0])+' m/s')
    ax.text(1, wind_data[1]+5, str(wind_data[1])+' degrees')

# plot the temperature data in a bar chart
def plot_temperature():
    # create a list of the temperature values
    temp_data = [temp, feels_like, temp_min, temp_max]

    # create a list of the x-axis labels
    labels = ['Temperature', 'Feels Like', 'Min', 'Max']

    # plot the data
    fig, ax = plt.subplots()
    ax.bar(labels, temp_data, color='red')

    # call the function to write the temperature on the bar chart
    write_temperature_on_bar_chart(ax, temp_data)

    # style the plot
    ax.set_ylim(min(temp_data)*0.9, max(temp_data)*1.1)

# write the temperature values on the bar chart
def write_temperature_on_bar_chart(ax, temp_data):
    ax.text(0, temp_data[0]+0.5, str(temp_data[0])+'°C')
    ax.text(1, temp_data[1]+0.5, str(temp_data[1])+'°C')
    ax.text(2, temp_data[2]+0.5, str(temp_data[2])+'°C')
    ax.text(3, temp_data[3]+0.5, str(temp_data[3])+'°C')

#plot all the weather data in subplots
def plot_all():
    init_plot()
plt.subplot(2, 2, 1)
plot_humidity()

plt.subplot(2, 2, 2)
plot_wind()

plt.subplot(2, 2, 3)
plot_temperature()

plt.subplots_adjust(hspace=0.5)

plt.show()

# run the program
plot_all()