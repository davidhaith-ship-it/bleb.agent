import random
chars = '!@#$%^&*()_+-<>/|[]1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
for time in range(18): # <--Change num in range for better password
    chosen_letter = random.choice(chars)
    password += chosen_letter
print('\nYour new password is: ',password,'\n')