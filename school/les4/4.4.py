oldpassword= input("voer het oude wachtwoord in: ")
newpassword= input('voer een nieuw wachtwoord in: ')

def new_password(oldpassword, newpassword):
    if len(newpassword) >= 6 and oldpassword != newpassword:
        return True
    else:
        return False

# new_password(oldpassword, newpassword)

print (new_password(oldpassword, newpassword))






