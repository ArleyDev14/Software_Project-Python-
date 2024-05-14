from menu import *
from datos import*

def crear_user_admin(datos):
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    datos = dict(datos)
    user={}
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        user["nombre"]=input("Ingrese su nombre completo").lower()                              #Lee NOMBRE
        ti = user["documento"]= (input("Ingrese el número de documento de identidad"))          #lee T.I
        while len(ti)!=10:                        
            print("| | | | | | | | | ")
            print("v v v v v v v v v ")                                              
            print("Documento de identidad inválido")                                            #VALIDA T.I
            ti = user["documento"]= (input("Ingrese el número de documento de identidad"))
        user["direccion"]= input("Ingrese su dirección").lower()                                #Lee DIRECCIÓN
        tel = user["numtelefono"]= (input("Ingrese su número de teléfono"))
        while len(tel) != 10:
            print("| | | | | | | | | ")
            print("v v v v v v v v v ")
            print("Número telefonico inválido")                                                 #VALIDA TEL
            tel = user["numtelefono"]= (input("Ingrese su número de teléfono")) 

        categoria = input ("Ingrese categoría a dar [Nuevo][Regular][Leal]").lower()            #Lee Categoria
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
    except Exception as e:
        log_error(e)
    return datos

def crear_user_cliente(datos):
    datos = dict(datos)
    user = {}

    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
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
    except Exception as e:
        log_error(e)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    return datos
    
def eliminar_user(datos):
    datos = dict(datos)
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        modus = False
        ti = (input("Ingrese el número de su documento de identidad"))              #Lee T.I
        while modus == False:
            while len(ti)!=10:
                print("Documento de identidad inválido")                                #Valida TI
                ti = (input("Ingrese el número de su documento de identidad"))
            
            for i in range(len(datos["user_nuevo"])):                                   #Recorre user_nuevo
                if datos ["user_nuevo"][i]["documento"]==ti:
                    datos["user_nuevo"].pop(i)
                    modus=True 
                    break
            for o in range(len(datos["user_regular"])):                                 #Recorre user_regular
                if datos ["user_regular"][o]["documento"]==ti:
                    datos["user_regular"].pop(o)
                    modus=True 
                    break
            for u in range(len(datos["user_leal"])):                                    #Recorre user_leal
                if datos ["user_leal"][u]["documento"]==ti:
                    datos["user_leal"].pop(u)
                    modus=True 
                    break
            if modus == False:
                print("| | | | | | | | | ")
                print("v v v v v v v v v ")
                print("Documento de identidad no encontrado")
                ti = (input("Ingrese el número de su documento de identidad"))
        print("---------------------------------")
        print("¡Usuario eliminado exitosamente!")
        print("---------------------------------")
        #/////////////////////////////////////////////////////////////////////////////////////////////////////    
    except Exception as e:
        log_error(e)
    return datos

def actualizar_user(datos):
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    try:
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
    except Exception as e:
        log_error(e)    
    return datos

def crear_producto(datos):
    datos = dict(datos)
    prod={}
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        prod["nombre"]=input("Ingrese nombre del producto").lower()                            #Lee nombre
        prod["precio"]= float(input("Ingrese el precio del producto"))                         #lee precio
        prod["caracteristicas"]= input("Ingrese las características").lower()                 #Lee caracteristicas
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
        mod = False
        categoria = input("¿Que tipo de producto es?--[celular]--[computador]--[televisor]-- ").lower()      #Lee categoria
        while mod == False:
            if categoria == "celular":
                datos["celular"].append(prod)                                                      #Agrega celular
                print("---------------------------------")
                print("Celular creado con éxito!")
                print("---------------------------------")
                mod = True
            elif categoria == "computador":
                datos["computador"].append(prod)                                                   #Agrega computador
                print("---------------------------------")
                print("Computador creado con éxito!")
                print("---------------------------------")
                mod = True
            elif categoria == "televisor":
                datos["televisor"].append(prod)                                                    #Agrega televisor
                print("---------------------------------")
                print("Televisor creado con éxito!")
                print("---------------------------------")
                mod = True
            elif mod == False:
                print("| | | | | | | | | ")
                print("v v v v v v v v v ")
                print("Categoría inválida")
                categoria = input("¿Que tipo de producto es?--[celular]--[computador]--[televisor]-- ").lower()
    except Exception as e:
        log_error(e)
    return datos

def eliminar_producto(datos):
    datos = dict(datos)
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:    
        modus=False                 
        categoria = str(input("¿Que tipo de producto es?--[celular]--[computador]--[televisor]-- ")).lower()           #Lee categoria
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
        while modus==False:
            if categoria != "celular" and "computador" and "televisor":
                print("| | | | | | | | | ")
                print("v v v v v v v v v ")
                print("Tipo de producto no encontrado")
                categoria = str(input("¿Que tipo de producto es?--[celular]--[computador]--[televisor]-- ")).lower()
            else:
                modus=True
        modus = False
        prodeliminar = str(input("Ingrese el nombre del producto que deseas eliminar")).lower()                            #Lee producto a eliminar
        while modus ==False:
            for i in range(len(datos[categoria])):                                                                         #Recorre la categoria
                if datos[categoria][i]["nombre"]==prodeliminar:
                    datos[categoria].pop(i)                                                                                #Elimina el producto
                    modus=True
            if modus == False:
                print("| | | | | | | | | ")
                print("v v v v v v v v v ")
                print("Producto no encontrado")
                prodeliminar = str(input("Ingrese el nombre del producto que deseas eliminar")).lower()
        print("---------------------------------")
        print("¡Producto eliminado exitosamente!")
        print("---------------------------------")
    except Exception as e:
        log_error(e)
    return datos 

def crear_servicio(datos):
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    datos = dict(datos)
    srv ={}
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        srv["nombre"]=input("Ingrese nombre del servicio que desea CREAR ").lower()                      #Lee nombre
        srv["precio"]= float(input("Ingrese el precio del producto "))                                   #Lee precio
        srv["gbytes"]= input("Ingrese las características del plan ")                                    #Lee gigabytes
        categoria = input("Que tipo de servicio es?[hogar]--[fibraÓptica]--[pospago]--[prepago]").lower() 
        while categoria != "hogar" and "fibraoptica" and "pospago" and "prepago":
            print("| | | | | | | | | ")
            print("v v v v v v v v v ")
            print("Tipo de servicio inválido")
            categoria = input("Que tipo de servicio es?[hogar]--[fibraÓptica]--[pospago]--[prepago]").lower()    #Lee categoria
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
        if categoria == "hogar":
            datos["hogar"].append(srv)                                                                  #Agrega a Hogar
            print("-----------------------------")
            print("¡Plan hogar creado con éxito!")
            print("-----------------------------")
        elif categoria == "fibraoptica":
            datos["fibraoptica"].append(srv)                                                            #Agrega a Fibra
            print("-----------------------------")
            print("¡Plan fibra óptica con éxito!")
            print("-----------------------------")
        elif categoria == "pospago":
            datos["pospago"].append(srv)                                                                #Agrega a Pospago
            print("-----------------------------")
            print("¡Plan pospago creado con éxito!")
            print("-----------------------------")
        elif categoria == "prepago":
            datos["prepago"].append(srv)                                                                #Agrega a prepago
            print("-----------------------------")
            print("¡Plan prepago creado con éxito!")
            print("-----------------------------")
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
    except Exception as e:
        log_error(e)
    return datos

def eliminar_servicio(datos):
    datos = dict(datos)
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        modus = False    
                             #Nombre a eliminar                                      
        categoria = str(input("Que tipo de servicio es?[hogar]--[fibraÓptica]--[pospago]--[prepago]").lower()) #Lee Categoria
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
        while categoria != "hogar" and "fibraoptica" and "pospago" and "prepago":
            print("| | | | | | | | | ")
            print("v v v v v v v v v ")
            print("¡Tipo de servicio no válido!")
            categoria = str(input("Que tipo de servicio es?[hogar]--[fibraÓptica]--[pospago]--[prepago]").lower())
        prodeliminar = str(input("Ingrese el nombre del servicio que deseas eliminar")).lower()
        while modus == False:
            for i in range(len(datos[categoria])):                                                                      #Recorre la categoria
                if datos[categoria][i]["nombre"]==prodeliminar:
                    datos[categoria].pop(i)
                    print("---------------------------------")
                    print("¡Servicio eliminado exitosamente!")
                    print("---------------------------------") 
                    modus = True
            if modus ==False:
                print("| | | | | | | | | ")
                print("v v v v v v v v v ")
                print("¡Servicio no encontrado!")
                prodeliminar = str(input("Ingrese el nombre del servicio que deseas eliminar")).lower()
                i=0
         
        #/////////////////////////////////////////////////////////////////////////////////////////////////////
    except Exception as e:
        log_error(e)
    return datos

def validar_us(datos):
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    try:
        modusuario = False
        while modusuario == False:    
            ti = (input("Ingrese su número de documento "))              #Lee documento
            while len(ti) != 10:
                print("| | | | | | | | | ")
                print("v v v v v v v v v ")
                print("Documento de identidad inválido")                #Valida documento
                ti = (input("Ingrese su número de documento" ))
            for i in range(len(["user_nuevo"])):                        #Recorre User_nuevo
                if datos["user_nuevo"][i]["documento"]==ti:
                    print("El usuario con número: "+ ti + "es Nuevo")
                    modusuario = True
                    break
            for o in range(len(["user_regular"])):                      #Recorre User_Regular
                if datos["user_regular"][o]["documento"]==ti:
                    print("El usuario con número: "+ ti + "es Regular")
                    modusuario = True
                    break
            for u in range(len(["user_leal"])):                         #Recorre User_leal
                if datos["user_leal"][u]["documento"]==ti:
                    print("El usuario con número: "+ ti + "es Leal")
                    modusuario = True
                    break
            if modusuario == False:
                print("No se ha encontrado este documento")
    except Exception as e:
        log_error(e)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////     

def compra_algo(datos):
    import traceback
    from datetime import datetime
    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)
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
    try:    
        menu_prod()
        opc = pedir_opc()
        #////////////////////////////////////////////////////////////////////////////////////////////////////        
        #////////////////////////////////////////////////////////////////////////////////////////////////////
        if opc == 1:
            moduser = False
            print("********************************************************")
            for p in range(len(datosp["celular"])):
                print(f"Nombre -->          {datosp["celular"][p]["nombre"]}")
                print(f"precio -->          {datosp["celular"][p]["precio"]}")
                print(f"Caracteristicas --> {datosp["celular"][p]["caracteristicas"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["productos"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    for i in range(len("celular")):
                        if  datosp["celular"][i]["nombre"] == nombrep:
                            break
                    while datosp["celular"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datosp["celular"][i]["nombre"]
                    print("¡Servicio comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        elif opc == 3:
            moduser = False
            print("********************************************************")
            for p in range(len(datosp["televisor"])):
                print(f"Nombre -->          {datosp["televisor"][p]["nombre"]}")
                print(f"precio -->          {datosp["televisor"][p]["precio"]}")
                print(f"Caracteristicas --> {datosp["televisor"][p]["caracteristicas"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["productos"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    for i in range(len("televisor")):
                        if  datosp["televisor"][i]["nombre"] == nombrep:
                            break
                    while datosp["televisor"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datosp["televisor"][i]["nombre"]
                    print("¡Producto comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        elif opc == 2:
            moduser = False
            print("********************************************************")
            for p in range(len(datosp["computador"])):
                print(f"Nombre -->          {datosp["computador"][p]["nombre"]}")
                print(f"precio -->          {datosp["computador"][p]["precio"]}")
                print(f"Caracteristicas --> {datosp["computador"][p]["caracteristicas"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["productos"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["productos"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    for i in range(len("computador")):
                        if  datosp["computador"][i]["nombre"] == nombrep:
                            break
                    while datosp["computador"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datosp["computador"][i]["nombre"]
                    print("¡Producto comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        elif opc == 4:
            moduser = False
            print("********************************************************")
            for p in range(len(datoss["hogar"])):
                print(f"Nombre -->          {datoss["hogar"][p]["nombre"]}")
                print(f"precio -->          {datoss["hogar"][p]["precio"]}")
                print(f"Caracteristicas --> {datoss["hogar"][p]["gbytes"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                    print("¡COMPRA EXITOSA!")
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["servicios"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    if  datoss["hogar"][i]["nombre"] == nombrep:
                            break
                    while datoss["hogar"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datoss["hogar"][i]["nombre"]
                    print("¡Servicio comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        elif opc == 5:
            moduser = False
            print("********************************************************")
            for p in range(len(datoss["fibraoptica"])):
                print(f"Nombre -->          {datoss["fibraoptica"][p]["nombre"]}")
                print(f"precio -->          {datoss["fibraoptica"][p]["precio"]}")
                print(f"Caracteristicas --> {datoss["fibraoptica"][p]["gbytes"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                    print("¡COMPRA EXITOSA!")
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["servicios"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    if  datoss["fibraoptica"][i]["nombre"] == nombrep:
                            break
                    while datoss["fibraoptica"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datoss["fibraoptica"][i]["nombre"]
                    print("¡Servicio comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        elif opc == 6:
            moduser = False
            print("********************************************************")
            for p in range(len(datoss["pospago"])):
                print(f"Nombre -->          {datoss["pospago"][p]["nombre"]}")
                print(f"precio -->          {datoss["pospago"][p]["precio"]}")
                print(f"Caracteristicas --> {datoss["pospago"][p]["gbytes"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                    print("¡COMPRA EXITOSA!")
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["servicios"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    if  datoss["pospago"][i]["nombre"] == nombrep:
                            break
                    while datoss["pospago"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datoss["pospago"][i]["nombre"]
                    print("¡Servicio comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        elif opc == 7:
            moduser = False
            print("********************************************************")
            for p in range(len(datoss["prepago"])):
                print(f"Nombre -->          {datoss["prepago"][p]["nombre"]}")
                print(f"precio -->          {datoss["prepago"][p]["precio"]}")
                print(f"Caracteristicas --> {datoss["prepago"][p]["gbytes"]}")
                print("********************************************************")
            nombrep = input("Ingrese el nombre del producto a comprar").lower()
            ti = (input("Ingrese su documento de identidad"))
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
                    moduser = True
                    print("¡COMPRA EXITOSA!")
                
                i = 0
            for i in range(len(datosu["user_regular"])):
                if datosu["user_regular"][i]["documento"]==ti:
                    producto["usuario"] = ti
                    cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                    producto["cantidad"] = cantidad
                    datosv["servicios"].append(producto)
                    moduser = True
                i = 0
                for i in range(len(datosu["user_leal"])):
                    if datosu["user_leal"][i]["documento"]==ti:
                        producto["usuario"] = ti
                        cantidad = int(input("Ingrese la cantidad de unidades que desea adquirir"))
                        producto["cantidad"] = cantidad
                        datosv["servicios"].append(producto)
                        moduser = True
                i = 0
                if moduser == True:
                    if  datoss["prepago"][i]["nombre"] == nombrep:
                            break
                    while datoss["prepago"][i]["nombre"] != nombrep:
                        print("Producto no encontrado")
                        nombrep = input("Ingrese el nombre del producto a comprar").lower()
                    producto["nombre"] = datoss["prepago"][i]["nombre"]
                    print("¡Servicio comprado con éxito!")
                else:
                    print("¡Usuario no encontrado!")
        #////////////////////////////////////////////////////////////////////////////////////////////////////   
    except Exception as e:
        log_error(e)     
    return datos

