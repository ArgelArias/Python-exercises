class Bus():    
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getColor(self):
        return self.color

    def setColor(self, Color):
        self.color = color

    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def __str__(self):
        return "Bus Marca "+ self.marca +", color "+ self.color +", capacidad : " + str(self.capacidad)

class Pasajero():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def subirABus(self, bus):
        bus.setCapacidad(bus.getCapacidad() -1)

    def __str__(self):
        return "Pasajero nombre "+ self.nombre +", edad "+ str(self.edad)

bus = Bus('BMW', 'Blanco', 50)
print("Capacidad del bus al crearlo " + str(bus.getCapacidad()))
pasajero = Pasajero('Carlos', 29)
pasajero.subirABus(bus)
print("Capacidad del bus al subir pasajero " + str(bus.getCapacidad()))
