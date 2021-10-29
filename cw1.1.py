import random
my_string = "Czym jest Lorem Ipsum? Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print("W tekście jest " + str(my_string.lower().count("a")) + " wystąpień litery a i " + str(my_string.lower().count("s")) + " wystąpień litery s.")
print('{:10.5}'.format('Lorem Ipsum'))
print('{:d}'.format(my_string.lower().count("k")))
print('{:06.5f}'.format(3.141592653589793))
my_string2 = {'first': 'Lorem', 'last': 'Ipsum'}
print('{last} {first}'.format(**my_string2))
print('{:{width}.{prec}f}'.format(3.141592653589793, width=7, prec=3))
print(dir(my_string))
print(my_string.replace("Lorem", "Korem"))
imie="Kacper Laszuk"
print(imie[::-1].lower().title())
lista=[]
for i in range(0,10):
    n=random.randint(0,10)
    lista.append(n)
#print(lista)
lista2=lista[5:10]
print(lista2)
lista=lista[0:5]
print(lista)
pol=[0]+lista+lista2
pol.sort(reverse=True)
print(pol)
tup = [("Kacper Laszuk",155554),("Eryk Krygier",155554)]
#print(tup)
def convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
slownik = {}
print(convert(tup,slownik))
slownik2=convert(tup,slownik)





