import xmltodict

def verwerk_xml():
    bestand = open('final assigment.XML')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

stations = verwerk_xml()

print('Dit zijn de codes en de tpes van de staions: ')
for station in stations['Stations']['Station']:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print('\nDit zijn alle stations met één of meer synoniemen')

for station in stations ['Stations']['Station']:
    if station['Synoniemen'] is not None:
        for synoniem in station['Synoniemen']['Synoniem']:
            print('{} - {}'.format(station['Code'], synoniem))

print('\nDit zijn de codes en de lange namen van de staions: ')
for station in stations['Stations']['Station']:
    print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))
