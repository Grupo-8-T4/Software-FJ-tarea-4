import datetime

# EXCEPCIONES PERSONALIZADAS (Requisito: Excepciones propias)
class ErrorSoftwareFJ(Exception):
    """Clase base para errores del sistema"""
    pass

class ErrorDatoInvalido(ErrorSoftwareFJ):
    """Se lanza cuando un dato no cumple el formato o rango"""
    pass

# FUNCIÓN DE LOGS (Requisito: Archivo de registro de errores)
def registrar_log(mensaje):
    try:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Abrimos el archivo en modo 'a' (append) para no borrar lo anterior
        with open("logs/errores.log", "a") as archivo:
            archivo.write(f"[{fecha_hora}] ERROR: {mensaje}\n")
    except Exception as e:
        print(f"No se pudo escribir en el log: {e}")