def main():
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    idnum = input("Enter Student ID ")
    print("Your system login name is: ")
    print(get_login_name(first, last, idnum))
    password =  input("Enter password: ")
    while not valid_password(password):
        print("Password  not valid")
        password = input("Enter password")
    print("Valid password")

def get_login_name(first, last, idnum):
    set1 = first [0:3] #Hol
    set2 = last [0:3] #Mol
    set3 = idnum[-3:]  #899

    login.name = set1+set2+set3

    return login.name

def valid_password(password):
    # set boolean to false

    correct.length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    if len(password)>7:
        correct_length = True

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True

        if correct_length and has_upper and \
            has_uppercase and \
            has_lowercase and \
                has_digit:
                isvalid = True

        else:
            is_valid = False

    return is_valid
                








            
            
