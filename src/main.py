import os
from modelos import Cliente, ReservaSala  # Solo importamos lo que existe
from servicios import GestorSistema

def ejecutar_sistema():
    # Datos de prueba
    cliente_prueba = Cliente("123", "Santiago Rivera", "santiago@correo.com")
    print(f"Sistema iniciado por: {cliente_prueba.obtener_identificacion()}")
    
    # Aquí puedes seguir con tu lógica de menú...
    print("Conexión exitosa con modelos.py")

if __name__ == "__main__":
    ejecutar_sistema()