def list_to_string(list):
    string = " "
    a = string.join(list)
    return a


def win_column():
    if (row_1[0] == row_2[0] == row_3[0] and row_1[0] =="X") or (row_1[0] == row_2[0] == row_3[0] and row_1[0] == "O"):
        print("Wygrałeś 1")
        return True       
    elif (row_1[1] == row_2[1] == row_3[1] and row_1[1] =="X") or (row_1[1] == row_2[1] == row_3[1] and row_1[1] == "O"):
        print("Wygrałeś 2")
        return True
    elif (row_1[2] == row_2[2] == row_3[2] and row_1[2] =="X") or (row_1[2] == row_2[2] == row_3[2] and row_1[2] == "O"):
        print("Wygrałeś 3")
        return True 

def win_cross():
    if row_1[0] == row_2[1] == row_3[2] and row_1[0] == "X" or row_1[0] == row_2[1] == row_3[2] and row_1[0] == "O":
        print("Wygrałeś 4")
        return True
    elif row_1[2] == row_2[1] == row_3[0] and row_1[2] == "X" or row_1[2] == row_2[1] == row_3[0] and row_1[2] == "O":
        print("Wygrałeś 5")
        return True


row_1 = ["X","_","O"] # row_1[0] == row_1[1] == row_1[2] 
row_2 = ["_","O","_"]
row_3 = ["O","_","_"]
print(list_to_string(row_1))


if row_1[0] == row_1[1] == row_1[2] and "_" in row_1:
    print("True")


win_column()
win_cross()
sign = "X"
for x in row_1:
    if x == "_":
        x = sign

    else:
        print("To pole jest zajęte.\n Wybierz inne pole!")
        continue
while usr_sign != 1 or usr_sign != 2:
    print("NIewłaściwa wartość, wybierz: 1 lub 2")