from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada, Reserva
from utilidades import ErrorDatoInvalido, registrar_log

def validar_duracion(duracion):
    if duracion <= 0:
        raise ErrorDatoInvalido("La duración debe ser mayor que cero")

try:
    print("=== SISTEMA SOFTWARE FJ ===")

    nombre = input("Ingrese nombre del cliente: ")
    correo = input("Ingrese correo del cliente: ")

    cliente = Cliente(1, nombre, correo)

    print("\nServicios disponibles:")
    print("1. Reserva Sala")
    print("2. Alquiler Equipo")
    print("3. Asesoría Especializada")

    opcion = int(input("Seleccione servicio: "))
    horas = int(input("Ingrese duración en horas: "))

    validar_duracion(horas)

    if opcion == 1:
        servicio = ReservaSala("Reserva Sala", 100)

    elif opcion == 2:
        servicio = AlquilerEquipo("Alquiler Equipo", 150)

    elif opcion == 3:
        servicio = AsesoriaEspecializada("Asesoría", 200)

    else:
        raise ErrorDatoInvalido("La opción seleccionada no existe")

    reserva = Reserva(cliente, servicio, horas)

    costo = servicio.calcular_costo(horas)

    print("\n=== RESERVA EXITOSA ===")
    print(cliente.obtener_identificacion())
    print(f"Servicio: {servicio.nombre}")
    print(f"Duración: {horas} horas")
    print(f"Costo total: ${costo}")
    print(f"Estado: {reserva.estado}")

except ValueError:
    mensaje = "Debe ingresar valores numéricos válidos"
    print(f"ERROR: {mensaje}")
    registrar_log(mensaje)

except ErrorDatoInvalido as e:
    print(f"ERROR: {e}")
    registrar_log(str(e))

except Exception as e:
    print(f"Error inesperado: {e}")
    registrar_log(str(e))