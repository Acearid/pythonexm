num = [1,50,123,13,15,16]

def medelvarde(lista):
    summa=0
    langd=0
    for i in lista:
        summa += i
        langd += 1
    return summa/langd
print(medelvarde(num))