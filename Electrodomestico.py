#Haz una supeclase llamada Electrodomesticoque siga las siguientes condiciones:
#3.1: Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso.
#claseHeredable
class Electrodomestico:
    def __init__(self, precio = 100, color="blanco", consumoEnergetico= "F", peso= 5):
        self.precio = precio
        self.color = color
        self.consumoEnergetico = consumoEnergetico
        self.peso = peso

    def __str__(self): 
        return f"precio: ${self.precio}, color: {self.color}, consumoEnergetico: {self.consumoEnergetico}, peso: {self.peso}kg."
#Métodos get de todos los atributos.    
    def get_precio(self):
        return self.precio
    def get_color(self):
        return self.color
    def get_consumoEnergetico(self):
        return self.consumoEnergetico
    def get_peso(self):
        return self.peso
   
#comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocará al crear el objeto y no será visible.
    #def comprobarConsumoEnergetico2(self): #No respeta la consigna, pero funciona
        #valores = ("A","B","C","D","E","F")
        #for i in valores:
            #if i == self.consumoEnergetico.upper():
                #self.consumoEnergetico = self.consumoEnergetico.upper()      
                #break
        #else: self.consumoEnergetico = "F"

#comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocará al crear el objeto y no será visible.        
    def comprobarConsumoEnergetico(self, consumoEnergetico):
        self.consumoEnergetico = consumoEnergetico
        valores = ("A","B","C","D","E","F")
        for i in valores:
            if i == self.consumoEnergetico.upper():
                self.consumoEnergetico = self.consumoEnergetico.upper()      
                break
        else: self.consumoEnergetico = "F"

#comprobarColor(Stringcolor): comprueba que el color es correcto, sino lo es usa el color por defecto.
    def comprobarColor(self):
        colorDisp = ("blanco", "negro", "rojo", "azul", "gris")     
        for i in colorDisp:
            if i == self.color.lower():
                break
        else: self.color = "blanco"    

#precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño, también.
    def precioFinal(self):
        subePrecioA = {"A":100, "B":80, "C":60, "D":50,"E":30,"F":10}
        self.precio += subePrecioA.get(self.consumoEnergetico,0)
        
        if self.peso in range(0,20):
            self.precio += 10
        elif self.peso in range(20,50):
            self.precio += 50
        elif self.peso in range(50,80):
            self.precio += 80
        elif self.peso >= 80:
            self.precio += 100    

#• Un constructor por defecto.
electrodomestico01 = Electrodomestico()
electrodomestico01.comprobarConsumoEnergetico("H")
#print(electrodomestico01)
#• Un constructor con el precio y peso. El resto por defecto.
#electrodomestico02 = Electrodomestico(precio=float(input("Ingrese el precio: ")), peso=float(input("Ingrese el peso: ")))
#• Un constructor con todos los atributos.
electrodomestico03 = Electrodomestico(precio=500, color="aZul", consumoEnergetico="c", peso=20)

#print(electrodomestico03)
#electrodomestico03.comprobarConsumoEnergetico2()
#electrodomestico03.comprobarColor()
#print(electrodomestico03)
#electrodomestico03.precioFinal()
#print(electrodomestico03)
#--------------
#Crearemos una subclase llamada Lavadoracon las siguientes características:
#3.4.1: Su atributo es carga, además de los atributos heredados.
#3.4.2: Por defecto, la carga es de 5 kg. Usa una constante para ello.
class Lavadora(Electrodomestico):
    def __init__(self, precio=100, color="blanco", consumoEnergetico= "F", peso= 5,carga = 5):
        super().__init__(precio, color, consumoEnergetico, peso)
        self.carga = carga
    def __str__(self):
        return super().__str__() + f", carga: {self.carga}kg."
#Método get de carga.
    def get_carga(self):
        return self.carga 
#precioFinal(): Si tiene una carga mayor de 30 kg, aumentara el precio $ 50, sino es así no se incrementará el precio. Llama al método padre y añade el código necesario. 
# Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.   
    def precioFinal(self):
        super().precioFinal()
        if self.carga > 30:
            self.precio += 50

#Un constructor por defecto.
lavadora01 = Lavadora()
#print(lavadora01)
#Un constructor con el precio y peso. El resto por defecto.
lavadora02 = Lavadora( precio=1500, peso=80)
#print(lavadora02)
#Un constructor con la carga y el resto de los atributos heredados.
lavadora03 = Lavadora(carga=25)
#print(lavadora03)
#print(lavadora02)
#lavadora02.precioFinal()
#print(lavadora02)


#------------
#Crearemos una subclase llamada Television con las siguientes características:
#3.6.1: Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano), además de los atributos heredados.
#3.6.2: Por defecto, la resolución sera de 20 pulgadas y el sintonizador sera false.
class Television(Electrodomestico):
    def __init__(self, precio=100, color="blanco", consumoEnergetico="F", peso=5, resolucion = 20, tdt = False):
        super().__init__(precio, color, consumoEnergetico, peso)
        self.resolucion = resolucion
        self.tdt = tdt
    def __str__(self):
        return super().__str__() + f"resolucion: {self.resolucion} pulgadas, TDT: {self.tdt}"
#Método get de resolución y sintonizador TDT.
    def get_resolucion(self):
        return self.resolucion
    def get_tdt(self):
        return self.tdt
#precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementará el precio un 30% y si tiene un sintonizador TDT incorporado, aumentara $ 50.
#Recuerda las condiciones que hemos visto en la clase.
    def precioFinal(self):
        super().precioFinal()
        if self.resolucion > 40:
            self.precio *= 1.3
        if self.tdt == True:
            self.precio += 50

#3.6.4: Un constructor por defecto.
television01 = Television()
#print(television01)
#3.6.5: Un constructor con el precio y peso. El resto por defecto.
television02 = Television(precio =2500, peso = 38)
#print(television02)
#3.6.6: Un constructor con la resolución, sintonizador TDT y el resto de atributos heredados.
television03 = Television(resolucion=45, tdt=True)
#print(television03)
#television03.precioFinal()
#print(television03)


