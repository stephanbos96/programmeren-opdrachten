def pay(uurloon, uren):
    if uren > 40:
        geld = (uurloon * 1.5) * uren
        return geld
    else:
        geld = uurloon * uren
        return geld


print(pay(100, 50))
