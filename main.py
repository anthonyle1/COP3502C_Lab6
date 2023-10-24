def encoder(number):
    encoded_password = ""
    for x in range(len(number)): # password is normally 8 digits long
        if int(number[x]) >= 7: # for values 7-9 > minus 7 (account for overflow > ex: 7 to 0 instead of 10)
            encoded_password += str(int(number[x]) - 7)
        else: # for values 0-6 > add 3
            encoded_password += str(int(number[x]) + 3)

    return encoded_password