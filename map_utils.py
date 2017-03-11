import argparse
import json
import urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("-o","--origin", required = True, help="Your coordinates")
ap.add_argument("-d","--destination", required = True, help="Point of interest")
# example:  --origin "59.931882,30.361689" --destination "59.933607,30.362837"
args = vars(ap.parse_args())

origin = args["origin"]
destination = args["destination"]

# origin = "59.931882,30.361689"
# destination = "59.933607,30.362837"
link = "http://maps.google.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&mode=walking&sensor=false"
response = urllib.request.urlopen(link)
strind_json = response.read().decode('utf-8')
data = json.loads(strind_json)
for item, value in data['routes'][0]['legs'][0]['distance'].items():
    if item == 'text' : print("Distance between two points is {}".format(value))
