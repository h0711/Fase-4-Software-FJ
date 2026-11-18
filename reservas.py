
# ==========================================
# GESTION DE RESERVAS
# Proyecto: Software FJ - Fase 4
# ==========================================

from excepciones import ErrorReserva, ErrorValidacion


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        # Validar que exista un cliente
        if cliente is None:
            raise ErrorReserva("Debe seleccionar un cliente.")

        # Validar que exista un servicio
        if servicio is None:
            raise ErrorReserva("Debe seleccionar un servicio.")

        # Validar la duración
        if (isinstance(duracion, bool) or
                not isinstance(duracion, (int, float)) or duracion <= 0):
            raise ErrorValidacion("La duración debe ser mayor que cero.")

        # Atributos de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo_total = 0

    # Confirmar reserva
    def confirmar(self):

        if self.estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.estado = "Confirmada"

        print("Reserva confirmada correctamente.")

    # Cancelar reserva
    def cancelar(self):

        if self.estado == "Cancelada":
            raise ErrorReserva("La reserva ya se encuentra cancelada.")

        if self.estado == "Procesada":
            raise ErrorReserva(
                "No se puede cancelar una reserva procesada."
            )

        self.estado = "Cancelada"

        print("Reserva cancelada correctamente.")

    # Procesar reserva
    def procesar(self, impuesto=19, descuento=0):

        if self.estado != "Confirmada":
            raise ErrorReserva(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:
            self.costo_total = self.servicio.calcular_costo(
                self.duracion,
                impuesto,
                descuento
            )

            self.estado = "Procesada"

            print("Reserva procesada correctamente.")

        except ErrorValidacion as error:
            raise ErrorReserva(
                "No fue posible calcular el costo de la reserva."
            ) from error

    # Mostrar información
    def mostrar_reserva(self):

        return (
            f"\n========== INFORMACION DE RESERVA ==========\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Costo total: ${self.costo_total:,.2f}\n"
            f"============================================"
        )
