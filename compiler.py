import string
file = open("t.txt", "r")
grm = []
bcode = []


def state1(i, j):  # line
    global grm
    print(10),
    print(grm[i][j-1]),
    bcode.append(10)
    bcode.append(grm[i][j-1])
    if(grm[i][j] in string.ascii_uppercase and len(grm[i][j]) == 1 and grm[i][j+1] != "eol"):
        print(11),
        print(ord(grm[i][j])-64),
        bcode.append(11)
        bcode.append(ord(grm[i][j])-64)
        state2(i, j+1)
    elif(grm[i][j] == "IF" and grm[i][j] != "eol"):
        print("13 0"),
        bcode.append(13)
        bcode.append(0)
        state3(i, j+1)
    elif(grm[i][j] == "PRINT"and grm[i][j] != "eol"):
        print("15 0"),
        bcode.append(15)
        bcode.append(0)
        state4(i, j+1)
    elif(grm[i][j] == "GOTO"and grm[i][j] != "eol"):
        print("14"),
        bcode.append(14)
        state5(i, j+1)
    elif(grm[i][j] == "STOP"and grm[i][j] != "eol"):
        bcode.append(16)
        bcode.append(0)
        print("16 0")
    else:
        print("error")
        exit(1)


def state2(i, j):  # id from line
    global grm
    if(grm[i][j] == "=" and grm[i][j+1] != 'eol'):
        print("17 4"),
        bcode.append(17)
        bcode.append(4)
        state7(i, j+1)
    else:
        print("error")
        exit(1)


def state3(i, j):  # IF from line
    global grm
    if(grm[i][j] in string.ascii_uppercase and grm[i][j] != "eol"):
        print(11),
        print(ord(grm[i][j])-64),
        bcode.append(11)
        bcode.append(ord(grm[i][j])-64)
        state9(i, j+1)
    elif (0 <= int(grm[i][j]) <= 100 and grm[i][j] != "eol"):
        print(12),
        print(grm[i][j]),
        bcode.append(12)
        bcode.append(grm[i][j])
        state9(i, j+1)
    else:
        print("error")
        exit(1)


def state4(i, j):  # print
    global grm
    if(grm[i][j] in string.ascii_uppercase):
        print(11),
        print(ord(grm[i][j])-64)
        bcode.append(11)
        bcode.append(ord(grm[i][j])-64)
    else:
        print("error")
        exit(1)


def state5(i, j):  # GOTO
    global grm
    if(grm[i][j].isdigit):
        bcode.append(grm[i][j])
        print(grm[i][j])
    else:
        print("error")
        exit(1)


def state7(i, j):  # from state 2
    global grm
    if(grm[i][j] in string.ascii_uppercase):  # upper case
        print(11),
        bcode.append(11)
        if(grm[i][j+1] != "eol"):
            bcode.append(ord(grm[i][j])-64)
            print(ord(grm[i][j])-64),
            state8(i, j+1)
        else:
            bcode.append(ord(grm[i][j])-64)
            print(ord(grm[i][j])-64)

    elif(0 <= int(grm[i][j]) <= 100):  # const
        print(12),
        bcode.append(12)
        if(grm[i][j+1] != "eol"):
            bcode.append(grm[i][j])
            print(grm[i][j]),
            state8(i, j+1)
        else:
            bcode.append(grm[i][j])
            print(grm[i][j])
    else:
        print("error")
        exit(1)


def state8(i, j):  # from state 7
    global grm
    if(grm[i][j] == "+"):
        print("17 1"),
        bcode.append(17)
        bcode.append(1)
    elif(grm[i][j] == "-"):
        print("17 2"),
        bcode.append(17)
        bcode.append(2)
    else:
        print("error")
        exit(1)
    if(grm[i][j+1] in string.ascii_uppercase and grm[i][j+1] != "eol"):
        print(11),
        print(ord(grm[i][j+1])-64),
        bcode.append(11)
        bcode.append(ord(grm[i][j+1])-64)
    elif(grm[i][j+1].isdigit and 0 <= int(grm[i][j+1]) <= 100 and grm[i][j+1] != "eol"):
        print(12),
        print(grm[i][j+1])
        bcode.append(12)
        bcode.append(grm[i][j+1])
    else:
        print("error")
        exit(1)


def state9(i, j):  # from state 3
    global grm
    if(grm[i][j] == "<"):
        print("17 3"),
        bcode.append(17)
        bcode.append(3)
    elif(grm[i][j] == "="):
        print("17 4"),
        bcode.append(17)
        bcode.append(4)
    else:
        print("error")
        exit(1)
    if(grm[i][j+1] in string.ascii_uppercase):
        print(11),
        print(ord(grm[i][j+1])-64),
        bcode.append(11)
        bcode.append(ord(grm[i][j+1])-64)
        if(grm[i][j+2] != "eol"):
            state10(i, j+2)
        else:
            print("error")
            exit(1)
    elif(grm[i][j+1].isdigit and 0 <= int(grm[i][j+1]) <= 100):
        print(12)
        print(grm[i][j+1])
        bcode.append(12)
        bcode.append(grm[i][j+1])
        if(grm[i][j+2] != "eol"):
            state10(i, j+2)
        else:
            print("error")
            exit(1)
    else:
        print("error")
        exit(1)


def state10(i, j):  # if goto
    global grm
    if(grm[i][j].isdigit and 0 <= int(grm[i][j]) <= 100):
        print(14),
        print(grm[i][j])
        bcode.append(14)
        bcode.append(grm[i][j])
    else:
        print("error")
        exit(1)


# scanner
for line in file:
    grm += [line.strip().split(" ")]

# parsing
for i in range(len(grm)):
    grm[i].append("eol")
  #  print(grm[i])
    if(grm[i][0].isdigit):
        state1(i, 1)
print(bcode)

file.close()

file = open("./output.txt", "w")
for a in bcode:
    file.write(str(a))
    file.write(" ")
print("see output.txt file.")
