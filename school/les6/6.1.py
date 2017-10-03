def seizoen(nummer):
    seizoen = ''
    if nummer >= 3 and nummer <=5:
        print('lente')
    elif nummer >= 6 and nummer <=8:
        print('zomer')
    elif nummer >= 9 and nummer <=11:
        print('herfst')
    else:
        print('winter')
    return seizoen

for maand in range(1, 13):
    text = 'Voor maand {} is het seizoen {}'.format(str(maand), seizoen(maand))
    print(text)


