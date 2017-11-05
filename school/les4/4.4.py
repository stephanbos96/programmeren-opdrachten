def check_password_length(password):
    return len(password) >= 6


def is_not_diffrent(value1, value2):
    return value1 != value2

def has_numeric(string):
    return any(char.isdigit() for char in string)

def new_password(oldpassword, newpassword):
    return check_password_length(newpassword) and is_not_diffrent(oldpassword,newpassword) and has_numeric(newpassword)


print(new_password("wachtwoord1","wachtwoord2"))
print(new_password("wachtwoord1","wachtwoord"))

