def klantnummer(filename):
    infile = open(filename, 'r')
    content = infile.read().split('\n')
    for i in content:
        regel = i.split(',')
        print ("{} heeft kaartnummer: {} ".format(regel[1],regel[0]))
    infile.close()

klantnummer('kaartnummers.txt')







