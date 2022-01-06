cells = [[" "," "," "],[" "," "," "],[" "," "," "]]
winner = 0
def view_cells():
    print("  " + "0 1 2")
    print("0 " + cells[0][0], cells[0][1], cells[0][2])
    print("1 " + cells[1][0], cells[1][1], cells[1][2])
    print("2 " + cells[2][0], cells[2][1], cells[2][2])

def is_winner (a):
    if (cells[0][0]==a and cells[0][1]==a and cells[0][2]==a\
        or cells[1][0]==a and cells[1][1]==a and cells[1][2]==a\
        or cells[2][0]==a and cells[2][1]==a and cells[2][2]==a) \
        or (cells[0][0] == a and cells[1][0] == a and cells[2][0] == a \
        or cells[0][1] == a and cells[1][1] == a and cells[2][1] == a \
        or cells[0][2] == a and cells[1][2] == a and cells[2][2] == a) \
        or (cells[0][0] == a and cells[1][1] == a and cells[2][2] == a \
        or cells[0][2] == a and cells[1][1] == a and cells[2][0] == a):
        return True
    else:
        return False
while winner==0:
    view_cells()
    while winner==0:
        while winner == 0:
            x = int(input(' Первый игрок: введите строку:  '))
            if x == 0 or x == 1 or x == 2:
                break
            else:
                print("введена не правильная цифра для строки")
        while winner == 0:
            y = int(input(' Первый игрок: введите столбец:  '))
            if y == 0 or y == 1 or y == 2:
                break
            else:
                print("введена не правильная цифра для столбца")
            continue
        if  cells[x][y]== " ":
            cells[x][y] = "X"
            if is_winner("X"):
                winner = 1
                print("Победил X!!!")
            break
        else:
            print ("Ячейка уже занята введите занаво!")
    while winner==0:
        while winner == 0:
            x = int(input(' Второй игрок: введите строку:  '))
            if x == 0 or x == 1 or x == 2:
                break
            else:
                print("введена не правильная цифра для строки")
        while winner == 0:
            y = int(input(' Второй игрок: введите столбец:  '))
            if y == 0 or y == 1 or y == 2:
                break
            else:
                print("введена не правильная цифра для столбца")
            continue
        if cells[x][y] == " ":
            cells[x][y] = "0"
            if is_winner("0"):
                winner = 1
                print("Победил 0!!!")
            break
        else:
            print("Ячейка уже занята введите занаво!")
    view_cells ()


