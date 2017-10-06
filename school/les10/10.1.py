import xmltodict

def verwerk_xml():
    bestand = open('producten.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

artikelen = verwerk_xml()

for artikel in artikelen ['artikelen'] ['artikel']:
    print(artikel['naam'])
