def convert(celcius):
    fah = celcius * 1.8 + 32
    return fah

def table():
    for i in range(-30, 41, 10):
        print ('{0:5},{1:6}'.format(i, convert(i)))
print ('{0:6}{1:6}'.format('   c','   f'))

table()



