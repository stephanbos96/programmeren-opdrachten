import datetime

nu = datetime.datetime.today()
s = nu.strftime('%a %d %b %y, %H:%M:%S')

outfile = open('hardlopers.txt', 'a')

while True:
    naam = input('Wat is je naam: ')
    if naam == 'stop':
        break
    else:
        text = '{} {}\n'.format(s, naam)
        outfile.write(text)

outfile.close()

