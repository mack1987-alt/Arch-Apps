from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example@email.com")

zip_data = input("Enter zipcode: ")
zipcode = zip_data

location = geolocator.geocode(zipcode)

print("Zipcode: ", zipcode)
print("Details of the zipcode: ")
print(location)