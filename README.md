# pySmartWeatherIO

> This project has been Archived and is no longer maintained. It has been replaced by [`pyweatherflowrest`](https://github.com/briis/pyweatherflowrest) which will be the new wrapper for the WeatherFlow Rest API.

Wrapper for the WeatherFlow Smart Weather REST API. Designed to work with Home Assistant.

This module communicates with a Smart Home Weather station from the company [WeatherFlow](http://weatherflow.com/smart-home-weather-stations/) using their REST API. It retrieves current weather data from the attached units. Currently they have three types of Units:

* **AIR** - This unit measures Temperature, Humidity, Pressure and Lightning Strikes
* **SKY** - This unit measures Precipitation, Wind, Illuminance and UV
They are both attached to a central hub, that broadcasts the data via UDP and sends the data to a cloud database managed by WeatherFlow. This module retrieves the data back from the cloud database.
* **TEMPEST** - This is a combination of the features from the AIR and SKY units, in to one single device.

## Functions

The module exposes the following functions:

### SmartWeather(token, station_id, to_units, to_wind_units)

this will return a handle to the SmartWeather class and open the connection.

**token**
(string)(Required) The WeatherFlow REST API requires a Token. If you own a WeatherFlow station you can [login with your account](https://tempestwx.com/settings/tokens) and create the token. Previously there was a common token people could use, but this has been removed now - it might still work for a while, but I don't know for how long.

**station_id**
(string)(required) If you have your own Smart Weather Station, then you know your Station ID. If you don't have one, there are a lot of public stations available, and you can find one near you on [this link](https://smartweather.weatherflow.com/map). If you click on one of the stations on the map, you will see that the URL changes, locate the number right after */map/* - this is the Station ID

**to_units**
(string)(optional) The unit system to use. metric or imperial
Default value: metric

**to_wind_units**
(string)(optional) The wind unit system to use. mps (Meter pr second) or kmh (kilometer pr hour). Will be ignored if *to_units* is imperial
Default value: mps

### get_station_hardware()

Returns a JSON array with information about the Station Hardware.

* **station_name** The name of the Station as set by the Owner
* **serial_number** The serial number of the HUB Device
* **device_id** A unique device ID of the HUB Device
* **firmware_revision** The current firmware revision of the HUB Device

### get_station_data()

Returns a Data Class with current sensor values of the associated AIR and SKY or TEMPEST modules.

* **air_density** - Current Air Density
* **air_temperature** - Current temperature
* **brightness** - Shows the brightness in Lux
* **dew_point** - Dewpoint. The atmospheric temperature (varying according to pressure and humidity) below which water
* **feels_like** - How the temperature Feels Like. A combination of Heat Index and Wind Chill
* **freezing** - Is True when *air_temperature* is below zero, else False
* **heat_index** - A temperature measurement combining Humidity and temperature. How hot does it feel. Only used when temperature is above 26.67°C (80°F)
* **lightning** - Is True when *lightning_strike_count* is above zero, else False
* **lightning_strike_last_time** - The time when the last lightning strike occured.
* **lightning_strike_last_distance** - The distance away of the last lightning strike.
* **lightning_strike_count** - Shows the numbers of lightning strikes for last minute.
* **lightning_strike_count_last_3hr** - Shows the numbers of lightning strikes for last 3 hours.
* **precip_accum_last_1hr** - Precipitation in the last hour
* **precip_accum_local_day** - Precipitation since midnight
* **precip_accum_local_yesterday** - Precipitation yesterday
* **precip_rate** - The current precipitation rate - 0 if it is not raining
* **precip_minutes_local_day** - Number of minutes it has been raining for the current day
* **precip_minutes_local_yesterday** - Number of minutes it has been raining yesterday
* **raining** - Is True when *precip_rate* is above zero, else False
* **relative_humidity** - Current humidity in %
* **solar_radiation** - The current Solar Radiation measured in W/m2
* **station_pressure** - Current barometric pressure, taking in to account the position of the station
* **sea_level_pressure** - Current barometric pressure, at Sea Level
* **station_name** - Name of the station as supplied by the owner
* **timestamp** - The time of the last update
* **uv** - The UV index
* **wind_avg** - Current Average Wind Speed
* **wind_bearing** - Wind bearing in degrees (Example: 287°)
* **wind_chill** - How cold does it feel. Only used if temperature is below 10°C (50°F)
droplets begin to condense and dew can form
* **wind_direction** - Wind bearing as directional text (Example: NNW)
* **wind_gust** - Highest Wind Speed in the last minute
