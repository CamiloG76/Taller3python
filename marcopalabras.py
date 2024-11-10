def marco(texto):
    palabras = texto.split()
    longMax = max(len(palabra) for palabra in palabras)
    print('*' * (longMax + 4))
    for palabra in palabras:
        print(f'* {palabra.ljust(longMax)} *')
    
    print('*' * (longMax + 4))

marco("esnupi plaza 17")

