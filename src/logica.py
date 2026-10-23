class CifradorLogica:
    """Clase encargada exclusivamente de la lógica matemática de cifrado y descifrado."""

    @staticmethod
    def cifrar_numero(numero_str):
        """Aplica el algoritmo de cifrado de 6 dígitos."""
        digitos = [int(d) for d in numero_str]

        # Paso 1: Sumar 7 y modulo 10
        digitos = [(d + 7) % 10 for d in digitos]

        # Paso 2: Intercambio de posiciones (0<->2, 1<->3, 4<->5)
        digitos[0], digitos[2] = digitos[2], digitos[0]
        digitos[1], digitos[3] = digitos[3], digitos[1]
        digitos[4], digitos[5] = digitos[5], digitos[4]

        return "".join(map(str, digitos))

    @staticmethod
    def descifrar_numero(numero_str):
        """Revierte el algoritmo de cifrado de 6 dígitos."""
        digitos = [int(d) for d in numero_str]

        # Paso 1: Revertir intercambio de posiciones
        digitos[0], digitos[2] = digitos[2], digitos[0]
        digitos[1], digitos[3] = digitos[3], digitos[1]
        digitos[4], digitos[5] = digitos[5], digitos[4]

        # Paso 2: Revertir la suma de 7 modulo 10 [(d + 3) % 10]
        digitos = [(d + 3) % 10 for d in digitos]

        return "".join(map(str, digitos))