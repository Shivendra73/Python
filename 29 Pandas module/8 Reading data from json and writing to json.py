#pandas reading a json file

#json ---->JAVA SCRIPT OBJECT NOTATION---->k,v pairs

#from a list(dictionaries) create a json file
#that json file convert to DF
#again from that DF create a json file
#list(dictionaries)----->JSON file----->DF------>JSON file

#Create a list of dictionaries
cars = [
    {"Name":"swift", "Price": 1000000, "Model":2005, "Power": 1300},
    {"Name":"Toyota", "Price": 1200000, "Model":2010, "Power": 1600},
    {"Name":"Audi", "Price": 2500000, "Model":2017, "Power": 1800},
    {"Name":"Ford", "Price": 2800000, "Model":2009, "Power": 1200},
         
]

#writing data to a json
import json

with open('cars.json', 'w') as f:
    json.dump(cars, f)

#Creating a pandas dataframe by reading a jsonfile
import pandas as pd
cars_df = pd.read_json('cars.json')
print(cars_df)


#Writing into a json file
cars_df.to_json("carsdata_df.json")


