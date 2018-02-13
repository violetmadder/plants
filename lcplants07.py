import csv
import json
import pprint as pp


taxonlist = ['Kingdom', 'Subkingdom', 'Superdivision', 'Division', 'Subdivision', 'Class', 'Subclass', 'Order', 'Family', 'Genus', 'Species', 'Subspecies', 'Variety', 'Subvariety', 'Cultivar', 'Forma']


taxondict = {}

for plant in cleandict():
	




















Angiosperms = ['Acanthaceae', 'Achariaceae', 'Achatocarpaceae', 'Acoraceae', 'Actinidiaceae', 'Adoxaceae', 'Aextoxicaceae', 'Aizoaceae', 'Akaniaceae', 'Alismataceae', 'Alseuosmiaceae', 'Alstroemeriaceae', 'Altingiaceae', 'Amaranthaceae', 'Amaryllidaceae', 'Amborellaceae', 'Anacampserotaceae', 'Anacardiaceae', 'Anarthriaceae', 'Ancistrocladaceae', 'Anisophylleaceae', 'Annonaceae', 'Aphanopetalaceae', 'Aphloiaceae', 'Apiaceae', 'Apocynaceae', 'Apodanthaceae', 'Aponogetonaceae', 'Aquifoliaceae', 'Araceae', 'Araliaceae', 'Arecaceae', 'Argophyllaceae', 'Aristolochiaceae', 'Asparagaceae', 'Asteliaceae', 'Asteropeiaceae', 'Atherospermataceae', 'Austrobaileyaceae', 'Balanopaceae', 'Balanophoraceae', 'Balsaminaceae', 'Barbeuiaceae', 'Barbeyaceae', 'Basellaceae', 'Bataceae', 'Begoniaceae', 'Berberidaceae', 'Berberidopsidaceae', 'Betulaceae', 'Biebersteiniaceae', 'Bignoniaceae', 'Bixaceae', 'Blandfordiaceae', 'Bonnetiaceae', 'Boraginaceae', 'Boryaceae', 'Brassicaceae', 'Bromeliaceae', 'Brunelliaceae', 'Bruniaceae', 'Burmanniaceae', 'Burseraceae', 'Butomaceae', 'Buxaceae', 'Byblidaceae', 'Cabombaceae', 'Cactaceae', 'Calceolariaceae', 'Calophyllaceae', 'Calycanthaceae', 'Calyceraceae', 'Campanulaceae', 'Campynemataceae', 'Canellaceae', 'Cannabaceae', 'Cannaceae', 'Capparaceae', 'Caprifoliaceae', 'Cardiopteridaceae', 'Caricaceae', 'Carlemanniaceae', 'Caryocaraceae', 'Caryophyllaceae', 'Casuarinaceae', 'Celastraceae', 'Centrolepidaceae', 'Centroplacaceae', 'Cephalotaceae', 'Ceratophyllaceae', 'Cercidiphyllaceae', 'Chloranthaceae', 'Chrysobalanaceae', 'Circaeasteraceae', 'Cistaceae', 'Cleomaceae', 'Clethraceae', 'Clusiaceae', 'Colchicaceae', 'Columelliaceae', 'Combretaceae', 'Commelinaceae', 'Compositae', 'Connaraceae', 'Convolvulaceae', 'Coriariaceae', 'Cornaceae', 'Corsiaceae', 'Corynocarpaceae', 'Costaceae', 'Crassulaceae', 'Crossosomataceae', 'Ctenolophonaceae', 'Cucurbitaceae', 'Cunoniaceae', 'Curtisiaceae', 'Cyclanthaceae', 'Cymodoceaceae', 'Cynomoriaceae', 'Cyperaceae', 'Cyrillaceae', 'Cytinaceae', 'Daphniphyllaceae', 'Dasypogonaceae', 'Datiscaceae', 'Degeneriaceae', 'Diapensiaceae', 'Dichapetalaceae', 'Didiereaceae', 'Dilleniaceae', 'Dioncophyllaceae', 'Dioscoreaceae', 'Dipentodontaceae', 'Dipterocarpaceae', 'Dirachmaceae', 'Doryanthaceae', 'Droseraceae', 'Drosophyllaceae', 'Ebenaceae', 'Ecdeiocoleaceae', 'Elaeagnaceae', 'Elaeocarpaceae', 'Elatinaceae', 'Emblingiaceae', 'Ericaceae', 'Eriocaulaceae', 'Erythroxylaceae', 'Escalloniaceae', 'Eucommiaceae', 'Euphorbiaceae', 'Euphroniaceae', 'Eupomatiaceae', 'Eupteleaceae', 'Fagaceae', 'Flacourtiaceae', 'Flagellariaceae', 'Fouquieriaceae', 'Frankeniaceae', 'Garryaceae', 'Geissolomataceae', 'Gelsemiaceae', 'Gentianaceae', 'Geraniaceae', 'Gerrardinaceae', 'Gesneriaceae', 'Gisekiaceae', 'Gomortegaceae', 'Goodeniaceae', 'Goupiaceae', 'Grossulariaceae', 'Grubbiaceae', 'Guamatelaceae', 'Gunneraceae', 'Gyrostemonaceae', 'Haemodoraceae', 'Halophytaceae', 'Haloragaceae', 'Hamamelidaceae', 'Hanguanaceae', 'Haptanthaceae', 'Heliconiaceae', 'Helwingiaceae', 'Hernandiaceae', 'Himantandraceae', 'Huaceae', 'Humiriaceae', 'Hydatellaceae', 'Hydnoraceae', 'Hydrangeaceae', 'Hydrocharitaceae', 'Hydroleaceae', 'Hydrostachyaceae', 'Hypericaceae', 'Hypoxidaceae', 'Icacinaceae', 'Iridaceae', 'Irvingiaceae', 'Iteaceae', 'Ixioliriaceae', 'Ixonanthaceae', 'Joinvilleaceae', 'Juglandaceae', 'Juncaceae', 'Juncaginaceae', 'Kirkiaceae', 'Koeberliniaceae', 'Krameriaceae', 'Lacistemataceae', 'Lactoridaceae', 'Lamiaceae', 'Lanariaceae', 'Lardizabalaceae', 'Lauraceae', 'Lecythidaceae', 'Leguminosae', 'Lentibulariaceae', 'Lepidobotryaceae', 'Liliaceae', 'Limeaceae', 'Limnanthaceae', 'Linaceae', 'Linderniaceae', 'Loasaceae', 'Loganiaceae', 'Lophiocarpaceae', 'Lophopyxidaceae', 'Loranthaceae', 'Lowiaceae', 'Lythraceae', 'Magnoliaceae', 'Malpighiaceae', 'Malvaceae', 'Marantaceae', 'Marcgraviaceae', 'Martyniaceae', 'Mayacaceae', 'Melanthiaceae', 'Melastomataceae', 'Meliaceae', 'Melianthaceae', 'Menispermaceae', 'Menyanthaceae', 'Metteniusaceae', 'Misodendraceae', 'Mitrastemonaceae', 'Molluginaceae', 'Monimiaceae', 'Montiaceae', 'Montiniaceae', 'Moraceae', 'Moringaceae', 'Muntingiaceae', 'Musaceae', 'Myodocarpaceae', 'Myricaceae', 'Myristicaceae', 'Myrothamnaceae', 'Myrtaceae', 'Nartheciaceae', 'Nelumbonaceae', 'Nepenthaceae', 'Neuradaceae', 'Nitrariaceae', 'Nothofagaceae', 'Nyctaginaceae', 'Nymphaeaceae', 'Ochnaceae', 'Olacaceae', 'Oleaceae', 'Onagraceae', 'Oncothecaceae', 'Opiliaceae', 'Orchidaceae', 'Orobanchaceae', 'Oxalidaceae', 'Paeoniaceae', 'Pandaceae', 'Pandanaceae', 'Papaveraceae', 'Paracryphiaceae', 'Passifloraceae', 'Paulowniaceae', 'Pedaliaceae', 'Penaeaceae', 'Pennantiaceae', 'Pentadiplandraceae', 'Pentaphragmataceae', 'Pentaphylacaceae', 'Penthoraceae', 'Peraceae', 'Peridiscaceae', 'Petenaeaceae', 'Petermanniaceae', 'Petrosaviaceae', 'Phellinaceae', 'Philesiaceae', 'Philydraceae', 'Phrymaceae', 'Phyllanthaceae', 'Phyllonomaceae', 'Physenaceae', 'Phytolaccaceae', 'Picramniaceae', 'Picrodendraceae', 'Piperaceae', 'Pittosporaceae', 'Plantaginaceae', 'Platanaceae', 'Plocospermataceae', 'Plumbaginaceae', 'Poaceae', 'Podostemaceae', 'Polemoniaceae', 'Polygalaceae', 'Polygonaceae', 'Pontederiaceae', 'Portulacaceae', 'Posidoniaceae', 'Potamogetonaceae', 'Primulaceae', 'Proteaceae', 'Putranjivaceae', 'Quillajaceae', 'Rafflesiaceae', 'Ranunculaceae', 'Rapateaceae', 'Resedaceae', 'Restionaceae', 'Rhabdodendraceae', 'Rhamnaceae', 'Rhipogonaceae', 'Rhizophoraceae', 'Roridulaceae', 'Rosaceae', 'Rousseaceae', 'Rubiaceae', 'Ruppiaceae', 'Rutaceae', 'Sabiaceae', 'Salicaceae', 'Salvadoraceae', 'Santalaceae', 'Sapindaceae', 'Sapotaceae', 'Sarcobataceae', 'Sarcolaenaceae', 'Sarraceniaceae', 'Saururaceae', 'Saxifragaceae', 'Scheuchzeriaceae', 'Schisandraceae', 'Schlegeliaceae', 'Schoepfiaceae', 'Scrophulariaceae', 'Setchellanthaceae', 'Simaroubaceae', 'Simmondsiaceae', 'Siparunaceae', 'Sladeniaceae', 'Smilacaceae', 'Solanaceae', 'Sphaerosepalaceae', 'Sphenocleaceae', 'Stachyuraceae', 'Staphyleaceae', 'Stegnospermataceae', 'Stemonaceae', 'Stemonuraceae', 'Stilbaceae', 'Strasburgeriaceae', 'Strelitziaceae', 'Stylidiaceae', 'Styracaceae', 'Surianaceae', 'Symplocaceae', 'Talinaceae', 'Tamaricaceae', 'Tapisciaceae', 'Tecophilaeaceae', 'Tetrachondraceae', 'Tetramelaceae', 'Tetrameristaceae', 'Theaceae', 'Thomandersiaceae', 'Thurniaceae', 'Thymelaeaceae', 'Ticodendraceae', 'Tofieldiaceae', 'Torricelliaceae', 'Tovariaceae', 'Trigoniaceae', 'Trimeniaceae', 'Triuridaceae', 'Trochodendraceae', 'Tropaeolaceae', 'Typhaceae', 'Ulmaceae', 'Urticaceae', 'Vahliaceae', 'Velloziaceae', 'Verbenaceae', 'Violaceae', 'Vitaceae', 'Vivianiaceae', 'Vochysiaceae', 'Winteraceae', 'Xanthorrhoeaceae', 'Xeronemataceae', 'Xyridaceae', 'Zingiberaceae', 'Zosteraceae', 'Zygophyllacea']
Gymnosperms = ['Araucariaceae', 'Cupressaceae', 'Cycadaceae', 'Ephedraceae', 'Ginkgoaceae', 'Gnetaceae', 'Pinaceae', 'Podocarpaceae', 'Sciadopityaceae', 'Taxaceae', 'Welwitschiaceae', 'Zamiacea']
Pteridophytes = ['Anemiaceae', 'Apleniaceae', 'Aspleniaceae', 'Athyriaceae', 'Blechnaceae', 'Cibotiaceae', 'Culcitaceae', 'Cyatheaceae', 'Cystodiaceae', 'Cystopteridaceae', 'Davalliaceae', 'Dennstaedtiaceae', 'Dicksoniaceae', 'Diplaziopsidaceae', 'Dipteridaceae', 'Dryopteridacae', 'Dryopteridaceae', 'Equisetaceae', 'Gleicheniaceae', 'Hymenophyllaceae', 'Hypodematiaceae', 'IsoÃ«taceae', 'Lindsaeaceae', 'Lomariopsidaceae', 'Lonchitidaceae', 'Loxsomataceae', 'Lycopodiaceae', 'Lygodiaceae', 'Marattiaceae', 'Marsileaceae', 'Matoniaceae', 'Metaxyaceae', 'Nephrolepidaceae', 'Oleandraceae', 'Onocleaceae', 'Ophioglossaceae', 'Osmundaceae', 'Plagiogyriaceae', 'Polypodiaceae', 'Psilotaceae', 'Pteridaceae', 'Rhachidosoraceae', 'Saccolomataceae', 'Salviniaceae', 'Schizaeaceae', 'Selaginellaceae', 'Tectariaceae', 'Thelypteridaceae', 'Thyrsopteridaceae', 'Woodsiacea']
Bryophytes = ['Acrobolbaceae', 'Adelanthaceae', 'Allisoniaceae', 'Amblystegiaceae', 'Anastrophyllaceae', 'Andreaeaceae', 'Andreaeobryaceae', 'Aneuraceae', 'Antheliaceae', 'Anthocerotaceae', 'Archidiaceae', 'Arnelliaceae', 'Aulacomniaceae', 'Aytoniaceae', 'Balantiopsaceae', 'Bartramiaceae', 'Blasiaceae', 'Brachytheciaceae', 'Brevianthaceae', 'Bruchiaceae', 'Bryaceae', 'Bryobartramiaceae', 'Bryoxiphiaceae', 'Buxbaumiaceae', 'Calomniaceae', 'Calymperaceae', 'Calypogeiaceae', 'Catagoniaceae', 'Catoscopiaceae', 'Cephaloziaceae', 'Cephaloziellaceae', 'Chaetophyllopsaceae', 'Chonecoleaceae', 'Cinclidotaceae', 'Cleveaceae', 'Climaciaceae', 'Conocephalaceae', 'Corsiniaceae', 'Cryphaeaceae', 'Cyrtopodaceae', 'Daltoniaceae', 'Dendrocerotaceae', 'Dicnemonaceae', 'Dicranaceae', 'Diphysciaceae', 'Disceliaceae', 'Ditrichaceae', 'Echinodiaceae', 'Encalyptaceae', 'Entodontaceae', 'Ephemeraceae', 'Erpodiaceae', 'Eustichiaceae', 'Exormothecaceae', 'Fabroniaceae', 'Fissidentaceae', 'Fontinalaceae', 'Fossombroniaceae', 'Funariaceae', 'Geocalycaceae', 'Gigaspermaceae', 'Goebeliellaceae', 'Grimmiaceae', 'Gymnomitriaceae', 'Gyrothyraceae', 'Haplomitriaceae', 'Hedwigiaceae', 'Helicophyllaceae', 'Herbertaceae', 'Hookeriaceae', 'Hylocomiaceae', 'Hymenophytaceae', 'Hypnaceae', 'Hypnodendraceae', 'Hypopterygiaceae', 'Jackiellaceae', 'Jubulaceae', 'Jubulopsaceae', 'Jungermanniaceae', 'Lejeuneaceae', 'Lembophyllaceae', 'Lepicoleaceae', 'Lepidolaenaceae', 'Lepidoziaceae', 'Leptodontaceae', 'Lepyrodontaceae', 'Leskeaceae', 'Leucodontaceae', 'Leucomiaceae', 'Lophocoleaceae', 'Lophoziaceae', 'Lunulariaceae', 'Makinoaceae', 'Marchantiaceae', 'Mastigophoraceae', 'Meesiaceae', 'Mesoptychiaceae', 'Meteoriaceae', 'Metzgeriaceae', 'Microtheciellaceae', 'Mitteniaceae', 'Mizutaniaceae', 'Mniaceae', 'Monocarpaceae', 'Monocleaceae', 'Monosoleniaceae', 'Myriniaceae', 'Myuriaceae', 'Neckeraceae', 'Neotrichocoleaceae', 'Notothyladaceae', 'Octoblepharaceae', 'Oedipodiaceae', 'Orthorrhynchiaceae', 'Orthotrichaceae', 'Oxymitraceae', 'Pallaviciniaceae', 'Pelliaceae', 'Phyllodrepaniaceae', 'Phyllogoniaceae', 'Pilotrichaceae', 'Plagiochilaceae', 'Plagiotheciaceae', 'Pleurophascaceae', 'Pleuroziaceae', 'Pleuroziopsaceae', 'Polytrichaceae', 'Porellaceae', 'Pottiaceae', 'Prionodontaceae', 'Pseudoditrichaceae', 'Pseudolepicoleaceae', 'Pterigynandraceae', 'Pterobryaceae', 'Ptilidiaceae', 'Ptychomitriaceae', 'Ptychomniaceae', 'Racopilaceae', 'Radulaceae', 'Regmatodontaceae', 'Rhabdoweisiaceae', 'Rhachitheciaceae', 'Rhacocarpaceae', 'Rhizogoniaceae', 'Ricciaceae', 'Riellaceae', 'Rigodiaceae', 'Rutenbergiaceae', 'Scapaniaceae', 'Schistochilaceae', 'Schistostegaceae', 'Scorpidiaceae', 'Seligeriaceae', 'Sematophyllaceae', 'Serpotortellaceae', 'Sorapillaceae', 'Sphaerocarpaceae', 'Sphagnaceae', 'Spiridentaceae', 'Splachnaceae', 'Splachnobryaceae', 'Stereophyllaceae', 'Takakiaceae', 'Targioniaceae', 'Tetraphidaceae', 'Thamnobryaceae', 'Theliaceae', 'Thuidiaceae', 'Timmiaceae', 'Trachypodaceae', 'Treubiaceae', 'Trichocoleaceae', 'Trichotemnomataceae', 'Vandiemeniaceae', 'Vetaformaceae', 'Viridivelleraceae', 'Wardiaceae', 'Wiesnerellacea']
















def taxonomytree():
    for plant in cleandict():
        if not plant.get('Species'):
            continue
        else:
            species = plant.get('Species')
            if not plant.get('Kingdom'):
                continue 
            else:
                kingdom = plant['Kingdom']
                category = plant['Category']
                order = plant['Order']
                pclass = plant['Class']
                family = plant['Family']
                genus = plant['Genus']
                sciname = genus + ' ' + species
                if plant.get('Common Name'):
                    coname = plant.get('Common Name')
                else:
                    pass
                taxadict[kingdom] = {order: {pclass: {family: genus}}}
                

taxonomytree()
print (taxadict)

def listify(): #for quick found lists pasted into a text file
    templist = []
    with open ('temp.txt') as textfile:
        textfile = textfile.readlines()
        for line in textfile:
            #add something here to handle multiple columns
            templist.append(line[:-1])
        print (templist)


def readcsv():
    with open('usdasearch.txt', encoding='utf-8') as csvfile:
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
    print ("this dictionary has " + str(plantnum) + " plants")
    return filteredItems
#    {k: [item for item in v if item] for k, v in readcsv())

#def focusdict():
#    for item in cleandict():
#        if item['Category'] == 'Lichen': #ignoring lichens
#            continue
#        else:
#            focusdict.append(item)
#    return focusdict



plants = cleandict()
writejson()




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
        
        
