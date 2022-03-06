# stwórz grę w kółko i krzyżyk

def list_to_string(list):
    string = " "
    a = string.join(list)
    return a

print("Witaj w grze kółko i krzyżyk")
print("Wybierz czym grasz")
print("aby wybrać kółko wybierz: 1, aby wybrać krzyżyk wybierz: 2")
row_1 = ["_","_","_"]
row_2 = ["_","_","_"]
row_3 = ["_","_","_"]

usr_won = False

usr_sign = int(input())
sign = ""
if usr_sign == 1:
    sign = "O"
elif usr_sign == 2:
    sign = "X"

while usr_sign == 1 or usr_sign == 2:
    print("aby podać pozycję gdzie ma być wstawiony znak wybierz rząd (1,2,3) a następnie pozycję (1,2,3)")
    row = int(input())
    order = int(input())
    if row == 1:
        order -= 1
        row_1[order] = sign
        print(list_to_string(row_1))
        print(list_to_string(row_2))
        print(list_to_string(row_3))




