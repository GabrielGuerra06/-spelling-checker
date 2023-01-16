import string

oracion = input().lower()
palabra_oracion = oracion.split()
oracion_corregida = []
file = open("/Users/family/Documents/Programas_Gabriel/CLASES/3-Semestre/E. Datos/Corrector/lemario.txt" , "r", encoding="utf8")

diccionario = set()

for palabra_dic in file:
    diccionario.add(palabra_dic.rstrip("\n"))

def lemario(palabra_busqueda):
    return palabra_busqueda in diccionario


def variaciones(papa):
    variaciones = set()
    print('No encontramos la palabra, te sugerimos las siguientes')
    num_letra = len(papa)
    ac = "áéíóú"
    letras = string.ascii_lowercase
    for i in range(0,num_letra):
        var = papa[:i] + papa[i+1:]
        variaciones.add(var)
    for i in range(0, num_letra):
        for letra in letras:
            var = papa[:i] + letra + papa[i+1:]
            variaciones.add(var)
        for letra in ac:
            var = papa[:i] + letra + papa[i+1:]
            variaciones.add(var)
    for i in range(num_letra):
        if i!=num_letra-1:
            cambio= papa[:i]+ papa[i+1]+ papa[i] + papa[i+2:]
            variaciones.add(cambio)
    for i in range(0, num_letra):
        for letra in letras:
            adicion= papa[:i] + letra  + papa[i:]
            variaciones.add(adicion)
        for letra in letras:
            adicionfaltante = papa + letra
            variaciones.add(adicionfaltante)
    sugerencias = []
    for variacion in variaciones:
        if variacion in diccionario:
            sugerencias.append(variacion)
    for opciones in range(len(sugerencias)):
        print(str(opciones) + ".- " + sugerencias[opciones])
    choice = int(input())
    return sugerencias[choice]

for i in palabra_oracion:
    if (lemario(i)):
        oracion_corregida.append(i)
    else:
        oracion_corregida.append(variaciones(i))

print(" ".join(oracion_corregida))
