import folium
import IPython
from IPython.display import display, HTML

map_center = [40.7128, -74.0060]
mymap = folium.Map(location=map_center, zoom_start=12)

folium.Marker(
    [40.7128, -74.0060],
    popup='New York City',
    icon=folium.Icon(icon='info-sign', color='blue')
).add_to(mymap)

# display(mymap)
mymap.save('map.html')