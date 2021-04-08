import csv
from django.conf import settings

list_station = []
with open(settings.BUS_STATION_CSV, mode='r') as f:
    reader = csv.reader(f)
    for idx, row in enumerate(reader):
        if idx > 0:
            list_station.append({'Name': row[1], 'Street': row[4], 'District': row[6]}) 