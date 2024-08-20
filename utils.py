utils.py

import json

from banco import Banco, CuentaBancaria, CuentaCorriente, CuentaAhorro

def guardar_datos(banco, archivo):
    with open(archivo, 'w') as f:
        json.dump([cuenta.mostrar_info() for cuenta in banco.cuentas], f)

def cargar_datos(archivo):
    banco = Banco()
    try:
        with open(archivo, 'r') as f:
            cuentas = json.load(f)
            for cuenta_data in cuentas:
                cuenta = CuentaBancaria(**cuenta_data)
                banco.agregar_cuenta(cuenta)
    except FileNotFoundError:
        pass
    return banco