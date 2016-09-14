import sys
import json
import csv
import pandas as pd
import getMtaData as gmd

mtakey = sys.argv[1]
busline = sys.argv[2]
output = sys.argv[3]

download = False

# download and read the data

if(download):
  gmd.getMtaData(busline, mtakey, 'bus.json')

with open('bus.json') as data_file:    
  data = json.load(data_file)

busses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

busses_clean = []
for i in range(len(busses)):
  lat = busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
  lon = busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
  stop = busses[i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
  status = busses[i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
    
  bus_new = [lat,lon,stop,status]
  busses_clean.append(bus_new)
 
with open(output, 'wb') as f:   
  writer = csv.writer(f)
  writer.writerows(busses_clean)


