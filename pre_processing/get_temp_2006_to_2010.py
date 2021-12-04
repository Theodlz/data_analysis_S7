from bs4 import BeautifulSoup
import requests
import re
import js2xml
from itertools import repeat
from pprint import pprint as pp
import csv

import datetime as dt

def generate_temp_data():
    years = [2006,2007,2008,2009,2010]
    dates = []
    temps_max = []
    temps_min = []
    for year in years:
        temp_max = False
        temp_min = False
        date = False
        print('downloading data of {} ...'.format(year))
        
        soup = BeautifulSoup(requests.get("https://www.infoclimat.fr/climatologie/normales-records/{}-{}/paris-montsouris/details/07156.html".format(year,year)).content, "html.parser")
        script = soup.find("script", text=re.compile("Highcharts.Chart")).text
        parsed = js2xml.parse(script)
        for parsed2 in parsed.xpath("//property[@name='series']/array/object"):
            type = parsed2.xpath(".//property[@name='name']/string/text()")
            if type[0] in ['Température maximale moyenne','Température minimale moyenne']:
                for d in parsed2.xpath(".//property[@name='data']"):
                    if date == False:
                        date=True
                        timestamp = d.xpath(".//array/object/property[@name='x']/number/@value")
                        for indx, ts in enumerate(timestamp):
                            timestamp[indx] = dt.datetime.fromtimestamp(int(ts[:10])).date()
                        dates.extend(timestamp)
                    temperature = d.xpath(".//array/object/property[@name='y']/number/@value")
                    if type[0] == 'Température maximale moyenne' and temp_max==False:
                        temps_max.extend(temperature)
                        temp_max=True
                    if type[0] == 'Température minimale moyenne' and temp_min==False:
                        temps_min.extend(temperature)
                        temp_min=True




    with open("temperatures.csv".format(year), "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "min_t", "max_t"])
        writer.writerows(zip(dates,temps_min,temps_max))
    print('download complete ! \n')

generate_temp_data()