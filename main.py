
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from sistema import SistemaGestion
from logs import registrar_evento, registrar_error

print("===================================")
print("       SISTEMA SOFTWARE FJ")
print("===================================")

sistema = SistemaGestion()
registrar_evento("Inicio del sistema Software FJ")

try:
    # Registro del cliente
    cliente1 = Cliente(
        "1007400888",
        "Heidy Saavedra",
        "7hcsl11@gmail.com",
        "3232843404"
    )

    print(sistema.registrar_cliente(cliente1))

    # Creación y registro de servicios
    sala = ReservaSala(20)
    equipo = AlquilerEquipo("Computadores", 3)
    asesoria = AsesoriaEspecializada("Desarrollo de software")

    for servicio in [sala, equipo, asesoria]:
        print(sistema.registrar_servicio(servicio))

    # Creación y procesamiento de reservas
    servicios = [
        (sala, 2),
        (equipo, 2),
        (asesoria, 1)
    ]

    for servicio, duracion in servicios:
        print("\n-----------------------------------")
        print("SERVICIO:", servicio.nombre)
        print(servicio.describir_servicio())

        reserva = sistema.crear_reserva(
            cliente1, servicio, duracion
        )

        print(reserva.mostrar_reserva())
        reserva.confirmar()
        reserva.procesar(impuesto=19, descuento=0)

        print(reserva.mostrar_reserva())
        registrar_evento(
            f"Reserva procesada: {servicio.nombre}"
        )

    # Resumen de registros
    print("\n========== RESUMEN DEL SISTEMA ==========")
    print("Clientes registrados:", len(sistema.clientes))
    print("Servicios registrados:", len(sistema.servicios))
    print("Reservas creadas:", len(sistema.reservas))

    registrar_evento("Operaciones principales finalizadas")

except Exception as error:
    print("Se presentó un error:", error)
    registrar_error(str(error))

finally:
    print("\n===================================")
    print("       FIN DEL SISTEMA")
    print("===================================")
    registrar_evento("Finalización del sistema")


