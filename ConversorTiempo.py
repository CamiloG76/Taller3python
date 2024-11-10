def conversor_tiempo(dias, horas, minutos, segundos):
    milisegundos = (dias * 24 * 60 * 60 * 1000) + (horas * 60 * 60 * 1000) + (minutos * 60 * 1000) + (segundos * 1000)
    return milisegundos
dias = int(input("Ingrese cantidad de días: "))
horas = int(input("Ingrese cantidad de horas: "))
minutos = int(input("Ingrese cantidad de minutos: "))
segundos = int(input("Ingrese cantidad de segundos: "))
resultado = conversor_tiempo(dias, horas, minutos, segundos)
print("El tiempo en milisegundos es:", resultado)
