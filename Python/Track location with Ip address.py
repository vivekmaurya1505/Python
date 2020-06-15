"""
import requests
import folium
import webbrowser as web

res = requests.get("https://ipinfo.io/")
data = res.json()
print(data)
location = data['loc'].split(",")


lat = float(location[0])
log = float(location[1])
print(lat,log)

fg = folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data = (open("IndianStates.json","r",encoding = "utf-8-sig").read())))
fg.add_child(folium.Marker(location = [lat,log],popup = "this is my location"))

map = folium.Map(location = [lat,log],zoom_start = 7)

map.add_child(fg)
map.save("1.html")

"""

import requests
import webbrowser as web

res = requests.get("https://ipinfo.io/")
data = res.json()
location = data['loc'].split(",")
web.open("https://www.google.com/maps/place/"+location[0]+","+location[1])
