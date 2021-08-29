from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'enter_your_api_key'

darksky = DarkSky(API_KEY)

latitude = 41 # type - number for South and + for North
longitude = 29   # type - number for West, + number for East
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto` 
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print(forecast.currently.temperature)
print(forecast.currently.humidity)
print(forecast.currently.summary)
print(forecast.daily.summary)



forecast.latitude # 42.3601
forecast.longitude # -71.0589
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. Can be finded at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be finded at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be finded at darksky/forecast.py
forecast.daily # DailyForecast. Can be finded at darksky/forecast.py
forecast.alerts # [Alert]. Can be finded at darksky/forecast.py



from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	title = "Homepage"
	weather_temperature = forecast.currently.temperature
	weather_humidity = forecast.currently.humidity
	weather_summary = forecast.currently.summary
	weather_summary_daily = forecast.daily.summary
	return render_template("index.html", title=title, weather_temperature=weather_temperature, weather_humidity=weather_humidity, weather_summary=weather_summary, weather_summary_daily=weather_summary_daily)

@app.route("/about.html")
def about():
	title = "About"
	return render_template("about.html", title=title)

@app.route("/contacts.html")
def contacts():
	title = "Contacts"
	return render_template("contacts.html", title=title)

# if can't activate debug mode use the lines on the comment
# if __name__=="_main_":
    #app.run(debug=True)
