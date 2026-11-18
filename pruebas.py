
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
        print("Resultado: Operación exitosa")
        registrar_evento(f"Prueba exitosa: {nombre}")

    finally:
        print("Prueba finalizada:", nombre)


# PRUEBAS DE VALIDACIÓN

def cliente_invalido():
    Cliente("123", "", "maria@gmail.com", "3124567890")


def correo_invalido():
    Cliente("124", "Maria Perez", "mariagmail.com", "3124567890")


def telefono_invalido():
    Cliente("125", "Maria Perez", "maria@gmail.com", "abc")


def servicio_invalido():
    ReservaSala(0)


def equipo_invalido():
    AlquilerEquipo("Computadores", -2)


def asesoria_invalida():
    AsesoriaEspecializada("")


def duracion_invalida():
    cliente = Cliente("126", "Carlos Ruiz", "carlos@gmail.com", "3101234567")
    sala = ReservaSala(20)
    Reserva(cliente, sala, 0)


def procesar_sin_confirmar():
    cliente = Cliente("127", "Laura Diaz", "laura@gmail.com", "3111234567")
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
    ("Nombre de cliente vacío", cliente_invalido),
    ("Correo electrónico incorrecto", correo_invalido),
    ("Teléfono incorrecto", telefono_invalido),
    ("Capacidad de sala incorrecta", servicio_invalido),
    ("Cantidad de equipos incorrecta", equipo_invalido),
    ("Especialidad vacía", asesoria_invalida),
    ("Duración de reserva incorrecta", duracion_invalida),
    ("Procesar reserva sin confirmar", procesar_sin_confirmar),
    ("Cancelar reserva pendiente", cancelar_reserva),
    ("Crear cliente correctamente", crear_cliente_correcto),
    ("Crear reserva sin cliente", crear_reserva_sin_cliente),
    ("Calcular costo con impuesto inválido", impuesto_invalido),
    ("Procesar dos veces la misma reserva", procesar_reserva_dos_veces),
    ("Cálculo de costo normal", calcular_costo_normal),
    ("Cálculo de costo con impuesto", calcular_costo_con_impuesto),
    ("Cálculo de costo con descuento", calcular_costo_con_descuento),
    ("Cálculo de costo con impuesto y descuento", calcular_costo_completo)
]


print("===================================")
print(" PRUEBAS DE VALIDACIÓN Y ERRORES")
print("===================================")

for nombre, funcion in pruebas:
    ejecutar_prueba(nombre, funcion)

print("\n===================================")
print(" TOTAL DE PRUEBAS:", len(pruebas))
print(" FIN DE LAS PRUEBAS")
print("===================================")

registrar_evento("Finalización de las 13 pruebas")
