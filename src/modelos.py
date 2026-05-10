from abc import ABC, abstractmethod

# CLASE ABSTRACTA GENERAL (Requisito: Entidades generales)
class EntidadSistema(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Atributo protegido

    @abstractmethod
    def obtener_identificacion(self):
        pass

# CLASE CLIENTE (Requisito: Encapsulación y validaciones)
class Cliente(EntidadSistema):
    def __init__(self, id_entidad, nombre, correo):
        super().__init__(id_entidad)
        self.__nombre = nombre  # Atributo privado
        self.__correo = correo  # Atributo privado

    def obtener_identificacion(self):
        return f"CLIENTE: {self.__nombre} (ID: {self._id_entidad})"

# CLASE ABSTRACTA SERVICIO (Requisito: Herencia y Polimorfismo)
class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, horas):
        pass

# TRES SERVICIOS ESPECIALIZADOS
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas

class AlquilerEquipo(Servicio):
    def calcular_costo(self, horas):
        return (self.precio_base * horas) + 50 # Cargo por mantenimiento

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        # Descuento si son más de 5 horas (Sobrecarga lógica)
        total = self.precio_base * horas
        return total * 0.9 if horas > 5 else total

# CLASE RESERVA
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Confirmada"