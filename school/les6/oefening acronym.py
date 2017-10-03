def acronym(zin):
    woorden = zin.split()
    resultaat = ''
    for woord in woorden:
        character = woord[0]
        resultaat += character
    resultaat = resultaat.upper()
    return resultaat

antwoord = acronym('randon access memory')
print(antwoord)


