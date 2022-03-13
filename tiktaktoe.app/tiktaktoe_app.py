# stwórz grę w kółko i krzyżyk

import sys, os

def list_to_string(list):
    string = " "
    a = string.join(list)
    return a

def win_row(row_1):
    if row_1[0] == row_1[1] == row_1[2] and "X" in row_1 or row_1[0] == row_1[1] == row_1[2] and "O" in row_1:
        print("Wygrałeś")
        usr_won == True
        return usr_won

def win_column():
    if (row_1[0] == row_2[0] == row_3[0] and row_1[0] =="X") or (row_1[0] == row_2[0] == row_3[0] and row_1[0] == "O"):
        print("Wygrałeś 1")
        usr_won == True
        return usr_won      
    elif (row_1[1] == row_2[1] == row_3[1] and row_1[1] =="X") or (row_1[1] == row_2[1] == row_3[1] and row_1[1] == "O"):
        print("Wygrałeś 2")
        usr_won == True
        return usr_won
    elif (row_1[2] == row_2[2] == row_3[2] and row_1[2] =="X") or (row_1[2] == row_2[2] == row_3[2] and row_1[2] == "O"):
        print("Wygrałeś 3")
        usr_won == True
        return usr_won 

def win_cross():
    if row_1[0] == row_2[1] == row_3[2] and row_1[0] == "X" or row_1[0] == row_2[1] == row_3[2] and row_1[0] == "O":
        print("Wygrałeś 4")
        usr_won == True
        return usr_won
    elif row_1[2] == row_2[1] == row_3[0] and row_1[2] == "X" or row_1[2] == row_2[1] == row_3[0] and row_1[2] == "O":
        print("Wygrałeś 5")
        usr_won == True
        return usr_won

def print_game_status():
        print(list_to_string(row_1))
        print(list_to_string(row_2))
        print(list_to_string(row_3))

print("Witaj w grze kółko i krzyżyk")
print("Wybierz czym grasz")
print("aby wybrać kółko wybierz: 1, aby wybrać krzyżyk wybierz: 2")
row_1 = ["_","_","_"] # row_1[0] == row_1[1] == row_1[2] 
row_2 = ["_","_","_"]
row_3 = ["_","_","_"]

usr_won = False

usr_sign = int(input())
sign = ""
if usr_sign == 1:
    sign = "O"
elif usr_sign == 2:
    sign = "X"

while usr_won == False:
    print("aby podać pozycję gdzie ma być wstawiony znak wybierz rząd (1,2,3) a następnie pozycję (1,2,3)")
    row = int(input())
    order = int(input())
    if row == 1:
        order -= 1
        row_1[order] = sign
        print_game_status()
        win_column()
        win_row(row_1)
        win_cross()
        if sign == "X":
            sign ="O"
        else:
            sign = "X"
    elif row == 2:
        order -= 1
        row_2[order] = sign 
        print_game_status()
        win_column()
        win_row(row_2)
        win_cross()
        if sign == "X":
            sign ="O"
        else:
            sign = "X"
    elif row == 3:
        order -= 1
        row_3[order] = sign 
        print_game_status()
        win_column()
        win_row(row_3)
        win_cross()
        if sign == "X":
            sign ="O"
        else:
            sign = "X"        

    else:
        print("niewłaśiwa wartość")
        continue 
    if usr_won == True:
        sys.exit()

    



