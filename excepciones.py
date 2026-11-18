
# ==========================================
# EXCEPCIONES PERSONALIZADAS
# Proyecto: Software FJ
# ==========================================

class ErrorSistema(Exception):
    """Clase base para los errores del sistema."""
    pass


class ErrorCliente(ErrorSistema):
    """Errores relacionados con los clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Errores relacionados con los servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Errores relacionados con las reservas."""
    pass


class ErrorValidacion(ErrorSistema):
    """Errores ocasionados por datos inválidos."""
    pass
