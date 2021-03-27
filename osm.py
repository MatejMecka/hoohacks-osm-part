from fastapi import FastAPI
import json

import overpy
api = overpy.Overpass()
app = FastAPI()

types = [
  "recycling:aerosol_cans",
  "recycling:animal_waste",
  "recycling:aluminium",
  "recycling:bags",
  "recycling:batteries",
  "recycling:belts",
  "recycling:beverage_cartons",
  "recycling:bicycles",
  "recycling:books",
  "recycling:cans",
  "recycling:car_batteries",
  "recycling:cardboard",
  "recycling:cartons",
  "recycling:cds",
  "recycling:chipboard",
  "recycling:christmas_trees",
  "recycling:clothes",
  "recycling:coffee_capsules",
  "recycling:computers",
  "recycling:cooking_oil",
  "recycling:cork",
  "recycling:drugs",
  "recycling:electrical_items",
  "recycling:engine_oil",
  "recycling:fluorescent_tubes",
  "recycling:foil",
  "recycling:food",
  "recycling:food_waste",
  "recycling:furniture",
  "recycling:gas_bottles",
  "recycling:glass",
  "recycling:glass_bottles",
  "recycling:green_waste",
  "recycling:garden_waste",
  "recycling:hazardous_waste",
  "recycling:hardcore",
  "recycling:low_energy_bulbs",
  "recycling:magazines",
  "recycling:metal",
  "recycling:mobile_phones",
  "recycling:newspaper",
  "recycling:organic",
  "recycling:paint",
  "recycling:pallets",
  "recycling:paper",
  "recycling:paper_packaging",
  "recycling:pens",
  "recycling:PET",
  "recycling:plasterboard",
  "recycling:plastic",
  "recycling:plastic_bags",
  "recycling:plastic_bottles",
  "recycling:plastic_packaging",
  "recycling:plastic_bottle_tops",
  "recycling:PMD",
  "recycling:polyester",
  "recycling:polystyrene_foam",
  "recycling:printer_cartridges",
  "recycling:printer_toner_cartridges",
  "recycling:printer_inkjet_cartridges",
  "recycling:rubble",
  "recycling:scrap_metal",
  "recycling:sheet_metal",
  "recycling:shoes",
  "recycling:small_appliances",
  "recycling:small_electrical_appliances",
  "recycling:styrofoam",
  "recycling:tyres",
  "recycling:tv_monitor",
  "recycling:waste",
  "recycling:white_goods",
  "recycling:wood"
]

@app.get("/")
async def get_locations(latitude: str = "0", longitude: str = "0", other_latitude: str = "0", other_longitude: str = "0"):
    result = api.query(f'[out:json];node["amenity"="recycling"]({latitude}, {longitude}, {other_latitude}, {other_longitude});out body;')

    data = []
    for node in result.nodes:
        print(node.tags)
        info = {
            "latitude": node.lat,
            "longitude": node.lon,
            "recycling": []
        }


        for elem in types:
            if node.tags.get(elem) != None:
                if node.tags.get(elem) == "yes":
                    info["recycling"].append(elem.split(':')[1])

        data.append(info)
        print(node)
    
    return data
