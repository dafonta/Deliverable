#Haz una clase llamada Password que siga las siguientes condiciones:
#2.1: Que tenga los atributos longitud y contraseña . Por defecto, la longitud será de 8.
#Los constructores serán los siguiente:
#•Un constructor por defecto.
#•Un constructor con la longitud que nosotros le pasemos.
#•Generará una contraseña aleatoria con esa longitud.
import random
import string

class Password():
    def __init__(self, constrasena = None, longitud=8):
        self._longitud = longitud
        self._contrasena = constrasena
        
    def __str__(self):

        return f"Password: {self._contrasena}, longitud: {self._longitud}"
           
    def generarPassword(self):
        self._contrasena = "" 
        for i in range(self._longitud): 
            azar = random.randint(1,3)
            if azar == 1:
                self._contrasena += str(random.randint(0,9))
            elif azar == 2:
                self._contrasena += random.choice(string.ascii_letters)
            elif azar == 3:
                self._contrasena += random.choice(string.punctuation)

    def __repr__(self):
        return f"{self}"
    
#Método get para contraseña y longitud.
    def contrasena(self):
        return self._contrasena

    def longitud(self): 
        return self._longitud
    
#Método set para longitud.
    def set_longitud(self, longitud):
        self._longitud = longitud


#esFuerte(): devuelve un booleano si es fuerte o no,
#para que sea fuerte debe tener mas de 2 mayúsculas, mas de 1 minúscula y mas de 5 números.
    def esFuerte(self):        
        contMay = 0
        contMin = 0
        contNum = 0
        j = 0

        for i in self._contrasena:
            if self._contrasena[j].isupper() == True:
                contMay += 1
            if self._contrasena[j].islower() == True:
                contMin += 1
            if self._contrasena[j].isdigit() ==True:
                contNum += 1
            j += 1
        if contMay>2 and contMin>1 and contNum>5:
            print(True) 
        else: print(False)

#Crea un array de Passwords con el tamaño que tu le indiques por teclado.
#Crea un bucle que cree un objeto para cada posición del array.
#Indica también por teclado la longitud de los Passwords (antes de bucle).
cantidad = int(input("Ingrese la cantidad de passwords automaticos: "))
largocontra = int(input("Ingrese cuantos caracteres tendra la contraseña: "))
array = []
for i in range(cantidad):
    password = Password(longitud = largocontra)
    password.generarPassword()
    array.append(password)

#Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).

arrayBooleano = []
for i in array:
    if array[i]

        
        



#•Un constructor por defecto.
password01 = Password()

#•Un constructor con la longitud que nosotros le pasemos.
#password02 = Password(longitud = int(input("Ingrese longitud del pass: ")))



# PRUEBAS 
password01.generarPassword()
#password01.esFuerte()
print(password01)
print(password01.longitud())
password01.set_longitud(14)
print(password01.longitud())
#print(password01.contrasena())
print(array)
print(array[0])

