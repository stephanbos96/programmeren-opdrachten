def inlezen_beginstation(allstations):
    while True:
        station = input('beginstation: ')
        if station in allstations:
            return station


def inlezen_eindstation(allstations, beginstation):
    index_begin_station = allstations.index(beginstation)
    while True:
        station = input('eindstation')
        if station in allstations:
            index_begin_station = allstations.index(station)
            if index_eind_station > index_begin_station:
                return station




def omroepen_reis(allstations, beginstation, eindstation):
    index_begin = allstations.index(beginstation) + 1
    begin = 'Het beginstation is {} en is het {}e station'.format(beginstation,str(index_begin))
    index_eind = allstations.index(eindstation) + 1
    eind = 'Het eindstation is {} en is het {}e station'.format(eindstation, str(index_eind))

    print(begin)
    print(eind)
    afstand = index_eind - index_begin
    print('stand is {}'.format(str(afstand)))
    if afstand > 1:
        for index in range(index_begin + 1, index_eind):
            print(' -' + stations[index])

stations = ['schagen','heerhugowaard','alkmaar','castricum','zaandam','amsterdam sloterdijk','amsterdam centraal','amsterdam amstel','utrecht centraal','\'s-hertogenbosch','eindhoven','weert','roermond','sittard','maastricht']
beginstation = inlezen_beginstation()
eindstation = inlezen_eindstation()
omroepen_reis()