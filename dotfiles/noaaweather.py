#!/usr/bin/python
import urllib2,re
from optparse import OptionParser

# Define available options
# Planning to add options to output specific data via arguments
db = "ICAO Codes can be found at: http://www.mapping.com/airportcodes.html"
oparser = OptionParser(usage="%prog [-i] [-v]\n"+db, version="%prog 1.0")
oparser.add_option("-i", "--icao", dest="icao",
                   help = "ICAO code", metavar="ICAO")
oparser.add_option("-v", "--verbose",
                   action="store_true", dest="verbose")
(options, args) = oparser.parse_args()

# Verify if an icao was supplied with "-i" 
if options.icao == None:
    oparser.error("Please supply a valid ICAO code.")

def fetchData():
    # Fetch data from NOAA
    xmlData = urllib2.Request("http://www.weather.gov/data/current_obs/" + options.icao.upper() + ".xml")
    response = urllib2.urlopen(xmlData)
    xml = response.read()
    response.close()
    return xml

def parseData():
    # Match xml with re and create a dictionary
    match = re.compile('\t<(.+?)>(.+?)</').findall(fetchData())
    noaaDict = dict(match)    
    return noaaDict

# Get parsed data
parsedData = parseData()

# Print data as you wish
print "Temp                 " + parsedData["temp_f"] + " F"
if "windchill_f" in parsedData:
	print "${offset 10}Windchill           " + parsedData["windchill_f"] + " F"
else:
	print "${offset 10}Windchill           " + "Unavailable"
print "${offset 10}Humidity           " + parsedData["relative_humidity"] + "%"
print "${offset 10}Weather           " + parsedData["weather"]
print "${offset 10}Pressure          " + parsedData["pressure_in"] + " in"
print "${offset 10}Wind                  " + parsedData["wind_dir"], parsedData["wind_mph"] + " MPH"

"""
List of available keys

icon_url_name
privacy_policy_url
weather
ob_url
pressure_in
dewpoint_string
suggested_pickup_period
disclaimer_url
title
dewpoint_f
location
dewpoint_c
latitude
wind_mph
temp_f
station_id
pressure_string
link
temp_c
visibility_mi
wind_string
pressure_mb
wind_kt
temperature_string
two_day_history_url
wind_dir
wind_degrees
copyright_url
icon_url_base
url
observation_time
relative_humidity
longitude
credit_URL
suggested_pickup
credit
"""
