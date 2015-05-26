import os
#-------------------------------------------------proceso-importante-----------------------------------------------------------------------------
def Proceso_ingresar_archivo_a_lista_de_archivos(Nombre_documento):
    Documento_escribir=open("[Guardar_datos_de_documentos].txt","a")
    Nombre_documento+="\n"
    Documento_escribir.write(Nombre_documento)
    Documento_escribir.close()

"""_________________________________________________________encriptar_________________________________________________________________"""
def Formula_encriptar_caracter(Caracter,Caracter_a_comparar,Valor_caracter,):
    if Caracter==Caracter_a_comparar:
        return(Valor_caracter)
    else:
        return("")

def Encriptar_caracter(Caracter):
    Palabra=""
    Palabra1=""
    #A
    F_1_1=Formula_encriptar_caracter(Caracter,"A","☺")
    F_1_2=Formula_encriptar_caracter(Caracter,"a","☻")
    F_1_3=Formula_encriptar_caracter(Caracter,"á","♥")
    F_1_4=Formula_encriptar_caracter(Caracter,"ä","♦")
    #B
    F_2_1=Formula_encriptar_caracter(Caracter,"B","♣")
    F_2_2=Formula_encriptar_caracter(Caracter,"b","♠")
    #C
    F_3_1=Formula_encriptar_caracter(Caracter,"C","•")
    F_3_2=Formula_encriptar_caracter(Caracter,"c","◘")
    #D
    F_4_1=Formula_encriptar_caracter(Caracter,"D","○")
    F_4_2=Formula_encriptar_caracter(Caracter,"d","◙")
    #E
    F_5_1=Formula_encriptar_caracter(Caracter,"E","♂")
    F_5_2=Formula_encriptar_caracter(Caracter,"e","♀")
    F_5_3=Formula_encriptar_caracter(Caracter,"é","♪")
    F_5_4=Formula_encriptar_caracter(Caracter,"ë","♫")
    #F
    F_6_1=Formula_encriptar_caracter(Caracter,"F","☼")
    F_6_2=Formula_encriptar_caracter(Caracter,"f","►")
    #G
    F_7_1=Formula_encriptar_caracter(Caracter,"G","◄")
    F_7_2=Formula_encriptar_caracter(Caracter,"g","↕")
    #H
    F_8_1=Formula_encriptar_caracter(Caracter,"H","‼")
    F_8_2=Formula_encriptar_caracter(Caracter,"h","¶")
    #I
    F_9_1=Formula_encriptar_caracter(Caracter,"I","§")
    F_9_2=Formula_encriptar_caracter(Caracter,"i","▬")
    F_9_3=Formula_encriptar_caracter(Caracter,"í","↨")
    F_9_4=Formula_encriptar_caracter(Caracter,"ï","↑")
    #J
    F_10_1=Formula_encriptar_caracter(Caracter,"J","↓")
    F_10_2=Formula_encriptar_caracter(Caracter,"j","→")
    #K
    F_11_1=Formula_encriptar_caracter(Caracter,"K","←")
    F_11_2=Formula_encriptar_caracter(Caracter,"k","∟")
    #L
    F_12_1=Formula_encriptar_caracter(Caracter,"L","↔")
    F_12_2=Formula_encriptar_caracter(Caracter,"l","▲")
    #M
    F_13_1=Formula_encriptar_caracter(Caracter,"M","▼")
    F_13_2=Formula_encriptar_caracter(Caracter,"m","▲")
    #N
    F_14_1=Formula_encriptar_caracter(Caracter,"N","!")
    F_14_2=Formula_encriptar_caracter(Caracter,"n","└")
    #Ñ
    F_15_1=Formula_encriptar_caracter(Caracter,"Ñ","#")
    F_15_2=Formula_encriptar_caracter(Caracter,"ñ","$")
    #O
    F_16_1=Formula_encriptar_caracter(Caracter,"O","%")
    F_16_2=Formula_encriptar_caracter(Caracter,"o","&")
    F_16_3=Formula_encriptar_caracter(Caracter,"ó","/")
    F_16_4=Formula_encriptar_caracter(Caracter,"ö","(")
    #P
    F_17_1=Formula_encriptar_caracter(Caracter,"P",")")
    F_17_2=Formula_encriptar_caracter(Caracter,"p","=")
    #Q
    F_18_1=Formula_encriptar_caracter(Caracter,"Q","?")
    F_18_2=Formula_encriptar_caracter(Caracter,"q","¡")
    #R
    F_19_1=Formula_encriptar_caracter(Caracter,"R","¨")
    F_19_2=Formula_encriptar_caracter(Caracter,"r","*")
    #S
    F_20_1=Formula_encriptar_caracter(Caracter,"S","[")
    F_20_2=Formula_encriptar_caracter(Caracter,"s","]")
    #T
    F_21_1=Formula_encriptar_caracter(Caracter,"T","´")
    F_21_2=Formula_encriptar_caracter(Caracter,"t","+")
    #U
    F_22_1=Formula_encriptar_caracter(Caracter,"U","{")
    F_22_2=Formula_encriptar_caracter(Caracter,"u","}")
    F_22_3=Formula_encriptar_caracter(Caracter,"ú","░")
    F_22_4=Formula_encriptar_caracter(Caracter,"ü","▒")
    #V
    F_23_1=Formula_encriptar_caracter(Caracter,"V","▓")
    F_23_2=Formula_encriptar_caracter(Caracter,"v","┤")
    #W
    F_24_1=Formula_encriptar_caracter(Caracter,"W","├")
    F_24_2=Formula_encriptar_caracter(Caracter,"w","┼")
    #X
    F_25_1=Formula_encriptar_caracter(Caracter,"X","╣")
    F_25_2=Formula_encriptar_caracter(Caracter,"x","╗")
    #Y
    F_26_1=Formula_encriptar_caracter(Caracter,"Y","╝")
    F_26_2=Formula_encriptar_caracter(Caracter,"y","┴")
    #Z
    F_27_1=Formula_encriptar_caracter(Caracter,"Z","©")
    F_27_2=Formula_encriptar_caracter(Caracter,"z","║")

    Palabra+=F_1_1+F_1_2+F_1_3+F_1_4+F_2_1+F_2_2+F_3_1+F_3_2+F_4_1+F_4_2+F_5_1+F_5_2+F_5_3+F_5_4+F_6_1+F_6_2+F_7_1+F_7_2+F_8_1+F_8_2+F_9_1+F_9_2+F_9_3+F_9_4+F_10_1+F_10_2+F_11_1+F_11_2+F_12_1+F_12_2+F_13_1+F_13_2+F_14_1+F_14_2+F_15_1+F_15_2+F_16_1+F_16_2+F_16_3+F_16_4+F_17_1+F_17_2+F_18_1+F_18_2+F_19_1+F_19_2+F_20_1+F_20_2+F_21_1+F_21_2+F_22_1+F_22_2+F_22_3+F_22_4+F_23_1+F_23_2+F_24_1+F_24_2+F_25_1+F_25_2+F_26_1+F_26_2+F_27_1+F_27_2
    return(Palabra)

def Proceso_generar_lista_de_encriptar(Nombre_documento):
    Nombre_documento+=".txt"
    Pregunta_existencia_de_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    if Pregunta_existencia_de_archivo1=="si hay":
        Documento=open(Nombre_documento,"r")
        Lineas=Documento.readlines()
        Lista_de_palabras_a_encriptar=[]
        for L in Lineas:
            Lista_de_palabras_a_encriptar.append(L)
        Documento.close()
        return(Lista_de_palabras_a_encriptar)
    else:
        print("El documento que desea encriptar no existe")

def Proceso_encriptar_documento_(Lista_de_comando2):
    Palabra_encriptada_caracter_por_caracter=""
    Nombre_documento=Lista_de_comando2[2]
    Lista_de_palabras_a_encriptar=Proceso_generar_lista_de_encriptar(Nombre_documento)
    print(Lista_de_palabras_a_encriptar)
    for Palabra in Lista_de_palabras_a_encriptar:
        for Caracter in Palabra:
            Palabra_encriptada_caracter_por_caracter+=Encriptar_caracter(Caracter)
        Palabra_encriptada_caracter_por_caracter+="ð"
    print(Palabra_encriptada_caracter_por_caracter)

#---------------------------------------------------------proceso1----------------------------------------------------------------------------------

def Analizar_existencia_de_archivo(Nombre_documento):
    try:
        Documento=open(Nombre_documento,"r")
        Documento.close()
        return("si hay")
    except:
        return("no hay")

def Proceso_cambiar_nombre_de_la_lista_de_archivos(Nombre_documento_original,Nombre_documento_nuevo):
    Nombre_documento_original+="\n"
    Nombre_documento_nuevo+="\n"
    Lista_de_los_nombres_de_archivos=[]
    Lista_de_los_nombres_de_archivos.append(Nombre_documento_nuevo)
    Documento=open("[Guardar_datos_de_documentos].txt","r")
    Lineas=Documento.readlines()
    for L in Lineas:
        if L!=Nombre_documento_original:
            Lista_de_los_nombres_de_archivos.append(L)
    Documento.close()
    Documento=open("[Guardar_datos_de_documentos].txt","w")
    for L in Lista_de_los_nombres_de_archivos:
        Nombre_archivo=L
        Nombre_archivo+="\n"
        Documento.write(L)
    Documento.close()

def Proceso_eliminar_nombre_de_la_lista_de_archivos(Nombre_documento):
    Nombre_documento+="\n"
    Lista_de_los_nombres_de_archivos=[]
    Documento=open("[Guardar_datos_de_documentos].txt","r")
    Lineas=Documento.readlines()
    for L in Lineas:
        if L!=Nombre_documento:
            Lista_de_los_nombres_de_archivos.append(L)
    Documento.close()
    Documento=open("[Guardar_datos_de_documentos].txt","w")
    for L in Lista_de_los_nombres_de_archivos:
        Nombre_archivo=L
        Nombre_archivo+="\n"
        Documento.write(L)
    Documento.close()
    
#------------------------------------------proceso2-----------------------------------------------------------------------------------------------------

#Bloqueo_proceso_documento2 =si el usuario toma la desicion de "cambiar nombre" el bloqueo se desbloquea debido a que el proceso se debe repetir hasta "Pregunta_inicial2=str(input(""))"
#Pregunta_crear_archivo1=cuando no exista el archivo con el mismo nombre digitado se realiza el procedimiento de crear archivo.
#Pregunta_crear_archivo2= cuando el usurio tome la desicion de sobrescribir se realiza el procedimiento de crear archivo.

#_____________________desicion_crear_documento____________________________________________________________________
def Proceso_crear_archivo(Bloqueo_proceso_documento1,Lista_de_comando2,Pregunta_crear_archivo2):
    Nombre_documento=Lista_de_comando2[2]
    print("Creando archivo de nombre",Nombre_documento,"...")
    Nombre_documento+=".txt"
    Pregunta_crear_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    Bloqueo_proceso_documento2="bloqueado"
    while Bloqueo_proceso_documento2=="bloqueado":
            if Pregunta_crear_archivo1=="no hay" or Pregunta_crear_archivo2=="si sobrescribir":
                Documento=open(Nombre_documento,"w")
                Documento.close()
                Bloqueo_proceso_documento2="desbloqueado"
                Proceso_ingresar_archivo_a_lista_de_archivos(Nombre_documento)
                print("¡Finalizado!")
            else:
                print("Ya existe un archivo con ese nombre ¿que desea hacer?")
                print("""*Cambiar(Digitar otro nombre para su archivo)
o
*sobrescribir(Borrar archivo anterior y remplazarlo por uno en blanco actual)""")
                Desicion_escribir_cambiar_nombre_archivo=str(input(""))
                Lista_de_desicion1=Desicion_escribir_cambiar_nombre_archivo.split(" ")
                if Lista_de_desicion1[0]=="cambiar":
                    print("Cambiando...")
                    Bloqueo_proceso_documento2="desbloqueado"
                if Lista_de_desicion1[0]=="sobrescribir":
                    print("El archivo a sido sobrescrito")
                    Pregunta_crear_archivo2="si sobrescribir"

def Proceso_borrar_archivo(Lista_de_comando2):
    Nombre_documento=Lista_de_comando2[2]
    if Nombre_documento=="[Guardar_datos_de_documentos]":
        print("No se permite borrar este documento")
    if Nombre_documento!="[Guardar_datos_de_documentos]":
        Nombre_documento+=".txt"
        Pregunta_borrar_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
        if Pregunta_borrar_archivo1=="si hay":
            os.remove(Nombre_documento)
            Proceso_eliminar_nombre_de_la_lista_de_archivos(Nombre_documento)
            print("¡Finalizado!")
        else:
            print("El documento que desea borrar no existe")

def Proceso_renombrar_archivo(Lista_de_comando2):
    Nombre_documento_original=Lista_de_comando2[2]
    Nombre_documento_nuevo=Lista_de_comando2[4]
    if Nombre_documento_original=="[Guardar_datos_de_documentos]":
        print("No se permite borrar este documento")
    if Nombre_documento_original!="[Guardar_datos_de_documentos]":
        print("renombrando documento",Nombre_documento_original,"a",Nombre_documento_nuevo,"...")
        Nombre_documento_original+=".txt"
        Nombre_documento_nuevo+=".txt"
        Pregunta_renombrar_archivo1=Analizar_existencia_de_archivo(Nombre_documento_original)
        if Pregunta_renombrar_archivo1=="si hay":
            os.rename(Nombre_documento_original,Nombre_documento_nuevo)
            Proceso_cambiar_nombre_de_la_lista_de_archivos(Nombre_documento_original,Nombre_documento_nuevo)
            print("¡Finalizado!")
        else:
            print("El documento que desea renombrar no existe")

#Bloqueo1_proceso_renombrar_archivo= este bloqueo se desbloquea cuando el usurio no digite el comando de ayuda
#Bloqueo2_proceso_renombrar_archivo= este bloqueo se desbloquea cuando hay un archivo ya que se puede escribir en ese archivo y se bloquea cuando no se encuentra el archivo

def Proceso_escribir_en_archivo(Lista_de_comando2):
    Nombre_documento=Lista_de_comando2[3]
    print("Escribiendo en el documento",Nombre_documento,"...")
    Nombre_documento+=".txt"
    Bloqueo1_proceso_renombrar_archivo="bloqueado"
    Pregunta_escribir_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    if Pregunta_escribir_archivo1=="si hay":
        Bloqueo2_proceso_renombrar_archivo="desbloqueado"
    else:
        print("El documento en el que desea escribir no existe")
        Bloqueo2_proceso_renombrar_archivo="bloqueado"
    
    while Bloqueo1_proceso_renombrar_archivo=="bloqueado" and Bloqueo2_proceso_renombrar_archivo=="desbloqueado":
        Dictado=str(input(""))
        if Dictado=="salir":
            Bloqueo1_proceso_renombrar_archivo="desbloqueado"
            print("¡Finalizado!")
        if Dictado=="ayuda":
            print("Actualmente usted se encuentra realizando el proceso de escritura del archivo",Nombre_documento,"""
Comandos Actuales:
*salir""")
        if Dictado!="salir" and Dictado!="ayuda":
            Dictado+="\n"
            Documento_escribir=open(Nombre_documento,"a")
            Documento_escribir.write(Dictado)
            Documento_escribir.close()

def Proceso_leer_archivo(Lista_de_comando2):
    Nombre_documento=Lista_de_comando2[2]
    Nombre_documento+=".txt"
    Pregunta_leer_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    if Pregunta_leer_archivo1=="si hay":
        Documento=open(Nombre_documento,"r")
        Lineas=Documento.readlines()
        for L in Lineas:
            print(L)
        Documento.close()
    else:
        print("El documento que desea borrar no existe")

def Proceso_mostrar_archivos_actuales(Lista_de_comando2):
    Documento=open("[Guardar_datos_de_documentos].txt","r")
    Lineas=Documento.readlines()
    if Lineas==[]:
        print("No existen ningun archivo")
    for L in Lineas:
        print(L)
        Documento.close()

#Bloqueo1_proceso_documento1 = si el usuario digita el comando salir el "Bloqueo1_proceso_documento1 se desbloquea".

#__________________________________________menu_documento______________________________________
def Proceso_documento():
    Bloqueo_proceso_documento1="bloqueado"
    Pregunta_crear_archivo2="no sobrescribir"
    while Bloqueo_proceso_documento1=="bloqueado":
        Pregunta_inicial2=str(input(""))
        Lista_de_comando2=Pregunta_inicial2.split(" ")
        if Lista_de_comando2[0]=="ayuda":
            print("""Actualmente usted se encuentra en el menu de documentos.
Comandos Actuales:
*Crear documento "ejemplo(data)"
*Borrar documento "ejemplo(data)"
*Renombrar documento "ejemplo(data)" a "ejemplo(save)"
*Escribir en documento "ejemplo(data)"
*Leer documento "ejemplo(data)"
*Nombres de documentos actuales
"Encriptar documento "ejemplo(data)""
*Salir""")
        if Lista_de_comando2[0]=="salir":
            Bloqueo_proceso_documento1="desbloqueado"
            print("Finalizado")
        try:
            if Lista_de_comando2[0]=="crear" and Lista_de_comando2[1]=="documento" and Lista_de_comando2[2]!=[]:
                Proceso_crear_archivo(Bloqueo_proceso_documento1,Lista_de_comando2,Pregunta_crear_archivo2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="borrar" and Lista_de_comando2[1]=="documento" and Lista_de_comando2[2]!=[]:
                Proceso_borrar_archivo(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="renombrar" and Lista_de_comando2[1]=="documento" and Lista_de_comando2[2]!=[] and Lista_de_comando2[3]=="a" and Lista_de_comando2[4]!=[]:
                Proceso_renombrar_archivo(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="escribir" and Lista_de_comando2[1]=="en" and Lista_de_comando2[2]=="documento" and Lista_de_comando2[3]!=[]:
                Proceso_escribir_en_archivo(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="leer" and Lista_de_comando2[1]=="documento" and Lista_de_comando2[2]!=[]:
                Proceso_leer_archivo(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="nombres" and Lista_de_comando2[1]=="de" and Lista_de_comando2[2]=="documentos" and Lista_de_comando2[3]=="actuales":
                Proceso_mostrar_archivos_actuales(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="encriptar" and Lista_de_comando2[1]=="documento" and Lista_de_comando2[2]!=[]:
                Proceso_encriptar_documento_(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")

#_________________________menu_principal________________________________________________________________________

#Bloqueo1 = estara bloqueado siempre y cuando el usurio no digite "finalizar"
#Proceso Principal
Bloqueo1="bloqueado"
while Bloqueo1=="bloqueado":
    Pregunta_inicial1=str(input(""))
    Lista_de_comando1=Pregunta_inicial1.split(" ")
    if Lista_de_comando1[0]=="ayuda":
        print("""Actualmento usted se encuentra en el menu general.
Comandos:
*Documento
*Cita
*Finalizar""")
    if Lista_de_comando1[0]=="finalizar":
        Bloqueo1="desbloqueado"
        print("El Programa ha sido cerrado")
    if Lista_de_comando1[0]=="documento":
        Proceso_documento()
    if Lista_de_comando1[0]=="cita":
        print("Crear Cita")

