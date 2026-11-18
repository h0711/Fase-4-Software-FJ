
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


def ejecutar_prueba(nombre, funcion):
    print("\n-----------------------------------")
    print("PRUEBA:", nombre)

    try:
        funcion()

    except ErrorSistema as error:
        print("Error controlado:", error)
        registrar_error(f"{nombre}: {error}")

    except Exception as error:
        print("Error inesperado:", error)
        registrar_error(f"Error inesperado en {nombre}: {error}")

    else:
        print("Resultado: Operacion exitosa")
        registrar_evento(f"Prueba exitosa: {nombre}")

    finally:
        print("Prueba finalizada:", nombre)


# PRUEBAS DE VALIDACION

def cliente_invalido():
    Cliente("123", "", "7h@gmail.com", "3232843477")


def correo_invalido():
    Cliente("124", "Jaime Gonzalez", "gonzgmail.com", "3120012090")


def telefono_invalido():
    Cliente("125", "Maribel Gomez", "mago@gmail.com", "abc")


def servicio_invalido():
    ReservaSala(0)


def equipo_invalido():
    AlquilerEquipo("Computadores", -2)


def asesoria_invalida():
    AsesoriaEspecializada("")


def duracion_invalida():
    cliente = Cliente("126", "Carlos Ruiz", "carl@gmail.com", "3122234767")
    sala = ReservaSala(20)
    Reserva(cliente, sala, 0)


def procesar_sin_confirmar():
    cliente = Cliente("127", "Sebastian Castro", "sebas@gmail.com", "3178234567")
    sala = ReservaSala(20)
    reserva = Reserva(cliente, sala, 2)
    reserva.procesar()


def cancelar_reserva():
    cliente = Cliente("128", "Pedro Lopez", "pedro@gmail.com", "3151234567")
    sala = ReservaSala(20)
    reserva = Reserva(cliente, sala, 2)
    reserva.cancelar()


def crear_cliente_correcto():
    Cliente("129", "Ana Torres", "ana@gmail.com", "3001234567")


def crear_reserva_sin_cliente():
    sala = ReservaSala(20)
    Reserva(None, sala, 2)


def impuesto_invalido():
    sala = ReservaSala(20)
    sala.calcular_costo(2, impuesto=150)


def procesar_reserva_dos_veces():
    cliente = Cliente("130", "Andres Gomez", "andres@gmail.com", "3109876543")
    sala = ReservaSala(20)
    reserva = Reserva(cliente, sala, 2)

    reserva.confirmar()
    reserva.procesar()
    reserva.procesar()

def calcular_costo_normal():
    sala = ReservaSala(20)
    print("Costo normal:", sala.calcular_costo(2))

def calcular_costo_con_impuesto():
    sala = ReservaSala(20)
    print("Costo con impuesto:", sala.calcular_costo(2, impuesto=19))

def calcular_costo_con_descuento():
    sala = ReservaSala(20)
    print("Costo con descuento:", sala.calcular_costo(2, descuento=10))

def calcular_costo_completo():
    sala = ReservaSala(20)
    print(
        "Costo con impuesto y descuento:",
        sala.calcular_costo(2, impuesto=19, descuento=10)
    )


# LISTA DE LAS 13 PRUEBAS

pruebas = [
    ("Nombre de cliente vacio", cliente_invalido),
    ("Correo electronico incorrecto", correo_invalido),
    ("Telefono incorrecto", telefono_invalido),
    ("Capacidad de sala incorrecta", servicio_invalido),
    ("Cantidad de equipos incorrecta", equipo_invalido),
    ("Especialidad vacia", asesoria_invalida),
    ("Duracion de reserva incorrecta", duracion_invalida),
    ("Procesar reserva sin confirmar", procesar_sin_confirmar),
    ("Cancelar reserva pendiente", cancelar_reserva),
    ("Crear cliente correctamente", crear_cliente_correcto),
    ("Crear reserva sin cliente", crear_reserva_sin_cliente),
    ("Calcular costo con impuesto invalido", impuesto_invalido),
    ("Procesar dos veces la misma reserva", procesar_reserva_dos_veces),
    ("Calculo de costo normal", calcular_costo_normal),
    ("Calculo de costo con impuesto", calcular_costo_con_impuesto),
    ("Calculo de costo con descuento", calcular_costo_con_descuento),
    ("Calculo de costo con impuesto y descuento", calcular_costo_completo)
]


print("===================================")
print(" PRUEBAS DE VALIDACION Y ERRORES")
print("===================================")

for nombre, funcion in pruebas:
    ejecutar_prueba(nombre, funcion)

print("\n===================================")
print(" TOTAL DE PRUEBAS:", len(pruebas))
print(" FIN DE LAS PRUEBAS")
print("===================================")

registrar_evento("Finalizacion de las 13 pruebas")
