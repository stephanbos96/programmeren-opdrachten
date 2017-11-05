age = eval(input("Geef je leeftijd: "))
passport = input("Nederlands paspoort: ")

if age >= 18 and (passport == "Ja" or passport == "ja" or passport == "yes" or passport == "Yes"):
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas je mag niet stemmen :(")
