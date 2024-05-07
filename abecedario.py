abecedario1 = [["-","-","-","-","-","-"],
               ["-","-","-","-","-","-"],
               ["-","-","-","-","-","-"],
               ["-","-","-","-","-","-"],
               ["-","-","-","-","-","-"]]

abecedario2 = [["a","c","d","e","f","g"],
                ["h","i","j","k","l","m"],
                ["n","ñ","o","p","q","r"],
                ["s","t","u","v","w","x"],
                ["y","z","ch","rr"]]
def fnt_limpiar():
    import os
    os.system("cls")
    print("Yasuan C ")
    print("\n\n")
    fnt_pintarMatriz
    print("\n\n")
fila = 0
columna = 0
def fnt_validarPos(dato,x,y):
    global fila 
    global columna
    for i in range (len(abecedario2)):
        for j in range (len(abecedario2[i])):
            if abecedario2[i][j] == dato :
                fila = i
                columna = j
                break
    if int (fila) == x and columna == y:
        abecedario1[fila][columna] = abecedario2[fila][columna]
                
        input("\nDato registrado con exito <ENTER>")
    else:

        input("\nLa posicion no coincide <ENTER>")
def fnt_pintarMatriz():
    for i in range(len(abecedario1)):
        for j in range(len(abecedario1[i])):
            print(abecedario1[i][j],end=" ")
        print("\n")
sw = True
while sw == True:
    opcion = fnt_validarPos(input("Fila :") ,int(input("Fila: ")), int(input("Columna: ")))

