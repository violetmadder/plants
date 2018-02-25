import json




fulltaxonlist = ['Kingdom', 'Subkingdom', 'Superdivision', 'Division', 'Subdivision', 'Class', 'Subclass', 'Order', 'Family', 'Genus', 'Species', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma']
maintaxonlist = ['Kingdom', 'Division', 'Class', 'Order', 'Family', 'Genus', 'Species']

def readjson():
    with open ('plantsdict.json', 'r') as jsonfile:
        return (json.load(jsonfile))

def taxonkumu(): 
    elements = []
    for plant in readjson():
        if plant.get('Kingdom') == 'Plantae':
            if plant.get('Species'):
                for counter, taxon in enumerate(maintaxonlist):
                    if taxon == 'Species':
                        if plant.get('Common Name'):
                            label = plant.get('Common Name')
                        else:
                            label = plant.get('Scientific Name')
                    else:
                        label = plant.get(taxon)
                        elements.append({
                            'label': label,
                            'type': taxon,
                            taxon : plant.get(taxon), #current taxon
                            maintaxonlist[counter - 1] : plant.get(maintaxonlist[counter - 1] ) #parent taxon
                            }) 
               
    kumu = {'elements': elements, 'connections': []}
    return kumu

def writekumu():
    with open ('plantskumu.json', 'w') as outfile:
        json.dump(taxonkumu(), outfile, sort_keys=True, indent=4)

writekumu()


    




