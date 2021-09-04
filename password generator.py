#Import all the required libraries
import random

#Generate readable words from a text file
wordlist = []
with open('Text.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        words = line.split()

#Select words of suitable lenght
        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())
word = random.choice(wordlist)

#Select random special characters and two digit numbers
special_char = ['@', '#', '$', '%', '&']
Schar = random.choice(special_char)
num = str(random.randint(10, 99))

#Generate the password
password = word + Schar + num
print(password)

