import urllib.request,urllib.parse
import json

serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address=input("Enter the location")
    url=serviceurl+urllib.parse.urlencode({'address':address})

    print('Retreiving',url)

    uh=urllib.request.urlopen(url)
    data=uh.read().decode()
    print("Retrieved",len(data),'Data')

    try:
        js=json.loads(data)
    except:
        js=None

    if not js or 'status' not in js or js['status']!='OK':
        print("===Failure in retreiving Data===")
        print(data)
        continue
    
    print(json.dumps(js,indent=4))

    lat=js['results'][0]['geometry']['location']['lat']
    long = js['results'][0]['geometry']['location']['lng']

    print("Latitude :",lat)
    print("Longitude :",long)

    location=js['resutl'][0]['formatted address']

    print("Location :",location)
