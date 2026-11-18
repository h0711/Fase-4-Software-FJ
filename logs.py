
from datetime import datetime


def registrar_evento(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("registro_eventos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] EVENTO: {mensaje}\n")


def registrar_error(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("registro_eventos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] ERROR: {mensaje}\n")
