# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:34:17 2019

@author: Erdogan
"""

from API.get_google_maps import get_google_maps
import geopy
from geopy.geocoders import Nominatim
nom=Nominatim()

filepath='C:/temp/STATION/ns_stations.csv'
df = pd.read_csv(filepath)

df=df.loc[df['Land']=='Netherlands',:]
df[['Lat', 'Lon']]

out=np.zeros([df.shape[0], AFRITTEN.shape[0]])
from geopy import distance
for i in range(0,df.shape[0]):
    getStation=df[['Lat', 'Lon']].iloc[i,:].values
    for k in range(0,AFRITTEN.shape[0]):
        getAfrit=df[['Lat', 'Lon']].iloc[i,:].values
        out[i,k]= distance.distance(getStation, getAfrit).km

#[adress, coord]=nom.geocode('station den dolder, Netherlands')
