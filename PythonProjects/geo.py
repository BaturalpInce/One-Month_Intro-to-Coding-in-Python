from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="me")
location = geolocator.geocode("London Street")
print(location.address)

print((location.latitude, location.longitude))

lat = location.latitude