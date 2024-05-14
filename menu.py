from functions import *
from datos import *

def menu_principal():
    print("********************************************************")
    print("MENÚ PRINCIPAL")
    print("Ingresa 1 para ingresar como ADMINISTRADOR: ")
    print("Ingresa 2 para ingresar como CLIENTE: ")
    print("Ingresa 11 para guardar cambios y salir: ")
    print("********************************************************")

def menu_admin():
    print("********************************************************")
    print("MENÚ ADMINISTRADOR")
    print("Ingresa 1 para REGISTRAR un usuario: ")
    print("Ingresa 2 para ELIMINAR un usuario: ")
    print("Ingresa 3 para ACTUALIZAR información de un usuario: ")
    print("Ingresa 4 para CREAR nuevo producto: ")
    print("Ingresa 5 para ELIMINAR un producto: ")
    print("Ingresa 6 para CREAR un servicio: ")
    print("Ingresa 7 para ELIMINAR un servicio: ")
    print("Ingresa 11 para guardar cambios y salir: ")
    print("********************************************************")

def menu_cliente():
    print("********************************************************")
    print("MENÚ CLIENTE")
    print("Ingresa 1 para REGISTRARTE: ")
    print("Ingresa 2 para ADQUIRIR algun producto/servicio: ")
    print("Ingresa 3 para SABER mi categoria: ")
    print("Ingresa 11 para guardar cambios y salir: ")
    print("********************************************************")

def menu_act():
    print("********************************************************")
    print("ACTUALIZACIÓN DE DATOS")
    print("Ingresa 1 para actualizar NOMBRE: ")
    print("Ingresa 2 para actualizar DOCUMENTO: ")
    print("Ingresa 3 para actualizar DIRECCION: ")
    print("Ingresa 4 para actualizar NumTELEFONO: ")
    print("********************************************************")
            
def menu_prod():
    print("********************************************************")
    print("¿Que que deseas adquirir?")
    print("Ingresa 1 para CELULARES: ")
    print("Ingresa 2 para COMPUTADORES: ")
    print("Ingresa 3 para TELEVISORES: ")
    print("Ingresa 4 para PLAN HOGAR: ")
    print("Ingresa 5 para PLAN FIBRA OPTICA: ")
    print("Ingresa 6 para PLAN POSPAGO: ")
    print("Ingresa 7 para PLAN PREPAGO: ")
    print("********************************************************")  

def menu_servicios():
    print("********************************************************")
    print("¿Que servicio desea adquirir?")
    print("Ingresa 1 para Planes Hogar: ")
    print("Ingresa 2 para Planes Fibra Optica: ")
    print("Ingresa 3 para Planes Pospago: ")
    print("Ingresa 4 para Planes Prepago: ")
    print("********************************************************")

def menu_registroventas():
    print("********************************************************")
    print("AHORA VAMOS A REGISTRAR TU COMPRA")
    print("TIPO DE PRODUCTO")
    print("Ingresa 1 para productos [Celulares][computadores][computadores]")
    print("Ingrese 2 para Servicios")
    print("********************************************************")

def pedir_opc():
    opc = 0
    try:
        opc = int(input("Ingresa tu elección: "))
        return opc
    except Exception:
        print("Valor invalido")
        return 0









