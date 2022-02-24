# TODO napisz aplikację wisielec 
# aplikacja ma pobierać hasła z pliku
# ma losowo wybierać hasła z pliku

# 1 program losuje hasło
# zamiast wyrazu są kreski
# gdy trafisz literę pojawia się zamiast kreski
# masz ograniczną ilość szans
# użyć słownika
import random

WORDS = ["kajak", "rower", "linijka", "basen", "biedronka", "komputer"]
user_guess = {} #  to co zgadł użytkownik keys = indexy, value = litera or _
phrase = random.choice(WORDS)  # to co wprowadzi użytkownik

i = 0
for letter in phrase:
    user_guess[i] = "_"
    i = i +1
for value in user_guess.values():
    print(value, end=' ')
print()
    
usr_letter = "i"
num_of_try = 5

while num_of_try != 0 and len(usr_letter) != 0:
    
    print("Wpisz literę")
    print("aby wyjść wprowadź enetr")
    usr_letter = input()
    for item in range(len(phrase)):
        if (phrase[item] == usr_letter):
            user_guess.update({item: usr_letter})
            for value in user_guess.values():
                print(value, end=' ')
    
    if usr_letter not in phrase:
        num_of_try -= 1
        print(f"niewłaściwa wartość pozostało prób: {num_of_try}")
            
if num_of_try == 0:
    print("Przegrałeś! \nSpróbuj jeszcze raz.")

        





#letter = input()
