from menu import *
from datos import*

def crear_user_admin(datos):
    datos = dict(datos)
    user={}
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    user["nombre"]=input("Ingrese su nombre completo").lower()                              #Lee NOMBRE
    ti = user["documento"]= (input("Ingrese el número de documento de identidad"))          #lee T.I

    while len(ti)!=10:                        
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")                                              
        print("Documento de identidad inválido")                                            #VALIDA T.I
        ti = user["documento"]= (input("Ingrese el número de documento de identidad"))

    user["direccion"]= input("Ingrese su dirección").lower()                                #Lee DIRECCIÓN
    tel = user["numtelefono"]= (input("Ingrese su número de teléfono"))                      #Lee Tel

    while len(tel) != 10:
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")
        print("Número telefonico inválido")                                                 #VALIDA TEL
        tel = user["numtelefono"]= (input("Ingrese su número de teléfono")) 

    categoria = input ("Ingrese categoría a dar [Nuevo][Regular][Leal]").lower()            #Lee Categoria
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    while categoria !="nuevo"and categoria !="leal"and categoria !="regular":               #Valida Categoria
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")
        print("Categoría inválida")
        categoria = input ("El usuario es [Nuevo][Regular][Leal]").lower()                  #Lee Categoria
    if categoria == "nuevo":
        datos["user_nuevo"].append(user)                                                    #Agrega a User_nuevo
    elif categoria == "regular":
        datos["user_regular"].append(user)                                                  #Agrega a User_Regular
    elif categoria == "leal":
        datos["user_leal"].append(user)                                                     #Agrega a User_Leal
    print("---------------------------------")
    print("¡Usuario registrado exitosamente!")
    print("---------------------------------")
    
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    return datos

def crear_user_cliente(datos):
    datos = dict(datos)
    user = {}
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    user["nombre"]=input("Ingrese su nombre completo").lower()                          #Lee Nombre
    ti = user["documento"]= (input("Ingrese el número de documento de identidad"))      #Lee TI

    while len(ti)!=10:
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")
        print("Documento de identidad inválido")                                        #Valida TI
        ti = user["documento"]= input("Ingrese el número de documento de identidad")
    
    user["direccion"]= input("Ingrese su direccion").lower()                            #Lee Direccion
    tel = user["numtelefono"]= input("Ingrese su número de teléfono")                    #LEE TELEFONO

    while len(tel) != 10:
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")
        print("Número de teléfono inválido")                                             #Valida TEL
        tel = user["numtelefono"]= input("Ingrese su número de teléfono")

    datos["user_nuevo"].append(user)                                                    #Agrega usuario
    print("-----------------------------")
    print("¡Has registrado exitosamente!")
    print("-----------------------------")
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    return datos
    
def eliminar_user(datos):
    datos = dict(datos)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    ti = (input("Ingrese el número de su documento de identidad"))              #Lee T.I

    while len(ti)!=10:
        print("Documento de identidad inválido")                                #Valida TI
        ti = (input("Ingrese el número de su documento de identidad"))
    
    for i in range(len(datos["user_nuevo"])):                                   #Recorre user_nuevo
        if datos ["user_nuevo"][i]["documento"]==ti:
            datos["user_nuevo"].pop(i)
            break
    for o in range(len(datos["user_regular"])):                                 #Recorre user_regular
        if datos ["user_regular"][o]["documento"]==ti:
            datos["user_regular"].pop(o)
            break
    for u in range(len(datos["user_leal"])):                                    #Recorre user_leal
        if datos ["user_leal"][u]["documento"]==ti:
            datos["user_leal"].pop(u)
            break
    #/////////////////////////////////////////////////////////////////////////////////////////////////////    
    print("¡Usuario eliminado exitosamente!")
    return datos

def actualizar_user(datos):
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    ti = (input("Ingrese el número de su documento de identidad"))                                        #lee T-I

    while len(ti)!=10:
        print("Documento de identidad inválido")                                                          #Valida T.I
        ti = (input("Ingrese el número de su documento de identidad"))
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    for i in range(len(datos["user_nuevo"])):                                                             #Recorre User_nuevo
        if datos ["user_nuevo"][i]["documento"]==ti:                                                      #Valida si la TI esta en nuevos
            menu_act()
            opc = pedir_opc()
            if opc == 1:
                datos["user_nuevo"][i]["nombre"]=input("Ingrese nuevo nombre").lower()
                print("---------------------------------")
                print("¡Nombre actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 2:
                ti = datos["user_nuevo"][i]["documento"]=input("Ingrese su nuevo documento de identidad")    
                while len(ti)!=10:                                                                        #Valida TI
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("Documento de identidad invalido")
                    datos["user_nuevo"][i]["documento"]=input("Ingrese su nuevo documento de identidad")     #Actualiza Ti
                    break
                print("---------------------------------")
                print("¡Documento actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 3:
                datos["user_nuevo"][i]["direccion"]=input("Ingrese nueva dirección")                      #Actualiza Direccion
                print("---------------------------------")
                print("¡Dirección actualizada exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 4:
                datos["user_nuevo"][i]["numtelefono"]=input("Ingrese nuevo numero de teléfono")
                while len(tel) != 10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("Número telefonico invalido")                                                   #Valida TEL
                    tel = datos["user_nuevo"][i]["numtelefono"]= input("Ingrese su número de teléfono")    #Actualiza NumTel
                print("---------------------------------")
                print("¡Teléfono actualizado exitosamente!")                                                   
                print("---------------------------------")
            break
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    for o in range(len(datos["user_regular"])):
        if datos ["user_regular"][o]["documento"]==ti:
            menu_act()
            opc = pedir_opc()
            if opc == 1:
                datos["user_regular"][o]["nombre"]=str(input("Ingrese su nuevo nombre")).lower()
                print("---------------------------------")
                print("¡Nombre actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 2:
                ti = datos["user_regular"][o]["documento"]=input("Ingrese su nuevo documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("Documento de identidad invalido")
                    datos["user_nuevo"][o]["documento"]=input("Ingrese su nuevo documento de identidad")
                    break
                print("---------------------------------")
                print("¡Documento actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 3:
                datos["user_regular"][o]["direccion"]=input("Ingrese su nueva dirección")
                print("---------------------------------")
                print("¡Dirección actualizada exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 4:
                datos["user_regular"][o]["numtelefono"]=input("Ingrese nuevo numero de teléfono")
                while len(tel) != 10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("Número telefonico invalido")                                                   
                    tel = datos["user_regular"][i]["numtelefono"]= input("Ingrese su número de teléfono")
                print("---------------------------------")
                print("¡Teléfono actualizado exitosamente!")                                                   
                print("---------------------------------")
            break
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    for u in range(len(datos["user_leal"])):
        if datos ["user_leal"][u]["documento"]==ti:
            menu_act()
            opc = pedir_opc()
            if opc == 1:
                datos["user_leal"][u]["nombre"]=str(input("Ingrese nuevo nombre")).lower()
                print("---------------------------------")
                print("¡Nombre actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 2:
                ti = datos["user_leal"][u]["documento"]=input("Ingrese nuevo documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("Documento de identidad inválido")
                    datos["user_nuevo"][u]["documento"]=input("Ingrese nuevo documento de identidad")
                    break
                print("---------------------------------")
                print("¡Documento actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 3:
                datos["user_leal"][u]["direccion"]=input("Ingrese nueva dirección")
                print("---------------------------------")
                print("¡Dirección actualizado exitosamente!")                                                   
                print("---------------------------------")
            elif opc == 4:
                datos["user_leal"][u]["numtelefono"]=input("Ingrese nuevo numero de teléfono")
                while len(tel) != 10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("Número de teléfono inválido")                                                  
                    tel = datos["user_leal"][i]["numtelefono"]= input("Ingrese su número de teléfono")    
                print("---------------------------------")
                print("¡Númerotel cambiado exitosamente!")                                                   
                print("---------------------------------")
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    return datos

def crear_producto(datos):
    datos = dict(datos)
    prod={}
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    prod["nombre"]=input("Ingrese nombre del producto").lower()                            #Lee nombre
    prod["precio"]= float(input("Ingrese el precio del producto"))                         #lee precio
    prod["caracteristicas"]= input("Ingrese las características").lower()                 #Lee caracteristicas
    prod["bodega"]=int(input("¿Cuantas unidades hay disponibles?")) 
    prod["ventas"]=0                                                                       #Lee cantidad
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    categoria = input("¿Que tipo de producto es?--[celular]--[computador]--[televisor]-- ").lower()      #Lee categoria
    if categoria == "celular":
        datos["celular"].append(prod)                                                      #Agrega celular
        print("PRODUCTO creado con éxito!")
    elif categoria == "computador":
        datos["computador"].append(prod)                                                   #Agrega computador
        print("PRODUCTO creado con éxito!")
    elif categoria == "televisor":
        datos["televisor"].append(prod)                                                    #Agrega televisor
        print("PRODUCTO creado con éxito!")
    elif categoria != "celular" or "computador" or "televisor":
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")
        print("Categoría no disponible")
    return datos

def eliminar_producto(datos):
    datos = dict(datos)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    prodeliminar = str(input("Ingrese el nombre del producto que deseas eliminar")).lower()                                #Lee producto a eliminar
    categoria = str(input("¿Que tipo de producto es?--[celular]--[computador]--[televisor]-- ")).lower()           #Lee categoria
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    for i in range(len(datos[categoria])):                                                                         #Recorre la categoria
        if datos[categoria][i]["nombre"]==prodeliminar:
            datos[categoria].pop(i)                                                                                #Elimina el producto
            print("---------------------------------")
            print("¡Producto eliminado exitosamente!")
            print("---------------------------------")
        else:
            print("| | | | | | | | | ")
            print("v v v v v v v v v ")
            print("¡ERROR! Producto no encontrado")
            break
    return datos 

def crear_servicio(datos):
    
    datos = dict(datos)
    srv ={}
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    srv["nombre"]=input("Ingrese nombre del servicio que desea CREAR ").lower()                      #Lee nombre
    srv["precio"]= float(input("Ingrese el precio del producto "))                                   #Lee precio
    srv["gbytes"]= input("Ingrese las características del plan ")                                    #Lee gigabytes
    srv["bodega"]=int(input("¿Cuantos hay disponibles? "))                                           #lee cantidad
    categoria = input("Que tipo de servicio es?[hogar]--[fibraÓptica]--[pospago]--[prepago]").lower()    #Lee categoria
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    if categoria == "hogar":
        datos["hogar"].append(srv)                                                                  #Agrega a Hogar
        print("Plan hogar creado con éxito!")
    elif categoria == "fibraoptica":
        datos["fibraoptica"].append(srv)                                                            #Agrega a Fibra
        print("Plan fibra óptica con éxito!")
    elif categoria == "pospago":
        datos["pospago"].append(srv)                                                                #Agrega a Pospago
        print("Plan pospago creado con éxito!")
    elif categoria == "prepago":
        datos["prepago"].append(srv)                                                                #Agrega a prepago
        print("Plan prepago creado con éxito!")
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    return datos

def eliminar_servicio(datos):
    datos = dict(datos)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    prodeliminar = str(input("Ingrese el nombre del servicio que deseas eliminar")).lower()                     #Nombre a eliminar                                      
    categoria = str(input("Que tipo de servicio es?[hogar]--[fibraÓptica]--[pospago]--[prepago]").lower()).lower() #Lee Categoria
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    for i in range(len(datos[categoria])):                                                                      #Recorre la categoria
        if datos[categoria][i]["nombre"]==prodeliminar:
            datos[categoria].pop(i)                                                                             #Elimina el servicio
            print("---------------------------------")
            print("¡Servicio eliminado exitosamente!")
            print("---------------------------------")
        else:
            print("| | | | | | | | | ")
            print("v v v v v v v v v ")
            print("¡ERROR! Servicio no encontrado")
            break
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    return datos

def validar_us(datos):
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    ti = (input("Ingrese su número de documento "))              #Lee documento
    while len(ti) != 10:
        print("| | | | | | | | | ")
        print("v v v v v v v v v ")
        print("Documento de identidad inválido")                #Valida documento
        ti = (input("Ingrese su número de documento" ))
    for i in range(len(["user_nuevo"])):                        #Recorre User_nuevo
        if datos["user_nuevo"][i]["documento"]==ti:
            print("El usuario con número: "+ ti + "es Nuevo")
            break
    for o in range(len(["user_regular"])):                      #Recorre User_Regular
        if datos["user_regular"][o]["documento"]==ti:
           print("El usuario con número: "+ ti + "es Regular")
           break
    for u in range(len(["user_leal"])):                         #Recorre User_leal
        if datos["user_leal"][u]["documento"]==ti:
            print("El usuario con número: "+ ti + "es Leal")
            break
    #/////////////////////////////////////////////////////////////////////////////////////////////////////     

def compra_algo(datos):
    BASE_DATOS_USERS = "users.json"
    BASE_DATOS_PRODUCTOS = "productos.json"
    BASE_DATOS_SERVICIOS = "servicios.json"
    BASE_DATOS_VENTAS = "ventas.json"
    datosv = cargar_datos(BASE_DATOS_VENTAS)
    datoss = cargar_datos(BASE_DATOS_SERVICIOS)                 #CARGO BASES DE DATOS --> JSON
    datosp = cargar_datos(BASE_DATOS_PRODUCTOS)
    datosu = cargar_datos(BASE_DATOS_USERS)
    datos = dict(datosv)
    producto={}
    menu_prod()
    opc = pedir_opc()
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    if opc == 1:
        print("********************************************************")
        for p in range(len(datosp["celular"])):
            print(f"Nombre -->          {datosp["celular"][p]["nombre"]}")
            print(f"precio -->          {datosp["celular"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["celular"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datosp["celular"])):
            if datosp["celular"][i]["nombre"] == nombrep:
                producto["nombre"] = datosp["celular"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()  
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i=0
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opc == 2:
        print("********************************************************")
        for p in range(len(datosp["computador"])):
            print(f"Nombre -->          {datosp["computador"][p]["nombre"]}")
            print(f"precio -->          {datosp["computador"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["computador"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datosp["computador"])):
            if datosp["computador"][i]["nombre"] == nombrep:
                producto["nombre"] = datosp["computador"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opc == 3:
        print("********************************************************")
        for p in range(len(datosp["televisor"])):
            print(f"Nombre -->          {datosp["televisor"][p]["nombre"]}")
            print(f"precio -->          {datosp["televisor"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["televisor"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datosp["televisor"])):
            if datosp["televisor"][i]["nombre"] == nombrep:
                producto["nombre"] = datosp["televisor"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        print("¡COMPRA EXITOSA!")
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opc == 4:
        print("********************************************************")
        for p in range(len(datosp["hogar"])):
            print(f"Nombre -->          {datosp["hogar"][p]["nombre"]}")
            print(f"precio -->          {datosp["hogar"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["hogar"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datoss["hogar"])):
            if datoss["hogar"][i]["nombre"] == nombrep:
                producto["nombre"] = datoss["hogar"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datoss["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opc == 5:
        print("********************************************************")
        for p in range(len(datosp["fibraoptica"])):
            print(f"Nombre -->          {datosp["fibraoptica"][p]["nombre"]}")
            print(f"precio -->          {datosp["fibraoptica"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["fibraoptica"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datoss["fibraoptica"])):
            if datoss["fibraoptica"][i]["nombre"] == nombrep:
                producto["nombre"] = datoss["fibraoptica"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datoss["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opc == 6:
        print("********************************************************")
        for p in range(len(datosp["pospago"])):
            print(f"Nombre -->          {datosp["pospago"][p]["nombre"]}")
            print(f"precio -->          {datosp["pospago"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["pospago"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datoss["pospago"])):
            if datoss["pospago"][i]["nombre"] == nombrep:
                producto["nombre"] = datoss["pospago"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datoss["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
            
    #////////////////////////////////////////////////////////////////////////////////////////////////////
    elif opc == 7:
        print("********************************************************")
        for p in range(len(datosp["prepago"])):
            print(f"Nombre -->          {datosp["prepago"][p]["nombre"]}")
            print(f"precio -->          {datosp["prepago"][p]["precio"]}")
            print(f"Caracteristicas --> {datosp["prepago"][p]["caracteristicas"]}")
            print("********************************************************")
        nombrep = input("Ingrese el nombre del producto a comprar").lower()
        for i in range(len(datoss["prepago"])):
            if datoss["prepago"][i]["nombre"] == nombrep:
                producto["nombre"] = datoss["prepago"][i]["nombre"]
                ti = input("Ingrese su documento de identidad")
                while len(ti)!=10:
                    print("| | | | | | | | | ")
                    print("v v v v v v v v v ")
                    print("¡Documento inválido!")
                    ti = input("Ingrese su documento de identidad").lower()
                for u in range(len(datosu["user_nuevo"])):
                    if datosu["user_nuevo"][u]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datoss["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_regular"])):
                    if datosu["user_regular"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        print("¡COMPRA EXITOSA!")
    else:
        print("ERROR DIGITADO")        
    return datos