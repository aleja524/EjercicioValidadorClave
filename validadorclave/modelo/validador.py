# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    @staticmethod
    def _contiene_mayuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    @staticmethod
    def _contiene_minuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        if self.regla.es_valida(clave):
            return True
        else:
            return False


class ReglaValidacionGanimedes(ReglaValidacion):
    pass


class ReglaValidacionCalisto(ReglaValidacion):
    pass
