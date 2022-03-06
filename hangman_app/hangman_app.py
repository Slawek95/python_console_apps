# TODO napisz aplikację wisielec 
# aplikacja ma pobierać hasła z pliku
# ma losowo wybierać hasła z pliku

# 1 program losuje hasło
# zamiast wyrazu są kreski
# gdy trafisz literę pojawia się zamiast kreski
# masz ograniczną ilość szans
# użyć słownika

# Zaimportowano biblioteki
import random
import sys, os
# ścieżka do pliku
PATH_TO_FILE = "python_console_apps\hangman_app\words.txt"
user_guess = {}
WORDS = []
# otwarcie pliku, słowa trafiają do listy
""""
try:
    file = open(PATH_TO_FILE, "r")
    WORDS = file.readlines()
    file.close()
except:
    print("Wystąpił błąd przy otworzeniu pliku!")
    sys.exit()
WORDS = WORDS.split()
"""
with open(PATH_TO_FILE,'r') as file:    
    for line in file:     
        for word in line.split():         
            WORDS.append(word) 

phrase = "kajak" #random.choice(WORDS) 


print(phrase)

# program przypisuje dla kluczy(indeksy) value(_)

i = 0
for letter in phrase:
    user_guess[i] = "_"
    i = i +1
for value in user_guess.values():
    print(value, end=' ')
print()
# program określa ilość prób 
usr_letter = "i"
num_of_try = 5
print("Witaj, oto aplikacja wisielec")
print()

# program sprawdza ilość pozostałych prób oraz długość wprowadzonej zmiennej
# następnie przypisuje do key(index) nowe value (usr_letter)
user_won = False

while num_of_try != 0 and len(usr_letter) != 0:
    print("Wpisz literę")
    print("aby wyjść wprowadź enetr")
    usr_letter = input()

    if usr_letter not in phrase:
        num_of_try -= 1
        print(f"niewłaściwa wartość pozostało prób: {num_of_try}")
    else:
        for item in range(len(phrase)):
            if (phrase[item] == usr_letter):
                user_guess.update({item: usr_letter})
                if "_" not in user_guess:
                    user_won = True
                    break
                    

        for value in user_guess.values():
            print(value, end=' ')
        
    
            
# program kończy się gdy ilość prób wynieśie zero 
if user_won == True:
    print("Wygrałeś")
    sys.exit()
else:
    print("------------------")
    print(f"Przegrałeś!\nPrawidłowa odpowiedź to: {phrase}\nSpróbuj jeszcze raz!")
    print("------------------")
#letter = input()
