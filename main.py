class Asiento:
    #Atriutos de instancia
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    #Método de instancia
    def cambiarColor(self, color):

        if (color == "rojo") or (color == "verde") or (color == "amarillo") or (color == "blanco") or (color == "negro"):
            self.color = color

class Motor:

    #Atriutos de instancia
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    #Métodos de instancia
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    #Corregido
    def asignarTipo(self, tipo):
        tipo = tipo.lower()
        if (tipo == "electrico") or (tipo == "gasolina"):
            self.tipo = tipo

class Auto:
    #Atributos estáticos
    cantidadCreados = 0

    #Atributos de instancia
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        totalAsientos = 0
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                totalAsientos+=1
        
        return totalAsientos
    
    def verificarIntegridad(self):
        for asiento in self.asientos:
            if type(asiento) == Asiento:
                if (asiento.registro == self.registro) and (Motor.registro == self.registro):
                    return "Auto original"
                else:
                    return "Las piezas no son originales"
    