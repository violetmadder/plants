import csv
import json
import pprint as pp
import re



maintaxonlist = ['Kingdom', 'Division', 'Class', 'Order', 'Family', 'Genus', 'Species']
fulltaxonlist = ['Kingdom', 'Subkingdom', 'Superdivision', 'Division', 'Subdivision', 'Class', 'Subclass', 'Order', 'Family', 'Genus', 'Species', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma']
subtaxonlist = ['Subkingdom', 'Superdivision', 'Subdivision', 'Subclass', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma' ] #these are nonessential and not every plant will have them
categories = ['Dicot', 'Gymnosperm', 'Moss', 'Monocot', None, 'Lichen', 'Liverwort', 'Fern', 'Hornwort', 'Green alga', 'Horsetail', 'RA', 'Lycopod', 'Quillwort', 'Whisk-fern']


def taxondict():
    print ("taxondict() is running")
    taxondict = {}
    for plant in readjson():
        if plant.get('Kingdom') == 'Plantae':
            if plant.get('Species'):
                for counter, taxon in enumerate(maintaxonlist):
                    if counter > 0:
                        parenttaxon = maintaxonlist[counter - 1]
                        parentname = plant.get(maintaxonlist[counter - 1])
                    if taxon == 'Species':
                        _id = plant.get('Accepted Symbol')
                        if plant.get('Common Name'):
                            label = plant.get('Common Name')
                        else:
                            label = plant.get('Scientific Name')
                        taxondict[label] = {
                        'label': label,
                        'type': taxon,
                        '_id' : _id,
                        taxon : plant.get(taxon), #current taxon
                        parenttaxon : parentname #parent taxon
                        }
                    elif counter == 0:
                        label = plant.get(taxon)
                        taxondict[label] = {
                            'label': label,
                            'type': taxon,
                            }
                    else:
                        label = plant.get(taxon)
                        taxondict[label] = {
                            'label': label,
                            'type': taxon,
                            taxon : plant.get(taxon), #current taxon
                            parenttaxon : parentname #parent taxon
                            }
    return taxondict




def checktype(dictionary):                       #this needs adjustment, it's missing stuff where species names have weird characters
    print ('checktype() is running')
    for plant in dictionary:
        sciname = plant.get('Scientific Name')
        scinamelist = sciname.split(' ')
        if plant.get('Species'):
            if len(scinamelist) == 2:
               if scinamelist[0][0].isupper():
                   if scinamelist[1][0].islower():
                       plant['type'] = 'Species'
            elif len(scinamelist) == 4:
                if scinamelist[2]== 'ssp.':
                    plant['type'] = 'Subpsecies'
                elif scinamelist[-2]== 'var.':
                    plant['type'] = 'Cultivar'
        elif not plant.get('Species'): #if the entry is missing a species name....
            if len(scinamelist) == 2:
                if scinamelist[0][0].isupper():
                    if scinamelist[1][0].islower(): #...but the scientific name has the format of a species...
                        plant['Species'] = scinamelist[1] #...fill in the species name from the full scientific name.
                        plant['type'] = 'Species'
            elif len(scinamelist) == 1: #if the scientific name is one word, this is probably a taxon and not a species
                    for counter, taxon in enumerate(maintaxonlist):
                        if not plant.get(taxon):
                            plant['type'] = maintaxonlist[counter-1] #find the first taxon field missing, step back one and set that as the type
                            #this will need more work to include subtaxoa
        else:
            plant['type'] = ''
    return dictionary



def readcsv(filename): #runs, but utf-16 characters come through as /u00 code. Will throw "Error: line contains NULL byte" if the file was saved as UTF-16
    print ("readcsv("+filename+") is running")
    with open(filename, 'r', errors = 'ignore') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        return [x for x in reader]
      
def writejson(dictionary, filename):
    print ("writejson("+filename+") is running")
    with open(filename, 'w') as outfile:
        json.dump(dictionary, outfile, sort_keys=True, indent=4)

def readjson(filename):
    print ("readjson("+filename+") is running")
    with open(filename, 'r') as jsonfile:
        return (json.load(jsonfile))

def writekumu(dictionary):
    print ("writekumu() is running")
    elements = []

    for plant in dictionary:
        dictionary[plant]['_id'] = dictionary[plant].get('Accepted Symbol')
        if dictionary[plant].get('Common Name'):
            dictionary[plant]['label'] = dictionary[plant].get('Common Name')
        elements.append(dictionary[plant])
               
    kumu = {'elements': elements, 'connections': []}
    with open ('plantskumu.json', 'w') as outfile:
        json.dump(kumu, outfile, sort_keys=True, indent=4, default=lambda x: None) #Warning: I used that default thing to hide an error

def readkumu():
    plants = readjson('plantskumu.json')
    return plants['elements']



def cleandict(dictionary): #remove empty values for easier viewing
    print ("cleandict() is running")
    filteredItems = []
    plantnum = 0
    for item in dictionary:
        plantnum = plantnum + 1
        filteredItem = {}
        for k, v in item.items(): 
            if v:
                filteredItem[k] = v
        if filteredItem:
            filteredItems.append(filteredItem)
    print ("this csv has " + str(plantnum) + " plants")
    return filteredItems
    # the above was based upon this: {k: [item for item in v if item] for k, v in readcsv())

def focusdict(dictionary): #trim down the big database into a smaller, more focused chunk
    focusdict = []
    desiredtypes = ['Kingdom', 'Division', 'Class', 'Order', 'Family', 'Genus']
    for plant in dictionary:
        if plant.get('type') not in desiredtypes:
            continue
        else:
            focusdict.append(plant)
    return focusdict

def focus2(dictionary): #gets rid of the gooey stuff and anything but straight up species
    focusdict = {}
    undesiredcats = ['Lichen', 'RA', 'Green alga']
    for plant in dictionary:
        if dictionary[plant].get('type') != 'Species':
            continue
        elif dictionary[plant].get('Category') in undesiredcats:
            continue
        elif dictionary[plant].get('Growth Habit') == 'Lichenous':
            continue
        else:
            focusdict[plant] = dictionary[plant]
    return focusdict

def focus3(dictionary):
    focusdict = {}
    for plant in dictionary:
        if dictionary[plant].get('Palatable Human') == 'Yes':
            focusdict[plant] = dictionary[plant]
    return focusdict
                     
def comparedicts(): #just getting started with this
    searchplants = readcsv('USDAsearch.txt') 
    checkedplants = readjson('checkeddict.json')
    oldplants = []
    newplants = []
    newlist = []
    for oldplant in masterplants:
        oldplants.append(oldplant.get('Symbol'))
    for newplant in searchplants:
        if newplant.get('Symbol') not in oldplants:
            newlist.append(newplant)
    return newlist
            

def countplants(dictionary):
    plantnum = 0
    for plant in dictionary:
        plantnum = plantnum + 1
    print (plantnum)






kingdoms =  ['Plantae', 'Fungi']

def taxa():
    taxondict = { 'Plantae': {}}
    plants = readjson('plantsdict.json')
    for plant in plants:
        if plants[plant].get('Kingdom') == 'Plantae':
            division = plants[plant].get('Division')
            taxondict['Plantae'][division] = {'boo'}
    return taxondict

#pp.pprint(taxa())











plants = readcsv('USDAsearch.txt')
divisions = []
for plant in plants:
    division = plant.get('Division')
    if division not in divisions:
        divisions.append(division)

print(divisions)















def freshgo():
    plants = readcsv('USDAsearch.txt')
    plantdict = {}
    for plant in plants:
        sciname = plant.get('Scientific Name')
        sciname = re.sub('Ã—', '', sciname) #kill the weird characters plz??
        scinamesplit = sciname.split(' ')
        symbol = plant.get('Accepted Symbol')
        tags = []
        coname = plant.get('Common Name')
        if coname:
            label = coname
        else:
            label = sciname
        if len(scinamesplit) == 2:
            if plant.get('Hybrid Species Indicator') is not '':
                ptype = 'hybrid'
            elif plant.get('Hybrid Species Indicator') == '':
                ptype = 'species'
            if plant.get('Palatable Human') == 'Yes':
                tags.append('edible')
            if plant.get('Nitrogen Fixation') == 'High':
                tags.append('Nfixer')
            if scinamesplit[0][0].isupper():
                if scinamesplit[1][0].islower():
                    key = sciname + ' ' + symbol
                    plantdict[key] = {'_id': symbol,
                             'label' : label,
                             'type' : ptype,
                             'species' : plant.get('Species'),
                             'genus' : plant.get('Genus'),
                             'family' : plant.get('Family'),
                             'tags' : tags,
                             'order' : plant.get('Order'),
                             'class' : plant.get('Class'),
                             'division' : plant.get('Division'),
                             'kingdom' : plant.get('Kingdom')
                             }
    writejson(plantdict, 'plantsdict.json')
    