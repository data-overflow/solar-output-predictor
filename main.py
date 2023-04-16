from flask import Flask, make_response, jsonify
from geopy.geocoders import Nominatim
import pandas as pd
import pvlib
from pvlib.location import Location
import datetime
from suntime import Sun, SunTimeException
from config import Config

SERVER_LOCATION = "http://127.0.0.1:5000"

app = Flask(__name__)
app.config.from_object(Config)


def efficiency(latitude, longitude, time_zone, altitude, place_name, start_date, end_date, panel_rating):
    surface_tilt = 20
    surface_azimuth = 180
    tus = Location(latitude, longitude, time_zone, altitude, place_name)
    times = pd.date_range(start=start_date, end=end_date, freq='H', tz=tus.tz)
    cs = tus.get_clearsky(times)
    solar_position = pvlib.solarposition.get_solarposition(
        times, latitude, longitude
    )
    dni_extra = pvlib.irradiance.get_extra_radiation(times)
    airmass = pvlib.atmosphere.get_relative_airmass(
        solar_position['zenith'], model='kastenyoung1989'
    )
    total_irradiance = pvlib.irradiance.get_total_irradiance(
        surface_tilt, surface_azimuth,
        solar_position['apparent_zenith'],
        solar_position['azimuth'],
        cs["dni"], cs["ghi"], cs["dhi"],
        dni_extra, airmass=airmass
    )
    eff = (panel_rating / 1000) * (total_irradiance['poa_global'].max() / 1000)
    return eff


def get_units(place, country, start_date_str, end_date_str, rating, no_panels, tz='UTC'):
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    geolocator = Nominatim(user_agent="suntime_app")
    location = geolocator.geocode(place + ', ' + country)
    latitude = location.latitude
    longitude = location.longitude
    sun = Sun(latitude, longitude)
    total_daylight_hours = 0
    while start_date <= end_date:
        try:
            sunrise = sun.get_local_sunrise_time(start_date)
            sunset = sun.get_local_sunset_time(start_date)
            daylight_hours = (sunset - sunrise).seconds / 3600
            total_daylight_hours += daylight_hours
        except SunTimeException:
            pass
        start_date += datetime.timedelta(days=1)
    e = efficiency(
        latitude, longitude, tz, altitude=0, place_name=place,
        start_date=start_date_str, end_date=end_date_str, panel_rating=rating
    )
    total_units = total_daylight_hours * e * no_panels * rating
    return latitude, longitude, total_units/1000


@app.route("/api/<place>/<country>/<start>/<end>/<num>/<pr>")
def index(place: str, country: str, start: str, end: str, num: int, pr: int):
    lat, lon, units = get_units(place, country, start, end, int(pr), int(num))
    d0 = datetime.date(*start.split('-'))
    d1 = datetime.date(*end.split('-'))
    delta = d1 - d0
    print(delta.days)
    return make_response(jsonify({
        "lat": lat,
        "lon": lon,
        "days": delta.days,
        "output": units
    }), 200)


if __name__ == "__main__":
    app.run(debug=True)
