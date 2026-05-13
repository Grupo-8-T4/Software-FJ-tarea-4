import logging
# Cambiamos el nombre para que coincida con lo que ya está en Git
from utilidades import ErrorSoftwareFJ, registrar_log 

# Configuración de logs básica para consola
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class GestorSistema:
    def __init__(self):
        self._empleados = []

    def registrar_empleado(self, empleado):
        try:
            if not empleado.nombre or not empleado.nombre.strip():
                # Usamos el nombre de la clase que ya está en utilidades.py
                raise ErrorSoftwareFJ("El nombre no puede estar vacío.")

            if empleado.salario_base <= 0:
                raise ErrorSoftwareFJ(f"El salario de {empleado.nombre} debe ser mayor a cero.")

            self._empleados.append(empleado)
            logging.info(f"Registro exitoso: {empleado.nombre}")
            
        except ErrorSoftwareFJ as e:
            # Usamos la función registrar_log que ya subiste
            registrar_log(str(e)) 
            logging.error(f"Operación denegada: {e}")
            raise e

    def get_lista_empleados(self):
        return self._empleados