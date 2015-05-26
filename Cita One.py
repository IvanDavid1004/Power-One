import os

def Analizar_existencia_de_archivo(Nombre_documento):
    try:
        Documento=open(Nombre_documento,"r")
        Documento.close()
        return("si hay")
    except:
        return("no hay")

#Bloqueo_proceso_documento2 =si el usuario toma la desicion de "cambiar nombre" el bloqueo se desbloquea debido a que el proceso se debe repetir hasta "Pregunta_inicial2=str(input(""))"
#Pregunta_crear_archivo1=cuando no exista el archivo con el mismo nombre digitado se realiza el procedimiento de crear archivo.
#Pregunta_crear_archivo2= cuando el usurio tome la desicion de sobrescribir se realiza el procedimiento de crear archivo.

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
    Nombre_documento+=".txt"
    Pregunta_borrar_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    if Pregunta_borrar_archivo1=="si hay":
        os.remove(Nombre_documento)
        print("¡Finalizado!")
    else:
        print("El documento que desea borrar no existe")

def Proceso_renombrar_archivo(Lista_de_comando2):
    Nombre_documento_original=Lista_de_comando2[2]
    Nombre_documento_nuevo=Lista_de_comando2[4]
    print("renombrando documento",Nombre_documento_original,"a",Nombre_documento_nuevo,"...")
    Nombre_documento_original+=".txt"
    Nombre_documento_nuevo+=".txt"
    Pregunta_renombrar_archivo1=Analizar_existencia_de_archivo(Nombre_documento_original)
    if Pregunta_renombrar_archivo1=="si hay":
        os.rename(Nombre_documento_original,Nombre_documento_nuevo)
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
        else:
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

#Bloqueo1_proceso_documento1 = si el usuario digita el comando salir el "Bloqueo1_proceso_documento1 se desbloquea".

def Proceso_documento():
    Bloqueo_proceso_documento1="bloqueado"
    Pregunta_crear_archivo2="no sobrescribir"
    while Bloqueo_proceso_documento1=="bloqueado":
        Pregunta_inicial2=str(input(""))
        Lista_de_comando2=Pregunta_inicial2.split(" ")
        if Lista_de_comando2[0]=="ayuda":
            print("""Actualmente usted se encuentra en el menu de archivos.
Comandos Actuales:
*Crear documento "ejemplo(data)"
*Borrar documento "ejemplo(data)"
*Renombrar documento "ejemplo(data)" a "ejemplo(save)"
*Escribir en documento "ejemplo(data)"
*Leer documento "ejemplo(data)"
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

