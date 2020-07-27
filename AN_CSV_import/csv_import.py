import csv
import numpy as np
filePath = '/home/hari/Downloads/airports.csv'

with open(filePath,'r') as csvFile:
    csvData = list(csv.reader(csvFile))
      
data = np.asarray(csvData).T
textIndex = max(min(13, textIndex), 0)
texts = data[textIndex].astype('U').tolist()
lat =  np.radians(data[6].astype('f'))
lon =  np.radians(data[7].astype('f'))

def latlonger(lat, lon, rad):
    # see: http://www.mathworks.de/help/toolbox/aeroblks/llatoecefposition.html
    alt = 0.01
    f = 0.00
    ls = np.arctan((1 - f)**2 * np.tan(lat))
    x = rad * np.cos(lat) * np.cos(lon) + alt * np.cos(lat) * np.cos(lon)
    y = rad * np.cos(lat) * np.sin(lon) + alt * np.cos(lat) * np.sin(lon)
    z = rad * np.sin(lat) + alt * np.sin(lat)
    
    locations = np.column_stack([x,y,z])
    
    return Vector3DList.fromNumpyArray(locations.ravel())

locations = latlonger(lat, lon, radius)