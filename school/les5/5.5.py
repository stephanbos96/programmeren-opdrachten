def gemiddelde(randomzin):
    total = 0
    avg = randomzin.split()
    for i in avg:
        total += len(i)
    ave_size = float(total) / float(len(avg))
    print(ave_size)

gemiddelde(input('Typ hier een willekeurige zin in: '))

