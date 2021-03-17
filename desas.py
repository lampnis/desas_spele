#jauztaisa desu spele
#varetu sakt ar speletaju profiliem
#un vispar varetu sakt ar sveicienu
print("XOXO\nDESAS\nOXOX")

#uztaisam speletajus

geimers1 = input("Pirmais spēlētājs (o): ")
geimers2 = input("Otrais spēlētājs (x): ")
speletaji = [geimers1, geimers2]

#definejam kas ir tukss un kas ir aplitis vai krustins
empty = "_"
apple = "o"
cross = "x"
viensviens = empty
viensdivi = empty
vienstris = empty
diviviens = empty
dividivi = empty
divitris = empty
trisviens = empty
trisdivi = empty
tristris = empty
print("---Sākam spēli---\n")
speles_laukums = "      1 2 3\n    1 {} {} {}\n    2 {} {} {}\n    3 {} {} {}\n\n".format(viensviens, viensdivi, vienstris, diviviens, dividivi, divitris, trisviens, trisdivi, tristris)
print(speles_laukums)

def gajiens(speletajs, x, y):
    
    global viensviens
    global viensdivi
    global vienstris
    global diviviens
    global dividivi
    global divitris
    global trisviens
    global trisdivi
    global tristris
    global speles_laukums

    coords = [x, y]
    symb = ""
    gajieni = []

    if speletajs == geimers1:
        symb = apple
    else:
        symb = cross
    
    if (x == 1) and (y == 1):
        viensviens = symb
    elif (x == 1) and (y == 2):
        viensdivi = symb
    elif (x == 1) and (y == 3):
        vienstris = symb
    elif (x == 2) and (y == 1):
        diviviens = symb
    elif (x == 2) and (y == 2):
        dividivi = symb
    elif (x == 2) and (y == 3):
        divitris = symb
    elif (x == 3) and (y == 1):
        trisviens = symb
    elif (x == 3) and (y == 2):
        trisdivi = symb
    elif (x == 3) and (y == 3):
        tristris = symb

    gajieni.append([speletajs, [x, y]])
    
    speles_laukums = "      1 2 3\n    1 {} {} {}\n    2 {} {} {}\n    3 {} {} {}\n\n".format(viensviens, viensdivi, vienstris, diviviens, dividivi, divitris, trisviens, trisdivi, tristris)

    return speles_laukums

print(geimers1)
x1 = input('x: ')
y1 = input('y: ')
print(gajiens(geimers1, int(y1), int(x1)))

print(geimers2)
x2 = input('x: ')
y2 = input('y: ')
print(gajiens(geimers2, int(y2), int(x2)))

print(geimers1)
x3 = input('x: ')
y3 = input('y: ')
print(gajiens(geimers1, int(y3), int(x3)))

print(geimers2)
x4 = input('x: ')
y4 = input('y: ')
print(gajiens(geimers2, int(y4), int(x4)))

print(geimers1)
x5 = input('x: ')
y5 = input('y: ')
print(gajiens(geimers1, int(y5), int(x5)))

print(geimers2)
x6 = input('x: ')
y6 = input('y: ')
print(gajiens(geimers2, int(y6), int(x6)))

print(geimers1)
x7 = input('x: ')
y7 = input('y: ')
print(gajiens(geimers1, int(y7), int(x7)))

print(geimers2)
x8 = input('x: ')
y8 = input('y: ')
print(gajiens(geimers2, int(y8), int(x8)))

print(geimers1)
x9 = input('x: ')
y9 = input('y: ')
print(gajiens(geimers1, int(y9), int(x9)))
