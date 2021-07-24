class Rectangulo:
    def __init__(self, ancho,alto):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        return self.ancho*self.alto
    
class Cuadrado:
    def __init__(self,lado):
        self.lado=lado
    
    def area(self):
        return self.lado**2
    
class Triangulo:
    def __init__(self, ancho,alto):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        return (self.ancho*self.alto)/2
    
class FigurasGeometricas(Rectangulo,Cuadrado):
    def __init__(self,tipo,ancho,alto):
        self.tipo=tipo
        Rectangulo.__init__(self,ancho,alto)
        Cuadrado.__init__(self,ancho)
        Triangulo.__init__(self,ancho,alto)
        
    def area(self):
        if self.tipo == "Rectangulo":
            return Rectangulo.area(self)
        elif self.tipo == "Triangulo":
            return Triangulo.area(self)
        else:
            return Cuadrado.area(self)
       
f=FigurasGeometricas("Triangulo",20,30)
area = f.area()
print(area)

f=FigurasGeometricas("Rectangulo",20,30)
area = f.area()
print(area)


f=FigurasGeometricas("Cuadrado",20,30)
area = f.area()
print(area)

