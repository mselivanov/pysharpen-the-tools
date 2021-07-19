import urllib.request as req
from http.client import HTTPResponse
import json

from helpers.helpers import print_header


def http_examples():
    print_header('HTTP examples')
    web_url = req.urlopen('https://google.com')
    print(f'Response code: {web_url.getcode()}')
    print(f'Response data: {web_url.read()}')


def print_results(data):
    earth_quakes = json.loads(data)
    if 'title' in earth_quakes['metadata']:
        print(f'Title: {earth_quakes["metadata"]["title"]}')    
    
    if 'count' in earth_quakes['metadata']:
        print(f'Earthquakes within last day: {earth_quakes["metadata"]["count"]}')    
    
    for idx, eq in enumerate(earth_quakes['features']):
        magnitude = eq["properties"]["mag"]
        felt = eq["properties"]["felt"]
        if magnitude > 4.0:
            print(f'Earthquake {idx} with magnitude {magnitude} happened in {eq["properties"]["place"]} felt by {felt}')

def json_examples():
    print_header('JSON examples')
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    resp = req.urlopen(url) 
    if resp.getcode() == 200:
        data = resp.read() 
        print_results(data)
    else:
        print(f'Something went wrong. Status code: {resp.getcode()}')


def main():
    http_examples()
    json_examples()


if __name__ == '__main__':
    main()