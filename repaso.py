from metodos import insertar_numeros

lista_numeros = []

for i in range(3):
    numero = input("Ingrese su número: ")
    insertar_numeros(lista_numeros, numero)
print(f"Numeros ingresados en la lista: {lista_numeros}")
