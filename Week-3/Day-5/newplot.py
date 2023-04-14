import matplotlib.pyplot as plt
import pytz
import datetime
import pyowm

# # initialize PyOWM object
# owm = pyowm.OWM('d75f7ab4cd952d8a2a4f55e8106158d4')


# # specify the city for which to retrieve the current weather data
city = 'Tel Aviv'

# # retrieve the current weather data for the specified city
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(city)
# w = observation.weather
w={"reference_time": 1681506864, "sunset_time": 1681574948, "sunrise_time": 1681528340, "clouds": 0, "rain": {}, "snow": {}, 
   "wind": {"speed": 1.54, "deg": 0}, "humidity": 72, "pressure": {"press": 1017, "sea_level": None}, 
   "temperature": {"temp": 289.37, "temp_kf": None, "temp_max": 289.92, "temp_min": 287.75, "feels_like": 288.93}, "status": "Clear", 
   "detailed_status": "clear sky", "weather_code": 800, "weather_icon_name": "01n", "visibility_distance": 10000, "dewpoint": None, 
   "humidex": None, "heat_index": None, "utc_offset": 10800, "uvi": None, "precipitation_probability": None}


# # retrieve the current humidity data
# humidity = observation.w.humidity()
humidity = w["humidity"]


# set up the plot
def init_plot():
    plt.ylabel('% Humidity')
    plt.title('Current Humidity for ' + city)

# plot the humidity data in a bar chart
def plot_humidity():
    # create a list of the humidity value
    humidity_data = [humidity]

    # create a list of the x-axis labels
    labels = ['']

    # plot the data
    fig, ax = plt.subplots()
    ax.bar(labels, humidity_data, color='blue')

    # call the function to write the humidity on the bar chart
    write_humidity_on_bar_chart(ax, humidity_data[0])

    # style the plot
    ax.set_ylim(0, 100)

    # add the title to the plot
    init_plot()

    plt.show()

# write the humidity value on the bar chart
def write_humidity_on_bar_chart(ax, humidity_value):
    ax.text(0, humidity_value+5, str(humidity_value)+'%')

# plot the humidity data
plot_humidity()