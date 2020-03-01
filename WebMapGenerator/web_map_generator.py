import folium
import pandas

# Retrieve coordinates from file
data = pandas.read_csv("C:/Users/darkphantom7/Desktop/Laulex/WebMapGenerator/map_data/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# Function to return a color based on elevation values
def color_producer(elevation):
  if elevation < 2000:
    return 'green'
  elif 2000 <= elevation < 3000:
    return 'orange'
  else:
    return 'red'

# html multi line string to use as the text for the popups of the map icons
html = """
Volcano name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Create Map to work with
map = folium.Map(location=[38.58,-110], zoom_start=6, tiles="Stamen Terrain")

# Create Folium FeatureGroup to add Volcano Markers to
fgv = folium.FeatureGroup(name="Volcano Markers")

# Iterate through coordinates from file and add "Points Layer" to FeatureGroup
for lt,ln,el,nm in zip(lat, lon, elev, name):
  pop = folium.Popup(html=html % (nm,nm,el))
  fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=pop, fill_color=color_producer(el), color='grey', fill_opacity=.7))

# Create Folium FeatureGroup to add Volcano Markers to
fgp = folium.FeatureGroup(name="Country Info")

# Add "GeoJson Layer" to Feature Group for Population
# 2 Parameters in this add_child
fgp.add_child(folium.GeoJson(
data=open('map_data/world.json', 'r', encoding='utf-8-sig').read(),
style_function=
lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
else 'red'}
))

# Add LayerControl + FeatureGroup to Map and save Map to file
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map_html_popup_google.html")