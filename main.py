import openmeteo

def Main():
    weather_item = openmeteo.OpenMeteoAPI({
	"latitude": 46.877186,
	"longitude": -96.789803,
	"hourly": ["temperature_2m", "apparent_temperature", "precipitation_probability", "precipitation", "snow_depth", "weather_code", "cloud_cover", "visibility", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "daylight_duration", "precipitation_sum", "precipitation_hours", "precipitation_probability_max", "wind_direction_10m_dominant"],
	"temperature_unit": "fahrenheit",
	"wind_speed_unit": "mph",
	"precipitation_unit": "inch",
	"forecast_days": 14
})
    weather_item.get_weather_data()




if __name__=="__main__":
    Main()