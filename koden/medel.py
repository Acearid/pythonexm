#listan nummmer
num = [1,50,123,13,15,16]

#funktionen 
def medelvarde(lista):
    #variablarna
    summa=0
    langd=0
    #loopen
    for i in lista:
        summa += i
        langd += 1
    return summa/langd
#svaret
print(medelvarde(num))