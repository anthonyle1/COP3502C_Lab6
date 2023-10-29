def encoder(number):
    encoded_password = ""
    for x in range(len(number)): # password is normally 8 digits long
        if int(number[x]) >= 7: # for values 7-9 > minus 7 (account for overflow > ex: 7 to 0 instead of 10)
            encoded_password += str(int(number[x]) - 7)
        else: # for values 0-6 > add 3
            encoded_password += str(int(number[x]) + 3)

    return encoded_password

def menu():
    return "Menu \n------------- \n1. Encode \n2. Decode \n3. Quit" # shows the user menu options

def main():
    while True:
        print(menu()) # prints menu
        option = int(input("Choose an option:")) # asks user to choose an option, based on menu prompt
        if option == 1:
            print(encoder(input("Password:"))) # asks the user for their passwords, returns encrypted password to user
        elif option == 2:
            pass # FIXME : not completed
        elif option == 3:
            break # ends program


if __name__ == "__main__":
    main()
