import csv
import json
import pprint as pp
from collections import defaultdict

#taxonlist = ['Kingdom', 'Subkingdom', 'Superdivision', 'Division', 'Subdivision', 'Class', 'Subclass', 'Order', 'Family', 'Genus', 'Species', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma']




def tree(): # trying out this magical defaultdict trick
    return defaultdict(tree)

def taxons():
    taxondefdict = tree()
    for plant in cleandict():
        if plant.get('Kingdom') is None: # I need a cleaner way to handle these
            continue
        else:
            kingdom = plant['Kingdom']
        order = plant['Order']
        pclass = plant['Class']
        family = plant['Family']
        genus = plant['Genus']
        if plant.get('Species') is None:
            continue
        else:
            species = plant['Species']

        category = plant['Category']

        taxondefdict[kingdom][order][pclass][family][genus] = species

    return taxondefdict

def dicts(t): return {k: dicts(t[k]) for k in t}
# theoretically this converts the magical defaultdict back into a proper dict
#pp.pprint(dicts(taxons()))


def readcsv():
    with open('USDAsearch.txt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    return reader


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
    # the above was based upon this: {k: [item for item in v if item] for k, v in readcsv())

#def focusdict(): #trim down the big library into a smaller, more focused thing
#    for item in cleandict():
#        if item['Category'] == 'Lichen': #ignoring lichens
#            continue
#        else:
#            focusdict.append(item)
#    return focusdict

def writekumu(): # repackaging the dict so it can be visualized in kumu (this is vestigial)
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
                #'species': plant['Species'],
                'scientific name': sciname,
                #'common name': plant['Common Name'],
                'zone' : '',
                })
    kumu = {'elements': elements, 'connections': []}
    with open ('plantskumu.json', 'w') as outfile:
        json.dump(kumu, outfile, sort_keys=True, indent=4)


plants = cleandict()
writejson()