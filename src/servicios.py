from modelos import Reserva
from utilidades import ErrorDatoInvalido, registrar_log

# Listas del sistema
clientes = []
reservas = []

# Registrar cliente
def registrar_cliente(cliente):

    try:
        if not cliente:
            raise ErrorDatoInvalido("El cliente no puede estar vacío")

        clientes.append(cliente)

        print("Cliente registrado correctamente")

    except ErrorDatoInvalido as e:
        registrar_log(str(e))
        print(f"ERROR: {e}")

# Crear reserva
def crear_reserva(cliente, servicio, duracion):

    try:

        if duracion <= 0:
            raise ErrorDatoInvalido("La duración debe ser mayor que cero")

        if servicio.precio_base <= 0:
            raise ErrorDatoInvalido("El precio del servicio debe ser mayor que cero")

        reserva = Reserva(cliente, servicio, duracion)

        reservas.append(reserva)

        print("Reserva creada exitosamente")

        return reserva

    except ErrorDatoInvalido as e:
        registrar_log(str(e))
        print(f"ERROR: {e}")

# Mostrar reservas
def mostrar_reservas():

    try:

        if len(reservas) == 0:
            raise ErrorDatoInvalido("No existen reservas registradas")

        for reserva in reservas:

            costo = reserva.servicio.calcular_costo(reserva.duracion)

            print("\n===== RESERVA =====")
            print(reserva.cliente.obtener_identificacion())
            print(f"Servicio: {reserva.servicio.nombre}")
            print(f"Duración: {reserva.duracion}")
            print(f"Costo: ${costo}")
            print(f"Estado: {reserva.estado}")

    except ErrorDatoInvalido as e:
        registrar_log(str(e))
        print(f"ERROR: {e}")

# Buscar cliente
def buscar_cliente(nombre):

    try:

        for cliente in clientes:

            if nombre.lower() in cliente.obtener_identificacion().lower():
                return cliente

        raise ErrorDatoInvalido("Cliente no encontrado")

    except ErrorDatoInvalido as e:
        registrar_log(str(e))
        print(f"ERROR: {e}")