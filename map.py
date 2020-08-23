import folium
import pandas
map = folium.Map([40,-100], zoom_start=7, titles="Stamen Terrain")


data=pandas.read_csv("App#2/Volcanoes.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
elev=list(data["ELEV"])
fgv=folium.FeatureGroup(name="Rare Pokemon Locations") #Pokemon location object

def color_producer(elevation):
    if elevation <1000:
        return "green"
    elif 1000<=elevation <3000:
        return "orange"
    else:
        return "red"         

for lt, ln, el in zip( lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup="Shinny Pokemon #" + str(el)+ " is here !!!",fill_color=color_producer(el), color="black", fill_opacity=0.5))
    #fg.add_child(folium.Marker(location=[lt, ln], popup="Shinny Pokemon #" + str(el)+ " is here !!!", icon=folium.Icon(color=color_producer(el))))
    #map.add_child(folium.Marker(location=[40, -99], popup="Hi I'm Marker", icon=folium.Icon(color='purple')))

fgp=folium.FeatureGroup(name="Hunman Population") #Human Population object 


fgp.add_child(folium.GeoJson(data=open("App#2/world.json", 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {"fillColor" : 'green' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red' }))


lc=(folium.LayerControl())
map.add_child(fgv)
map.add_child(fgp)
map.add_child(lc)

map.save("App#2/Map1.html")

