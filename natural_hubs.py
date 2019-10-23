from tqdm import tqdm, tqdm_gui
import os
import streamlit as st
import geopandas as gpd
import pandas as pd
import numpy as np
from geopy import distance

shape = gpd.read_file('afritten/divergenties.dbf')
shape = shape.to_crs(epsg=4326)

shape['lon'] = shape['geometry'].apply(lambda p: p.x)
shape['lat'] = shape['geometry'].apply(lambda p: p.y)


filepath = 'ns_stations/ns_stations.csv'
stations = pd.read_csv(filepath)

stations = stations.loc[stations['Land'] == 'Netherlands', :]
# stations[['Lat', 'Lon']]

# station = st.sidebar.selectbox('Selecteer Station',
                               # stations['Station'].unique())

station_selected = stations
# station_selected = stations.loc[stations['Station'] == station]
station_selected['lat'] = station_selected['Lat']
station_selected['lon'] = station_selected['Lon']
del station_selected['Lon']
del station_selected['Lat']

snelwegen = shape
del snelwegen['geometry']

in_distance = snelwegen[['lat','lon']]
#a2 = shape.loc[shape['WEGNUMMER'] == '002']
#del a2['geometry']


snelwegen.to_csv('snelwegen.csv')
# my_bar = st.progress(0)

# def get_station_dist(wegen, stations):
#     out = np.zeros([stations.shape[0], wegen.shape[0]])
#     for i in range(0, stations.shape[0]):
#         # my_bar.progress((i/stations.shape[0]) * 100)
#         getStation = stations[['lat', 'lon']].iloc[i, :].values
#         for k in range(0, wegen.shape[0]):
#             getAfrit = wegen[['lat', 'lon']].iloc[k, :].values
#             out[i, k] = distance.distance(getStation, getAfrit).km
#     dist_mat = pd.DataFrame(data=out)
#     dist_mat.write_csv('dist_mat.csv')
#
#
# if not os.path.isfile('dist_mat.csv'):
#     dist_mat = get_station_dist(snelwegen, stations)
# else:
#     pd.read_csv('dist_mat.csv')


st.title('Locatie stations en Afritten van rijkswegen')

radius = st.slider('Straal vanaf station', min_value=50, max_value=10000)
st.deck_gl_chart(
    viewport={
        'latitude': station_selected['lat'].tolist()[0],
        'longitude': station_selected['lon'].tolist()[0],
        'zoom': 12,
        'pitch': 50,
    },
    layers=[
        {
            'id': 'radius1',
            'data': station_selected,
            'type': 'ScatterPlotLayer',
            'getRadius': radius,
            'getColor': [230, 230, 30, 127],
        },
        {
            'id': 'divergents',
            'data': snelwegen,
            'type': 'ScatterPlotLayer',
            'getRadius': 50,
            'getColor': [75, 205, 250, 230]
        },
    ])

st.markdown('''
## Natural Hubs
Dit dashboard toont de afritten van alle rijkswegen in Nederland en de afstand
tot treinstations. De Radius is configureerbaar en laat zien welke afritten zich binnen deze straal bevinden.
''')