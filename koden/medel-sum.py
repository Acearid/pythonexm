#funktionen kalkylering
def medel(x):
   return sum(x) / len(x)

#listan x
x = [1, 2, 100, 354, 22, 143]
#Svart som variabel
svar = medel(x)
#svar text
print(svar)
