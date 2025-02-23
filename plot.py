from scrape import CityData
import pandas as pd

import plotly.express as px


def plot(city: CityData):
    # TODO make method of CityData to return house_data
    df = pd.DataFrame(data=city.get_house_data())
    fig = px.scatter_map(df, lat='lat', lon='lon', color='price', color_continuous_scale=px.colors.cyclical.IceFire,
                         size_max=15, zoom=10)
    fig.show()
    pass


# Example
"""import plotly.express as px
df = px.data.carshare()
fig = px.scatter_map(df, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
fig.show()
pass"""
