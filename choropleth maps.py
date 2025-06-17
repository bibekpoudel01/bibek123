import folium
import pandas as pd

# Load data (e.g., population by country)
data = pd.DataFrame({
    'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan'],
    'Code': ['CHN', 'IND', 'USA', 'IDN', 'PAK'],
    'Population': [1444216107, 1393409038, 331893745, 276361783, 225199937]
})

# Load GeoJSON data for countries
world_geo = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'

# Create map centered roughly around Asia
m = folium.Map(location=[20, 0], zoom_start=2)

# Add Choropleth layer
folium.Choropleth(
    geo_data=world_geo,
    data=data,
    columns=['Code', 'Population'],
    key_on='feature.id', 
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population'
).add_to(m)


m


