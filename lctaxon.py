import json




fulltaxonlist = ['Kingdom', 'Subkingdom', 'Superdivision', 'Division', 'Subdivision', 'Class', 'Subclass', 'Order', 'Family', 'Genus', 'Species', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma']
maintaxonlist = ['Kingdom', 'Division', 'Class', 'Order', 'Family', 'Genus', 'Species']

def readjson():
    with open ('plantsdict.json', 'r') as jsonfile:
        return (json.load(jsonfile))

def taxonkumu():
    print ("taxonkumu() is running")
    elements = []
    for plant in readjson():
        if plant.get('Kingdom') == 'Plantae':
            if plant.get('Species'):
                for counter, taxon in enumerate(maintaxonlist):
                    parenttaxon = maintaxonlist[counter - 1]
                    parentname = plant.get(maintaxonlist[counter - 1])
                    if taxon == 'Species':
                        _id = plant.get('Accepted Symbol')
                        if plant.get('Common Name'):
                            label = plant.get('Common Name')
                        else:
                            label = plant.get('Scientific Name')
                        elements.append({
                        'label': label,
                        'type': taxon,
                        '_id' : _id,
                        taxon : plant.get(taxon), #current taxon
                        parenttaxon : parentname #parent taxon
                        }) 
                    elif counter == 0:
                        label = plant.get(taxon)
                        elements.append({
                            'label': label,
                            'type': taxon,
                            }) 
                    else:
                        label = plant.get(taxon)
                        elements.append({
                            'label': label,
                            'type': taxon,
                            taxon : plant.get(taxon), #current taxon
                            parenttaxon : parentname #parent taxon
                            }) 

               
    kumu = {'elements': elements, 'connections': []}
    return kumu

def writekumu():
    print ("writekumu() is running")
    with open ('plantskumu.json', 'w') as outfile:
        json.dump(taxonkumu(), outfile, sort_keys=True, indent=4, default=lambda x: None) #Warning: I used that default thing to hide an error

writekumu()


    




