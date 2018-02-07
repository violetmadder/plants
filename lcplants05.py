import csv
import json
import pprint

pp = pprint.PrettyPrinter(depth=2);




def readcsv():
    with open('usdasearch02.txt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)
    return rows

def writejson():
    with open('plantsdict.json', 'w') as outfile:
        json.dump(plants, outfile, sort_keys=True, indent=4)

def readjson():
    with open ('plantsdict.json', 'r', encoding='utf8') as jsonfile:
        return (json.load(jsonfile))

def cleandict():
    filteredItems = []
    plantnum = 0
    for item in readcsv():
        plantnum = plantnum + 1
        filteredItem = {}    
        for k, v in item.items(): #cleaning off empty values
            if v:
                filteredItem[k] = v
        if filteredItem:
            filteredItems.append(filteredItem)
    print ("this csv has " + str(plantnum) + " plants")
    return filteredItems
#    {k: [item for item in v if item] for k, v in readcsv())

#def focusdict():
#    for item in cleandict():
#        if item['Category'] == 'Lichen': #ignoring lichens
#            continue
#        else:
#            focusdict.append(item)
#    return focusdict

def writekumu():
    elements = []
    for plant in cleandict():
        sciname = plant['Scientific Name']
        try:
            plant['Common Name']
            label = plant['Common Name']
        except:
            label =  sciname
        elements.append({
                'label': label,
                '_id': plant['Symbol'],
                'type' : 'species',
                'description': '',
                'tags': '',
                'genus': plant['Genus'], 
                'species': plant['Species'],
                'scientific name': sciname,
                #'common name': plant['Common Name'],
                'zone' : '',
                })
    kumu = {'elements': elements, 'connections': []}
    with open ('plantskumu.json', 'w') as outfile:
        json.dump(kumu, outfile, sort_keys=True, indent=4)
        
        
writekumu()
    
