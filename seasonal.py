import json
import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from config import *


LATLIST = []
LNGLIST = []

# atlantic boundaries:
# lon: -81, 39

# east pacific boundaries:
# lon: -152, -70

# west pacific boundaries:
# lon: 140, -152

def get_center(c):
    lngSum = 0
    latSum = 0

    for coor in c:
        lngSum += coor[0]
        latSum += coor[1]

    lng = lngSum/len(c)
    lat = latSum/len(c)

    return lng, lat

def parse_json(json_list):
    for season in json_list:
        with open(f'./data/{season}') as season:
            data = json.load(season)
            for data_point in data:
                entry = data_point['bbox']['coordinates'][0]
                lng, lat = get_center(entry)

                # if lng >= -81 and lng <= 39:
                LATLIST.append(np.floor(lat))
                LNGLIST.append(np.floor(lng))

def draw_map():
    cmblist = zip(LATLIST, LNGLIST)
    longitude_size = np.arange(-180, 180, SIZE_OF_GRID)
    latitude_size = np.arange(-90, 90, SIZE_OF_GRID)

    longitude_mesh, latitude_mesh = np.meshgrid(longitude_size, latitude_size)

    dens = np.zeros((int(180/SIZE_OF_GRID), int(360/SIZE_OF_GRID)))

    for lat, lon in cmblist:
        dens[int((lat+90)/SIZE_OF_GRID), int((lon+180)/SIZE_OF_GRID)] += 1

    ax = plt.axes(projection = ccrs.PlateCarree())
    plt.contourf(longitude_mesh, latitude_mesh, dens, 10, transform=ccrs.PlateCarree())

    ax.coastlines()
    plt.show()

if __name__ == "__main__":
    
    parse_json(ALL_MONTHS)
    draw_map()
