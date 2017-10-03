def stats(filename):
    infile = open('oefening.txt', 'r')
    linelist = infile.readlines()
    infile.close()

    return len(linelist)

    infile = open('oefening.txt', 'r')
    content = infile.read()
    infile.close()

    wordlist = content.split()
    return len(content)

print(stats('oefening.txt'))
