import folium

# Generate a map of Canada centered at its geographic center
nepal_map = folium.Map(
    location=[56.130, -106.35],
    zoom_start=4
)

# Create a feature group for Ontario
ontario = folium.map.FeatureGroup()

# Add a red circle marker to the Ontario feature group
ontario.add_child(
    folium.features.CircleMarker(
        location=[51.25, -85.32],
        radius=5,
        color='red',
        fill_color='red'
    )
)

# Add the feature group to the map
nepal_map.add_child(ontario)

# Add a labeled marker for Ontario
folium.Marker(
    location=[51.25, -85.32],
    popup='Ontario'
).add_to(nepal_map)

# Display the map (in Jupyter) or save it (in script)
# For Jupyter:
nepal_map

# For script:
# canada_map.save("canada_map.html")
