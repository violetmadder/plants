import csv
import json
import pprint as pp
import re

#==============================================================================
#USDA PLANTS database-specific stuff
#==============================================================================
USDAfieldnames = ["Accepted Symbol","Synonym Symbol","Symbol","Scientific Name","Hybrid Genus Indicator","Genus","Hybrid Species Indicator","Species","Subspecies Prefix","Hybrid Subspecies Indicator","Subspecies","Variety Prefix","Hybrid Variety Indicator","Variety","Subvariety Prefix","Subvariety","Forma Prefix","Forma","Genera/Binomial Author","Trinomial Author","Quadranomial Author","Questionable Taxon Indicator","Parents","Common Name","State and Province","Category","Genus","Family","Family Symbol","Family Common Name","Order","SubClass","Class","SubDivision","Division","SuperDivision","SubKingdom","Kingdom","Duration","Growth Habit","Native Status","Federal Noxious Status","State Noxious Status","Invasive","Federal T/E Status","State T/E Status","State T/E Common Name","National Wetland Indicator Status","Regional Wetland Indicator Status","Cultivar Name","Active Growth Period","After Harvest Regrowth Rate","Bloat","C:N Ratio","Coppice Potential","Fall Conspicuous","Fire Resistance","Flower Color","Flower Conspicuous","Foliage Color","Foliage Porosity Summer","Foliage Porosity Winter","Foliage Texture","Fruit Color","Fruit Conspicuous","Growth Form","Growth Rate","Height at Base Age, Maximum (feet)","Height, Mature (feet)","Known Allelopath","Leaf Retention","Lifespan","Low Growing Grass","Nitrogen Fixation","Resprout Ability","Shape and Orientation","Toxicity","Adapted to Coarse Textured Soils","Adapted to Medium Textured Soils","Adapted to Fine Textured Soils","Anaerobic Tolerance","CaCO<SUB>3</SUB> Tolerance","Cold Stratification Required","Drought Tolerance","Fertility Requirement","Fire Tolerance","Frost Free Days, Minimum","Hedge Tolerance","Moisture Use","pH (Minimum)","pH (Maximum)","Planting Density per Acre, Minimum","Planting Density per Acre, Maximum","Precipitation (Minimum)","Precipitation (Maximum)","Root Depth, Minimum (inches)","Salinity Tolerance","Shade Tolerance","Temperature, Minimum (°F)","Bloom Period","Commercial Availability","Fruit/Seed Abundance","Fruit/Seed Period Begin","Fruit/Seed Period End","Fruit/Seed Persistence","Propogated by Bare Root","Propogated by Bulbs","Propogated by Container","Propogated by Corms","Propogated by Cuttings","Propogated by Seed","Propogated by Sod","Propogated by Sprigs","Propogated by Tubers","Seeds per Pound","Seed Spread Rate","Seedling Vigor","Small Grain","Vegetative Spread Rate","Berry/Nut/Seed Product","Christmas Tree Product","Fodder Product","Fuelwood Product","Lumber Product","Naval Store Product","Nursery Stock Product","Palatable Browse Animal","Palatable Graze Animal","Palatable Human","Post Product","Protein Potential","Pulpwood Product","Veneer Product"]
#I'm sure I'm missing a few, getting a full version is tricky
maintaxonlist = ['Kingdom', 'Division', 'Class', 'Order', 'Family', 'Genus', 'Species']
fulltaxonlist = ['Kingdom', 'SubKingdom', 'Superdivision', 'Division', 'SubDivision', 'Class', 'SubClass', 'Order', 'Family', 'Genus', 'Species', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma'] 
subtaxonlist = ['SubKingdom', 'Superdivision', 'SubDivision', 'SubClass', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma' ] #these are nonessential and not every plant will have them
#the USDA versions of these ^^ have odd mid-word capitalizations
categories = ['Dicot', 'Gymnosperm', 'Moss', 'Monocot', None, 'Lichen', 'Liverwort', 'Fern', 'Hornwort', 'Green alga', 'Horsetail', 'RA', 'Lycopod', 'Quillwort', 'Whisk-fern']
growhabits = []



def USDAtags(plant):
    tags = []
    if plant.get('Palatable Human') == 'Yes':
        tags.append('edible')
    if plant.get('Nitrogen Fixation') == 'High':
        tags.append('Nfixer')
    if plant.get('Toxicity') == 'High':
        tags.append('toxic')
    if plant.get('Fire Resistance' == 'Yes'):
        tags.append('fireresist')
    if plant.get('Drought Tolerance' == 'High'):
        tags.append('droughttolerant')
    if plant.get('Duration'):
        if plant.get('Duration') == "AN":
            tags.append('Annual')
        else:
            tags.append(plant.get('Duration'))
    if plant.get('Category'):
        tags.append(plant.get('Category'))
    return tags



#change this one to work on individual plants at a time
def checktype(dictionary): #this needs adjustment, it's missing stuff where species names have weird characters
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

def taxondict(): # this needs to be broken up more cleanly
    print ('taxondict() is running')
    taxondict = {}
    elements = []
    plants = readcsv('USDAsearch.txt')
    
    pepperwood = readjson('pepperwoodlist.json')

    for counter, plant in enumerate(plants):
        sciname = plant.get('Scientific Name')
        if sciname not in pepperwood['indb']:
            continue
        else:
            kingdom = plant.get('Kingdom')
            division = plant.get('Division')
            pclass = plant.get('Class')
            order = plant.get('Order')
            family = plant.get('Family')
            genus = plant.get('Genus')
            species = plant.get('Species')
            coname = plant.get('Common Name')
            if coname:
                label = coname
            else:
                label = sciname
            symbol = plant.get('Accepted Symbol')
            fasymbol = plant.get('Family Symbol')
            faconame = plant.get('Family Common Name')
            habit = plant.get('Growth Habit')
            habit = habit.split(',')
            scinamesplit = sciname.split(' ')
            if len(scinamesplit) == 2:
                if kingdom == 'Fungi':
                    continue
                #if not counter % 19 == 0:  #randomly trims down the results so kumu can handle it
                    #continue
                else:
                    try:
                        taxondict[kingdom][division][pclass][order][family][genus][sciname]
                        continue
                    except:
                        pass
                    if taxondict.get(kingdom) == None:
                        taxondict[kingdom] = {
                                 'label': kingdom,
                                 'type': 'Kingdom',
                                'description':''
                                 }
                        elements.append({
                                 'label': kingdom,
                                 'kingdom': kingdom,
                                 'type': 'Kingdom',
                                'description':''
                                 })
                    if taxondict[kingdom].get(division) == None:
                        taxondict[kingdom][division] = {
                                 'label': division,
                                 'type': 'Division',
                                'description':''}
                        elements.append({
                                 'label': division,
                                 'kingdom': kingdom,
                                 'division': division,
                                 'type': 'Division',
                                'description':''
                                 })
                    if taxondict[kingdom][division].get(pclass) == None:
                        taxondict[kingdom][division][pclass] = {
                                'label': pclass,
                                'type': 'Class',
                                'description':''}
                        elements.append({
                                 'label': pclass,
                                 'division': division,
                                 'class': pclass,
                                 'type': 'Classs',
                                'description':''
                                 })
                    if taxondict[kingdom][division][pclass].get(order) == None:
                        taxondict[kingdom][division][pclass][order] = {
                                'label': order,
                                'type': 'Order',
                                'description':''}
                        elements.append({
                                 'label': order,
                                 'class': pclass,
                                 'order': order,
                                 'type': 'Order',
                                 'description':''
                                 })
                    if taxondict[kingdom][division][pclass][order].get(family) == None:
                        taxondict[kingdom][division][pclass][order][family] = {
                                '_id': fasymbol,
                                'order': order,
                                'label': family,
                                'type': 'Family',
                                'description':''}
                        elements.append({
                                 '_id': fasymbol,
                                 'label': family,
                                 'family': family,
                                 'order': order,
                                 'type': 'Family',
                                 'description':''
                                 })
                    if taxondict[kingdom][division][pclass][order][family].get(genus) == None:
                        taxondict[kingdom][division][pclass][order][family][genus] = {
                                'fasymbol': fasymbol,
                                'label': genus,
                                'type': 'Genus',
                                'description':''}
                        elements.append({
                                 'label': genus,
                                 'family': family,
                                 'genus': genus,
                                 'type': 'Genus',
                                'description':''
                                 })
                    else:
                        tags = planttags(plant)                    
                        taxondict[kingdom][division][pclass][order][family][genus][sciname] = {
                                '_id': symbol,
                                'fasymbol': fasymbol,
                                'label': label,
                                'sciname': sciname,
                                'coname': coname,
                                'genus': genus,
                                'habit': habit,
                                'type': 'Species',
                                'tags': tags,
                                'description':''
                                }
                        elements.append({
                                 '_id': symbol,
                                 'label': label,
                                 'fasymbol': fasymbol,
                                 'coname': coname,
                                 'sciname': sciname,
                                 'genus': genus,
                                 'habit': habit,
                                 'type': 'Species',
                                 'tags': tags,
                                 'description':''
                                 })
                
    return elements

def plantdict(): #this makes a flat dictionary of plant species, using scientific names as keys
    print ('plantdict() is running')
    plants = readcsv('USDAsearch.txt')
    plantdict = {}
    for plant in plants:
        sciname = plant.get('Scientific Name')
        sciname = re.sub('Ã—', '', sciname) #kill the weird characters plz??
        scinamesplit = sciname.split(' ')
        symbol = plant.get('Accepted Symbol')
        tags = USDAtags(plant)
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
            if scinamesplit[0][0].isupper():
                if scinamesplit[1][0].islower():
                    key = sciname# + ' ' + symbol
                    plantdict[key] = {'_id': symbol,
                             'label' : label,
                             'sciname': sciname,
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

def listscinames():
    plants = readcsv('USDAsearch.txt')
    stuff = whatkinds(plants, 'Scientific Name')
    writejson(stuff, 'scinames.json')
#==============================================================================
#misc little tools
#==============================================================================
def count(things):
    num = 0
    for thing in things:
        num = num + 1
    print ('count() counted' + str(num) + 'things')

#==============================================================================
# reading and writing files
#==============================================================================
def readfile(filename):
    print('readfile() is running')
    readfile = open(filename, 'r')
    return readfile.readlines()

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

def readkumu():
    plants = readjson('plantskumu.json')
    return plants['elements']

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

def writekumu2(elements):
    print ("writekumu2() is running")      
    kumu = {'elements': elements, 'connections': []}
    with open ('plantskumu.json', 'w') as outfile:
        json.dump(kumu, outfile, sort_keys=True, indent=4, default=lambda x: None)

#==============================================================================
#selecting and modifying more specific batches of content from the database
#==============================================================================

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
#==============================================================================
#checking batches of plants against each other
#==============================================================================                 
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
            


#==============================================================================
# asking the plant database questions
#==============================================================================

def whatkinds(plants, fieldname):
    print ('whatkinds() is running')
    kinds = []
    if type(plants) is dict:
        isdict = True
    elif type(plants)is list:
        isdict = False
    for plant in plants:
        if isdict:
            getting = plants[plant]
        else:
            getting = plant
        kind = getting.get(fieldname)
        if kind:
            if ',' in kind:
                kind = kind.split(', ')
                kinds.extend(kind)
            else:
                kinds.append(kind)
    return (list(set(kinds)))

def USDAcharacteristics(): #for checking against the USDA plant characteristics text
    print('USDAcharacteristics() is running')
    USDAfields = {}
    for fieldname in USDAfieldnames:
        toexclude = fulltaxonlist
        toexclude.extend(['Accepted Symbol', 'Symbol', 'Family Symbol', 'Family Common Name', 'Common Name', 'Scientific Name', 'Genera/Binomial Author', 'Trinomial Author', 'Quadranomial Author', 'Parents'])
        if fieldname not in toexclude:
            USDAfields[fieldname] = list(whatkinds(fieldname))
    writejson(USDAfields, 'USDAfields.json')


#plants = readcsv('USDAsearch.txt')
#stuff = whatkinds(plants, 'Genus')
#writejson(stuff, 'genera.json')

def isitgenus(word):
    if word in readfile('genera.json'):
        return True
    else:
        return False





#==============================================================================
# parsing text looking for plant information
#==============================================================================


def findspecies(text):
    genera = readjson('genera.json')
    plantsfound = []
    notspecies = ['sp','spp', 'seeds', 'to', 'was', 'thistles', 'specimens']
    for line in text:
        line = line.replace('\n','')
        line = line.replace('*', '')
        line = line.replace('â€\xa0', '')
        line = line.replace('.', '')
        line = line.replace('12','')
        line = line.replace(',', '')
        line = line.split(' ')
        capitalword = ''
        lowerword = ''
        if len(line) > 2:
            for counter, word in enumerate(line):
                if word:
                    if word is not line[-1]:
                        if word[0].isupper():
                            if word in genera:
                                if line[counter+1][0].islower():
                                    if line[counter+1] is 'x':
                                        if line[counter+2]:
                                            nextword = line[counter+2]
                                        else:
                                            continue
                                    elif line[counter+1] in notspecies:
                                        continue
                                    else:
                                        nextword = line[counter+1]
                                        maybeplant = word + ' ' + nextword
                                        plantsfound.append(maybeplant)
    return set(plantsfound)





def pepperwoodlist():  
    pepperwood = readfile('pepperwood.txt')     
    foundinpepperwood = (findspecies(pepperwood))
    foundplants = []
    generalist = readjson('genera.json')
    scinamelist = readjson('scinames.json')
    for maybeplant in foundinpepperwood:
        if maybeplant.split(' ')[0] in generalist:
            foundplants.append(maybeplant)
    plants =  readcsv('USDAsearch.txt')
    notindb = []
    indb = []
    for plant in foundplants:
        if plant not in scinamelist:
            notindb.append(plant)
        else:
            indb.append(plant)
    plants = {'notindb' : notindb,
              'indb' : indb}
    writejson(plants, 'pepperwoodlist.json')

    
#pepperwoodlist()
#writekumu2(taxondict())
##This produces a taxon tree in json for kumu-- BUT, a lot of the species are being left off. Every branch should end in a species, but many stump off at genus. Must figure that out.
    