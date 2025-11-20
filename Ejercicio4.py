notas_clase = [
{"nombre": "Ana", "nota": 8.5},
{"nombre": "Luis", "nota": 4.0},
{"nombre": "Marta", "nota": 9.2},
{"nombre": "Pedro", "nota": 6.5}
]

def calcular_media(lista_alumnos):
    suma = 0
    for i in notas_clase:
        suma += i["nota"]
    media = suma/len(lista_alumnos)
    return media
print(calcular_media(notas_clase))

