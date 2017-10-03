import random

def monopolyworp():
    worpen = worp1 = worp2 = 0

    while worp1 == worp2:
        worp1 = random.randrange(1,7)
        worp2 = random.randrange(1,7)
        worpen += 1

        if worp1 is worp2:
            if worpen == 3:
                print('{} + {} = (direct naar de gevangenis)'.format(worp1, worp2))
            else:
                print('{} + {} = {} (dubbel)'. format(worp1, worp2, worp1+worp2))
        else:
            print('{} + {} = {}'.format(worp1, worp2, worp1+worp2))

monopolyworp()
