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
    print("Creando archivo de nombre...",Nombre_documento)
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
*Salir""")
        if Lista_de_comando2[0]=="salir":
            Bloqueo_proceso_documento1="desbloqueado"
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

#Bloqueo1 = estara bloqueado siempre y cuando el usurio no digite "finalizar"
#Proceso Principal
Bloqueo1="bloqueado"
while Bloqueo1=="bloqueado":
    Pregunta_inicial1=str(input(""))
    Lista_de_comando1=Pregunta_inicial1.split(" ")
    if Lista_de_comando1[0]=="ayuda":
        print("""Actualmento usted se encuentra en el menu general.
Comandos:
*Documento:
-Nombre
-Borrar
-Salir
*Cita
*Finalizar""")
    if Lista_de_comando1[0]=="finalizar":
        Bloqueo1="desbloqueado"
    if Lista_de_comando1[0]=="documento":
        Proceso_documento()
    if Lista_de_comando1[0]=="cita":
        print("Crear Cita")

