def eliminar_caracteres(str1, str2):
    out1 = ''.join([char for char in str1 if char not in str2])
    out2 = ''.join([char for char in str2 if char not in str1])
    print("out1:", out1)
    print("out2:", out2)
str1 = "hola"
str2 = "mundo"
eliminar_caracteres(str1, str2)