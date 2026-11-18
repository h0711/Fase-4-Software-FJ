
from entidades import Cliente
from servicios import Servicio
from reservas import Reserva
from excepciones import ErrorSistema


class SistemaGestion:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise ErrorSistema("El objeto no es un cliente válido.")

        self.clientes.append(cliente)
        return "Cliente registrado correctamente."

    def registrar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise ErrorSistema("El objeto no es un servicio válido.")

        self.servicios.append(servicio)
        return "Servicio registrado correctamente."

    def crear_reserva(self, cliente, servicio, duracion):
        if cliente not in self.clientes:
            raise ErrorSistema("El cliente no está registrado.")

        if servicio not in self.servicios:
            raise ErrorSistema("El servicio no está registrado.")

        reserva = Reserva(cliente, servicio, duracion)
        self.reservas.append(reserva)

        return reserva

    def mostrar_clientes(self):
        return [
            cliente.mostrar_informacion()
            for cliente in self.clientes
        ]

    def mostrar_servicios(self):
        return [
            servicio.describir_servicio()
            for servicio in self.servicios
        ]

    def mostrar_reservas(self):
        return [
            reserva.mostrar_reserva()
            for reserva in self.reservas
        ]
