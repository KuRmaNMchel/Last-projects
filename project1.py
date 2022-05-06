matrix = [["",' 0 ',' 1 ',' 2 '],
    [0,'0 0','0 1','0 2'],
    [1,'1 0','1 1','1 2'],
    [2,'2 0','2 1','2 2']]
base= [["",' 0 ',' 1 ',' 2 '],
    [0,'0 0','0 1','0 2'],
    [1,'1 0','1 1','1 2'],
    [2,'2 0','2 1','2 2']]
i=1
z=1
print("КРЕСТИКИ-НОЛИКИ")
print("Перед вами игровое поле, впишите через пробел значение, например - 0 0, в которое хотите поставить Х или О. Приятной игры :)")

def net_polei():
    schetchik=0
    for mat1 in range(1,4):
        for mat2 in range(1,4):
            if matrix[mat1][mat2]!=base[mat1][mat2]:
                schetchik+=1
    if schetchik == 9:
        return True
    else:
        return False

def proverkachisel(g):
    if g[0] not in range(0,3) or g[1] not in range(0,3) or len(g) != 2:
        return False
    else:
        return True

def check():
    z=0
    if matrix[1][1]==matrix[2][2]==matrix[3][3]:
        z+=1
    if matrix[1][3]==matrix[2][2]==matrix[3][1]:
        z+=1
    for i in range(1,4):
        j=1
        if matrix[i][j]==matrix[i][j+1]==matrix[i][j+2]:
            z+=1
        else:
            z+=0
    for j in range(1,4):
        i=1
        if matrix[i][j]==matrix[i+1][j]==matrix[i+2][j]:
            z+=1
        else:
            z+=0
    if z == 1:
        return True
    else:
        return False

def  next(o):
    y=o
    if y==1:
        vernut=2
    else:
        vernut=1
    return vernut

def chto(i):
    if i == 1:
        return " X "
    else:
        return " O "

def pechatmatr():
    for i in range (0,4):
        print(matrix[i])

def changematrix(a,b,c):
    a+=1
    b+=1
    if matrix[a][b] != " X " and matrix[a][b] != " O ":
        matrix[a][b] = c
        return 1
    else:
        return 0

def hodim(d):
    stringovan=str(d)
    hod =list(map(int,input("Игрок "+ stringovan + " куда поставить " + chto(d)+"? ").split()))
    if proverkachisel(hod):
        if changematrix(*hod,chto(d)):
            pechatmatr()
            return next(d)
        else:
            print("Посмотри на игровое поле повнимательней и измени значение :)")
            pechatmatr()
            return d
    else:
        print("Введенные значения не соответствуют примеру или не принадлежат диапозону от 0 до 2, введите другие")
        print('Пример: 0 0')
        pechatmatr()
        return d

pechatmatr()
while i:
    if net_polei():
        print("------------------------------------------------")
        print("Игра закончилась ничьёй :( Повторим? :)")
        print("------------------------------------------------")
        break
    if check():
        stringuem=str(next(z))
        print("------------------------------------------------")
        print("Игра окончена. Поздравляю!!! Победил игрок "+ stringuem)
        print("------------------------------------------------")
        break
    z=hodim(z)


