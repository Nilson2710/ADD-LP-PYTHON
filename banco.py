banco.py

import json

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            raise ValueError("La cantidad a depositar debe ser positiva")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
            else:
                raise ValueError("Fondos insuficientes")
        else:
            raise ValueError("La cantidad a retirar debe ser positiva")

    def mostrar_info(self):
        return {
            "numero_cuenta": self.numero_cuenta,
            "titular": self.titular,
            "saldo": self.saldo
        }


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0, limite_descubierto=500):
        super().__init__(numero_cuenta, titular, saldo)
        self.limite_descubierto = limite_descubierto

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.saldo + self.limite_descubierto >= cantidad:
                self.saldo -= cantidad
            else:
                raise ValueError("Excede el límite de descubierto")
        else:
            raise ValueError("La cantidad a retirar debe ser positiva")


class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0, tasa_interes=0.02):
        super().__init__(numero_cuenta, titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.tasa_interes


class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminar_cuenta(self, numero_cuenta):
        self.cuentas = [c for c in self.cuentas if c.numero_cuenta != numero_cuenta]

    def obtener_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        raise ValueError("Cuenta no encontrada")

    def listar_cuentas(self):
        return [cuenta.mostrar_info() for cuenta in self.cuentas]

