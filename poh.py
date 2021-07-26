import json

from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen

url = "https://api.poh.dev/profiles?order_by=registered_time&order_direction=desc&include_unregistered=false"

response = urlopen(url)


data_json = json.loads(response.read())

def get_key(mykey):
    for key, value in data_json.items():
         if mykey == key:
             return value


# list out keys and values separately
key_list = list(data_json.keys())
val_list = list(data_json.values())
nested_list = val_list[0]

profiles = []
for x in val_list[0]:
    profiles.append(x.values())

count = 0 

for dic in profiles:
    for key in list(dic):
        if str(key).startswith("0x"):
            
            count +=1

            print(key)
            print(count)

        
        


    



# Opening a file
file1 = open('myfile.txt', 'w')










 



