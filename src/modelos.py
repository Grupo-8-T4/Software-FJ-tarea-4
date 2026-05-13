from abc import ABC, abstractmethod

# CLASE ABSTRACTA GENERAL
class EntidadSistema(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @abstractmethod
    def obtener_identificacion(self):
        pass

# CLASE CLIENTE
class Cliente(EntidadSistema):
    def __init__(self, id_entidad, nombre, correo):
        super().__init__(id_entidad)
        self.__nombre = nombre
        self.__correo = correo

    def obtener_identificacion(self):
        return f"CLIENTE: {self.__nombre} (ID: {self._id_entidad})"

# CLASE ABSTRACTA SERVICIO
class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, horas):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Confirmada"