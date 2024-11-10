#calculo del area de poligonos(cuadrado, triangulo, rectangulo)
def area():
    poligono = input("ingrese el tipo de polígono (triangulo, cuadrado, rectangulo): ")
    if poligono == "triangulo":
        base = float(input("ingrese la base del triangulo: "))
        altura = float(input("ingrese la altura del triangulo: "))
        return (base * altura) / 2
    elif poligono == "cuadrado":
        lado = float(input("ingrese el lado del cuadrado: "))
        return lado * lado
    elif poligono == "rectangulo":
        base = float(input("ingrese la base del rectangulo: "))
        altura = float(input("ingrese la altura del rectangulo: "))
        return base * altura
    else:
        return "este poligono no es soportado"
resultado = area()
print("el resultado del area de este poligono es:", resultado)






