"""
    Escribir funciones que dada una cadena de caracteres:
        a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
        'logaritmos' debe devolver 'lgrtms'.
        b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
        devolver 'i ooae'.
        c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
        devolver 'vistaerou'.
        d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
        (se lee igual de izquierda a derecha que de derecha a izquierda).
"""




def solamente_consonantes(palabra):

    print(palabra)
    palabra = palabra.lower()
    longitud = len(palabra)

    
    for i in range(longitud):

        if (palabra[i]!='a' and palabra[i]!='e' and palabra[i]!='i' and palabra[i]!='o' and palabra[i]!='u'):
            print(palabra[i],end="")
    print()        


# solamente_consonantes("algoritmos")



def solamente_vocales(palabra):

    print(palabra)
    palabra = palabra.lower()
    longitud = len(palabra)

    
    for i in range(longitud):

        if (palabra[i]=='a' or palabra[i]=='e' or palabra[i]=='i' or palabra[i]=='o' or palabra[i]=='u' or palabra[i]==" "):
            print(palabra[i],end="")
    print()    

# solamente_vocales("sin consonantes")


# def siguiente_vocal(palabra):

    