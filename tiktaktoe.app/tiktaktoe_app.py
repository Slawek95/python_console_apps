# stwórz grę w kółko i krzyżyk

# TODO użytkownik nie może nadpisać pola już zapisanego- WYKONANE do porpawy zmiana x,o co jesli usr pomyli sie wielokrotnie
# naprawić wybierania pozycji aby nie wyskakiwał błąd // sprubuj  try expect
# pozwolić użytkownikowi zagrać jeszcze raz
# Dodać licznik wygranych dla gracza 
# pozwolić użytkownikowi wprowadzić nick i licznik wygranych 
# zroić refactoring

import sys, os

def list_to_string(list):
    string = " "
    a = string.join(list)
    return a

def win_row(row_1):
    if row_1[0] == row_1[1] == row_1[2] and "X" in row_1 or row_1[0] == row_1[1] == row_1[2] and "O" in row_1:
        usr_won = True
        return usr_won

def win_column():
    if (row_1[0] == row_2[0] == row_3[0] and row_1[0] =="X") or (row_1[0] == row_2[0] == row_3[0] and row_1[0] == "O"):
        usr_won = True
        return usr_won      
    elif (row_1[1] == row_2[1] == row_3[1] and row_1[1] =="X") or (row_1[1] == row_2[1] == row_3[1] and row_1[1] == "O"):
        usr_won = True
        return usr_won
    elif (row_1[2] == row_2[2] == row_3[2] and row_1[2] =="X") or (row_1[2] == row_2[2] == row_3[2] and row_1[2] == "O"):
        usr_won = True
        return usr_won 

def win_cross():
    if row_1[0] == row_2[1] == row_3[2] and row_1[0] == "X" or row_1[0] == row_2[1] == row_3[2] and row_1[0] == "O":
        usr_won = True
        return usr_won

    elif row_1[2] == row_2[1] == row_3[0] and row_1[2] == "X" or row_1[2] == row_2[1] == row_3[0] and row_1[2] == "O":
        usr_won = True
        return usr_won

def print_game_status():
        print(list_to_string(row_1))
        print(list_to_string(row_2))
        print(list_to_string(row_3))

def check_sign_and_change(sign):
    if sign == "X":
        sign ="O"
    else:
        sign = "X"
    return sign

print("Witaj w grze kółko i krzyżyk")
print("Wybierz czym grasz")
print("aby wybrać kółko wybierz: 1, aby wybrać krzyżyk wybierz: 2")
row_1 = ["_","_","_"] # row_1[0] == row_1[1] == row_1[2] 
row_2 = ["_","_","_"]
row_3 = ["_","_","_"]

usr_won = False


try:
    usr_sign = int(input())
except:
    print("prowadziłeś niewłaściwą wartość, wybierz 1 lub 2")
    usr_sign = int(input())
    
sign = ""
usr_sign_range = (1,2)


while usr_sign not in usr_sign_range:
    print("NIewłaściwa wartość, wybierz: 1 lub 2")
    usr_sign = int(input())

if usr_sign == 1:
    sign = "O"
elif usr_sign == 2:
    sign = "X"

while usr_won != True:
    print("aby podać pozycję gdzie ma być wstawiony znak wybierz rząd (1,2,3) a następnie pozycję (1,2,3)")
    row = int(input())
    order = int(input())
    while order not in range(1,4) :
        print("Niewłaściwa Wartość, wybierz pozycje w rzędzie 1,2,3")
        order = int(input())



    if row == 1:
        order -= 1
        if row_1[order] == "_":
            row_1[order] = sign
        else:
            print("To pole jest zajęte.\n Wybierz inne pole!")
            sign =check_sign_and_change(sign) 
        print_game_status()
        win1 = win_column()
        win2 =win_row(row_1)
        win3 =win_cross()
        sign =check_sign_and_change(sign)
        if win1 == True or win2 == True or win3 == True:
            usr_won = True
            break

    elif row == 2:
        order -= 1
        if row_2[order] == "_":
            row_2[order] = sign 
        else:
            print("To pole jest zajęte.\n Wybierz inne pole!")
            sign =check_sign_and_change(sign)  
        print_game_status()
        win1 = win_column()
        win2 = win_row(row_2)
        win3 = win_cross()
        sign =check_sign_and_change(sign)
        if win1 == True or win2 == True or win3 == True:
            usr_won = True
            break
            
    elif row == 3:
        order -= 1
        if row_3[order] == "_":
            row_3[order] = sign
        else:
            print("To pole jest zajęte.\n Wybierz inne pole!")
            sign =check_sign_and_change(sign)
        print_game_status()
        win1 = win_column()
        win2 = win_row(row_3)
        win3 = win_cross()
        sign =check_sign_and_change(sign)
        if win1 == True or win2 == True or win3 == True:
            usr_won = True
            break   

    else:
        print("niewłaśiwa wartość")
        continue 

if usr_won == True:
    print("Wygrałeś")
    sys.exit()


    



