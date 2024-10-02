#Ahora crea una clase Ejecutableque realice lo siguiente:
#3.8.2: Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
from Electrodomestico import Electrodomestico
from Electrodomestico import Lavadora
from Electrodomestico import Television

if __name__ == "__main__":
#3.8.1: Crea un array de Electrodomesticos de 10 posiciones.
    array = [
        Electrodomestico(precio=500, color="aZul", consumoEnergetico="c", peso=20),
        Electrodomestico(precio=500, color="aZul", consumoEnergetico="c", peso=20),
        Electrodomestico(precio=500, color="aZul", consumoEnergetico="c", peso=20),
        Electrodomestico(precio=500, color="aZul", consumoEnergetico="c", peso=20),
        Lavadora( precio=1500, peso=80),
        Lavadora( precio=1500, peso=80),
        Lavadora( precio=2000, peso=80),
        Television(precio =2500, peso = 38),
        Television(precio =100, peso = 38),
        Television(consumoEnergetico="A", precio =2500, peso = 38)

    ]
#3.8.3: Ahora, recorre este array y ejecuta el método precioFinal().
precioElectro = 0
precioLava = 0
precioTele = 0
print(array[6].get_precio())
array[6].precioFinal()
print(array[6].get_precio())

for i in range(0, len(array)):
    array[i].precioFinal()
    print(array[i])
    precioElectro +=array[i].get_precio()
    if hasattr(array[i], "carga") == True:
        precioLava += array[i].get_precio()
    if hasattr(array[i], "resolucion") == True:
        precioTele += array[i].get_precio()


print("--------------------")
print(array[9].get_precio())
print("Precio total de los electrodomésticos: ",precioElectro)
print(array[5].get_carga())

print("--------------------")
ser =hasattr(array[5], "carga")
print(ser)
print(precioElectro)
print(precioLava)
print(precioTele) 
#print("--------------------")   
#print(array[8])
#array[8].precioFinal()
#print(array[8].get_precio())

#3.8.4: Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones por un lado, el de las lavadoras por otro y la suma de los Electrodomesticos (puedes
#crear objetos Electrodomestico, pero recuerda que Television y Lavadora también son electrodomésticos).

