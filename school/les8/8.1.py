bruin = {'boxtel', 'best', 'eindhoven', 'helmond\'t hout', 'helomd', 'helmond brouwhuis','deurne'}
groen = { 'boxtel', 'best', 'eindhoven', 'geldrop', 'heeze', 'weert'}

print('beide trajecten doen de volgende stations aan: {}'.format(bruin.intersection(groen)))
print('traject bruin doet als enige deze stations aan: {}'.format(bruin.difference(groen)))
print('alle stations op beide trajecten: {}'.format(bruin.union(groen)))
