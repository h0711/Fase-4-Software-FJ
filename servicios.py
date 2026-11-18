
from abc import ABC, abstractmethod
from excepciones import ErrorServicio, ErrorValidacion


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if (isinstance(tarifa_base, bool) or
                not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0):
            raise ErrorServicio("La tarifa debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    # Método de cálculo de costos de la clase padre
    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        if (isinstance(duracion, bool) or
                not isinstance(duracion, (int, float)) or duracion <= 0):
            raise ErrorValidacion("La duracion debe ser mayor que cero.")

        if (isinstance(impuesto, bool) or
                not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100):
            raise ErrorValidacion("El impuesto debe estar entre 0 y 100.")

        if (isinstance(descuento, bool) or
                not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100):
            raise ErrorValidacion("El descuento debe estar entre 0 y 100.")

        subtotal = self.tarifa_base * duracion
        subtotal -= subtotal * descuento / 100
        total = subtotal * (1 + impuesto / 100)

        return round(total, 2)


class ReservaSala(Servicio):

    def __init__(self, capacidad, tarifa_base=50000):
        super().__init__("Reserva de salas", tarifa_base)

        if (isinstance(capacidad, bool) or
                not isinstance(capacidad, int) or capacidad <= 0):
            raise ErrorServicio("La capacidad debe ser un entero positivo.")

        self.capacidad = capacidad

    def describir_servicio(self):
        return f"Sala con capacidad para {self.capacidad} personas."

    def validar_parametros(self):
        return self.capacidad > 0

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not self.validar_parametros():
            raise ErrorServicio("La capacidad de la sala no es valida.")

        return super().calcular_costo(duracion, impuesto, descuento)


class AlquilerEquipo(Servicio):

    def __init__(self, tipo_equipo, cantidad, tarifa_base=30000):
        super().__init__("Alquiler de equipos", tarifa_base)

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ErrorServicio("Debe indicar el tipo de equipo.")

        if (isinstance(cantidad, bool) or
                not isinstance(cantidad, int) or cantidad <= 0):
            raise ErrorServicio("La cantidad debe ser un entero positivo.")

        self.tipo_equipo = tipo_equipo.strip()
        self.cantidad = cantidad

    def describir_servicio(self):
        return f"Alquiler de {self.cantidad} unidad(es) de {self.tipo_equipo}."

    def validar_parametros(self):
        return self.cantidad > 0 and bool(self.tipo_equipo)

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not self.validar_parametros():
            raise ErrorServicio("Los datos del equipo no son validos.")

        return super().calcular_costo(
            duracion * self.cantidad, impuesto, descuento
        )


class AsesoriaEspecializada(Servicio):

    def __init__(self, especialidad, tarifa_base=80000):
        super().__init__("Asesoría especializada", tarifa_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ErrorServicio("Debe indicar la especialidad.")

        self.especialidad = especialidad.strip()

    def describir_servicio(self):
        return f"Asesoría especializada en {self.especialidad}."

    def validar_parametros(self):
        return bool(self.especialidad)

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if not self.validar_parametros():
            raise ErrorServicio("La especialidad no es válida.")

        return super().calcular_costo(duracion, impuesto, descuento)


