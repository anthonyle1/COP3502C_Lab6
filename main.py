#   Anthony Le (owner), Andria Subhit (collaborator)

#   Anthony
def encoder(number):
    encoded_password = ""
    for x in range(len(number)): # password is normally 8 digits long
        if int(number[x]) >= 7: # for values 7-9 > minus 7 (account for overflow > ex: 7 to 0 instead of 10)
            encoded_password += str(int(number[x]) - 7)
        else: # for values 0-6 > add 3
            encoded_password += str(int(number[x]) + 3)

    return encoded_password

#   Andria
def decoder(number):

    decoded_pass = ""

    for i, num in enumerate(number):
        # for values 3-9, subtract 3
        if int(num) >= 3:
            temp = (int(num) - 3)
            decoded_pass += str(temp)
            # print(str(num) + str(temp))
            # print(i)
        if int(num) < 3:
            temp = (int(num) + 7)
            decoded_pass += str(temp)

    return decoded_pass

#   Anthony
def menu():
    return "Menu \n------------- \n1. Encode \n2. Decode \n3. Quit" # shows the user menu options

def main():
    while True:
        print(menu()) # prints menu
        print("")
        option = int(input("Choose an option:")) # asks user to choose an option, based on menu prompt
        if option == 1:
            # asks the user for their passwords, saves encrypted password
            encrypted_pw = encoder(input("Please enter your password to encode:"))
            print("Your password has been encoded and stored!")
        elif option == 2:   # Andria
            temp = decoder(encrypted_pw)
            print(f"The encoded password is {encrypted_pw}, and the original password is {temp}")
        elif option == 3:
            break # ends program
        print("")


if __name__ == "__main__":
    main()
