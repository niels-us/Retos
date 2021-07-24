class vehiculo:
    def __init__(self,mar,km,col):
        self.marca=mar
        self.kilometraje=km
        self.color=col
        
    def encender(self):
        print("Encendido ...")
        
class auto(vehiculo):#HEREDA DE LA CLASE VEHICULO
    def __init__(self, mar, km, col,cap):
        super().__init__(mar, km, col)
        self.capacidad= cap
        
    def encender(self):
        super().encender()
        print("Auto ... ")
        
class Camion(vehiculo):#HEREDA DE LA CLASE VEHICULO
    def __init__(self, mar, km, col,eje):
        super().__init__(mar, km, col)
        self.ejes=eje
    
    def encender(self):
        super().encender()
        print("Camion ... ")
        
ferrari = auto('Ferrari','0','amarillo',2)
# print(ferrari)
ferrari.encender()
print(ferrari.color)

camion = Camion('Buses','12300','verde',8)
# print(camion)
camion.encender()
print(camion.ejes)
