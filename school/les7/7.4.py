def ticker(filename):
    ticker_dic = {}
    file = open('ticker_dic.txt', 'r')
    context = file.readlines()
    for line in context:
        gesplit = line.split(':')
        key = gesplit[0]
        value = gesplit[1]
        ticker_dic[key] = value[:-1]
    return ticker_dic

def search(dir):
    bedrijf = input('Welk bedrijf zoek je: ')
    if bedrijf in dir.keys():
        print('Ticker symbool is {}'.format(dir[bedrijf]))
    else:
        print('Dit is niet bekend')

    ticker = input('\nWelk symbool zoek je: ')
    if ticker in dir.values():
        for tuple in dir.items():
            if tuple[1] == ticker:
                key = tuple[0]
            print('Het bedrijf dat erbij hoort {}'.format(key))

    else:
        print('Dit symbool is niet bekend')



