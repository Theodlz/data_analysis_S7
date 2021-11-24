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
    for year in years:
        print('downloading data of {} ...'.format(year))
        date = []
        temp_max = []
        temp_min = []
        soup = BeautifulSoup(requests.get("https://www.infoclimat.fr/climatologie/normales-records/{}-{}/paris-montsouris/details/07156.html".format(year,year)).content, "html.parser")
        script = soup.find("script", text=re.compile("Highcharts.Chart")).text
        parsed = js2xml.parse(script)
        for parsed2 in parsed.xpath("//property[@name='series']/array/object"):
            type = parsed2.xpath(".//property[@name='name']/string/text()")
            if type[0] in ['Température maximale moyenne','Température minimale moyenne']:
                for d in parsed2.xpath(".//property[@name='data']"):
                    if len(date) == 0:
                        timestamp = d.xpath(".//array/object/property[@name='x']/number/@value")
                        for indx, ts in enumerate(timestamp):
                            timestamp[indx] = dt.datetime.fromtimestamp(int(ts[:10])).date()
                        date = timestamp
                    temperature = d.xpath(".//array/object/property[@name='y']/number/@value")
                    if type[0] == 'Température maximale moyenne' and len(temp_max)==0:
                        temp_max = temperature
                    if type[0] == 'Température minimale moyenne' and len(temp_min)==0:
                        temp_min = temperature




        with open("temperatures_{}.csv".format(year), "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "min_t", "max_t"])
            writer.writerows(zip(date,temp_min,temp_max))
        print('download complete ! \n')

generate_temp_data()
