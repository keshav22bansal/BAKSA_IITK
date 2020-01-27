import requests 
  
# api-endpoint 
URL = "https://www.google.com/inputtools/request?text=mai&ime=transliteration_en_hi&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi&uv"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 
print(data[1][0][1][0])
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
# latitude = data['results'][0]['geometry']['location']['lat'] 
# longitude = data['results'][0]['geometry']['location']['lng'] 
# formatted_address = data['results'][0]['formatted_address'] 
  
# # printing the output 
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#       %(latitude, longitude,formatted_address)) 