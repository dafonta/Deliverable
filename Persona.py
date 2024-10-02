#1) Haz una clase llamada Persona que siga las siguientes condiciones:
#1.1: Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura.
#No queremos que se accedan directamente a ellos.
#Piensa que modificador de acceso es el más adecuado, también su tipo.
#Si quieres añadir algún atributo puedes hacerlo. 
import random


class Persona:

    def __init__(self, nombre=None, edad=None, sexo=None, DNI=None, peso=None, altura=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}, Sexo: {self.__sexo}, Peso: {self.__peso}kg, altura: {self.__altura}"

#calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve
#un -1, si devuelve un número entre 20 y 25 (incluidos), significa que esta por debajo de su peso ideal la función devuelve un 0 y si devuelve un valor mayor que
#25 significa que tiene sobrepeso, la función devuelve un 1. Te recomiendo que uses constantes para devolver estos valores.
    # Métodos getter
    
    def calcularIMC(self):
        bajoPeso = -1
        pesoIdeal = 0
        sobrePeso = 1

        formula = (self.__peso) / (self.__altura**2)
       
        if formula<20: print(bajoPeso)
        elif formula>25: print(sobrePeso)
        else: print(pesoIdeal)

    def pesoIdeal(self):
        formula = (self.__peso) / (self.__altura**2)
       
        if formula<20: print(self, "Tiene bajo peso")
        elif formula>25: print(self, "Tiene sobrepeso")
        else: print(self, "Tiene peso ideal") 
        
#toString(): devuelve toda la información del objeto.
    def toString(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}, Sexo: {self.__sexo}, Peso: {self.__peso}kg, altura: {self.__altura}"
    
#esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano. 
#No sera visible al exterior.
    def esMayorDeEdad(self):
        if self.__edad == None:
            print("Edad no establecida")
        elif self.__edad < 0:
            print("Edad no puede ser negativa")
        elif self.__edad < 18 and self.__edad > 0:
             return 1 
        else: return 0
    
    def verEdad(self):
        if self.__edad == None:
            print("Edad no establecida")
        elif self.__edad < 0:
            print("Edad no puede ser negativa")
        elif self.__edad < 18 and self.__edad > 0:
             print("Es menor de Edad")
        else: print("Es mayor de edad")

 #comprobarSexo(char sexo):    #comprueba que el sexo introducido es correcto. Si no es correcto, sera H.    
    def comprobarSexo(self):
        try:
         if self.__sexo == "M" or self.__sexo =="H":
             return self.__sexo
         else: return "H"
        except ValueError as e:
            e = "H"
            self.__sexo = e

#generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este su número su letra correspondiente.
    def generarDNI(self):
        newDNI = random.randint(10000000, 99999999)
        self.__DNI = newDNI
        return newDNI
#Métodos set de cada parámetro, excepto de DNI.            
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

#Un constructor por defecto.    
persona01 = Persona()

#Un constructor con el nombre, edad y sexo, el resto por defecto.
persona02 = Persona(nombre = "Juan", edad = 40, sexo = "H")

#Un constructor con todos los atributos como parámetro.
persona03 = Persona("Alejandra", 37, "M", 96123123, 50 , 1.69)

#1.4.1: Pide por teclado el nombre, la edad, sexo, peso y altura.
#nombre = input("Ingrese un nombre")
#edad = int(input("Ingrese la edad: "))
#sexo = input("Ingrese el sexo (H o M): ")
#peso = float(input("Ingrese el peso: "))
#altura = float(input("Ingrese la altura: "))

#1.4.2: Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la
#altura y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
#persona04 = Persona(nombre = input("Ingrese un nombre: "), edad = int(input("Ingrese la edad: ")), sexo = input("Ingrese el sexo (H o M): "), peso = float(input("Ingrese el peso: ")), altura = float(input("Ingrese la altura: ")))
#persona05 = Persona(nombre = input("Ingrese un nombre: "), edad = int(input("Ingrese la edad: ")), sexo = input("Ingrese el sexo (H o M): "))
persona06 = Persona()
persona06.set_nombre("Teodora")
persona06.set_edad(60)
persona06.set_sexo("M")
persona06.generarDNI()
persona06.set_peso(80)
persona06.set_altura(169)

#1.4.3: Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
#persona01.pesoIdeal()
#persona02.pesoIdeal()
#persona03.pesoIdeal()
#persona04.pesoIdeal()
#persona05.pesoIdeal()
#persona06.pesoIdeal()

#1.4.4: Indicar para cada objeto si es mayor de edad.
#persona01.verEdad()
#persona02.verEdad()
#persona03.verEdad()
#persona04.verEdad()
#persona05.verEdad()
#persona06.verEdad()

#1.4.5: Por último, mostrar la información de cada objeto.
#print(persona01)
#print(persona02)
#print(persona03)
#print(persona06)




#PRUEBAS
#print(persona01)
#print(persona02)
#print(persona03)
#persona03.calcularIMC()
#persona03.pesoIdeal()
#print(persona03.esMayorDeEdad())
#print(persona03.comprobarSexo())
#print(persona02.comprobarSexo())
#persona01.generarDNI()
#print(persona02)








