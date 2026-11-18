
# ==========================================
# ENTIDADES GENERALES Y CLIENTES
# Proyecto: Software FJ
# ==========================================

from abc import ABC, abstractmethod
from excepciones import ErrorCliente, ErrorValidacion


# Clase abstracta
class Entidad(ABC):

    def __init__(self, identificador):
        if not identificador:
            raise ErrorValidacion("El identificador es obligatorio.")

        self._identificador = identificador

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente que hereda de Entidad
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        # Validar nombre
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorCliente("El nombre del cliente es obligatorio.")

        # Validar correo
        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise ErrorCliente("El correo electronico no es valido.")

        # Validar telefono
        if not str(telefono).isdigit() or len(str(telefono)) < 7:
            raise ErrorCliente("El numero de telefono no es valido.")

        # Atributos privados (encapsulación)
        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = str(telefono)

    # Metodo para mostrar informacion
    def mostrar_informacion(self):
        return (
            f"Identificacion: {self._identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )

    # Métodos para consultar los atributos privados
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono
