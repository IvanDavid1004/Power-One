import os
#-------------------------------------------------proceso-importante-----------------------------------------------------------------------------
def Proceso_ingresar_archivo_a_lista_de_archivos(Nombre_documento):
    Documento_escribir=open("[Guardar_datos_de_documentos].txt","a")
    Nombre_documento+="\n"
    Documento_escribir.write(Nombre_documento)
    Documento_escribir.close()

def Evaluar_documentos_importantes(Nombre_documento):
    if Nombre_documento=="[Guardar_datos_de_documentos]":
        print("No se permite borrar este documento")
        return("si")
    if Nombre_documento=="[Datos_Citas]":
        print("No se permite borrar este documento")
        return("si")
    if Nombre_documento!="[Guardar_datos_de_documentos]" and Nombre_documento!="[Datos_Citas]":
        return("No es documento importante")

"""_________________________________________________________encriptar_________________________________________________________________"""
def Formula_encriptar_caracter(Caracter,Caracter_a_comparar,Valor_caracter):
    if Caracter==Caracter_a_comparar:
        return(Valor_caracter)
    else:
        return("")

def Encriptar_caracter(Caracter):
    Palabra=""
    #A
    F_1_1=Formula_encriptar_caracter(Caracter,"A","#$&%/°")
    F_1_2=Formula_encriptar_caracter(Caracter,"a","#$[°")
    F_1_3=Formula_encriptar_caracter(Caracter,"á","A$Y&H°")
    F_1_4=Formula_encriptar_caracter(Caracter,"ä","E%&_[°")
    #B
    F_2_1=Formula_encriptar_caracter(Caracter,"B","!*/y°")
    F_2_2=Formula_encriptar_caracter(Caracter,"b","f;:_#°")
    #C
    F_3_1=Formula_encriptar_caracter(Caracter,"C","@EF_°")
    F_3_2=Formula_encriptar_caracter(Caracter,"c","Z_%45°")
    #D
    F_4_1=Formula_encriptar_caracter(Caracter,"D","sf_B/57°")
    F_4_2=Formula_encriptar_caracter(Caracter,"d","FIMNG}{+´°")
    #E
    F_5_1=Formula_encriptar_caracter(Caracter,"E","see_e°")
    F_5_2=Formula_encriptar_caracter(Caracter,"e","#$RG[°")
    F_5_3=Formula_encriptar_caracter(Caracter,"é","DERG!°")
    F_5_4=Formula_encriptar_caracter(Caracter,"ë","DF_s°")
    #F
    F_6_1=Formula_encriptar_caracter(Caracter,"F","fr_$#&[°")
    F_6_2=Formula_encriptar_caracter(Caracter,"f","][*°")
    #G
    F_7_1=Formula_encriptar_caracter(Caracter,"G","ee_#$1A°")
    F_7_2=Formula_encriptar_caracter(Caracter,"g","deOrs_1°")
    #H
    F_8_1=Formula_encriptar_caracter(Caracter,"H","03_soww!°")
    F_8_2=Formula_encriptar_caracter(Caracter,"h","deg_24°")
    #I
    F_9_1=Formula_encriptar_caracter(Caracter,"I","%&%F[]°")
    F_9_2=Formula_encriptar_caracter(Caracter,"i","DQ_3°")
    F_9_3=Formula_encriptar_caracter(Caracter,"í","$%/[**¡\!°")
    F_9_4=Formula_encriptar_caracter(Caracter,"ï","o¨[°")
    #J
    F_10_1=Formula_encriptar_caracter(Caracter,"J","RTB_;#°")
    F_10_2=Formula_encriptar_caracter(Caracter,"j","987_AUSUS!°")
    #K
    F_11_1=Formula_encriptar_caracter(Caracter,"K","rwg_25=¨[*°")
    F_11_2=Formula_encriptar_caracter(Caracter,"k","12#°")
    #L
    F_12_1=Formula_encriptar_caracter(Caracter,"L","_$TQWTG/°")
    F_12_2=Formula_encriptar_caracter(Caracter,"l","wgerh[°")
    #M
    F_13_1=Formula_encriptar_caracter(Caracter,"M","qwe_[\[°")
    F_13_2=Formula_encriptar_caracter(Caracter,"m","erg%$/([=°")
    #N
    F_14_1=Formula_encriptar_caracter(Caracter,"N","_#U(#$%&°")
    F_14_2=Formula_encriptar_caracter(Caracter,"n","fdnFDF°")
    #Ñ
    F_15_1=Formula_encriptar_caracter(Caracter,"Ñ","!$tfs_GG[Ñ¨°")
    F_15_2=Formula_encriptar_caracter(Caracter,"ñ","%&(_SG_°")
    #O
    F_16_1=Formula_encriptar_caracter(Caracter,"O","varjh_1#%°")
    F_16_2=Formula_encriptar_caracter(Caracter,"o","AR_3457!$$°")
    F_16_3=Formula_encriptar_caracter(Caracter,"ó","[]*_:[[°")
    F_16_4=Formula_encriptar_caracter(Caracter,"ö","[[¨\¡*]°")
    #P
    F_17_1=Formula_encriptar_caracter(Caracter,"P","[¨\%&//°")
    F_17_2=Formula_encriptar_caracter(Caracter,"p","!#%/%$&[¨_:°")
    #Q
    F_18_1=Formula_encriptar_caracter(Caracter,"Q",")/&%&)[_:°")
    F_18_2=Formula_encriptar_caracter(Caracter,"q","¨[*]*%°")
    #R
    F_19_1=Formula_encriptar_caracter(Caracter,"R","[¨*][°")
    F_19_2=Formula_encriptar_caracter(Caracter,"r","a_RTH°")
    #S
    F_20_1=Formula_encriptar_caracter(Caracter,"S","wagr_WRG°")
    F_20_2=Formula_encriptar_caracter(Caracter,"s","awb_(o)%/°")
    #T
    F_21_1=Formula_encriptar_caracter(Caracter,"T","egbE_&/°")
    F_21_2=Formula_encriptar_caracter(Caracter,"t","ARHC_weg345°")
    #U
    F_22_1=Formula_encriptar_caracter(Caracter,"U","{\'\{°")
    F_22_2=Formula_encriptar_caracter(Caracter,"u","{+\'5g°")
    F_22_3=Formula_encriptar_caracter(Caracter,"ú","35wd°")
    F_22_4=Formula_encriptar_caracter(Caracter,"ü","CER&/04__:2°")
    #V
    F_23_1=Formula_encriptar_caracter(Caracter,"V","FWGR_[\[")
    F_23_2=Formula_encriptar_caracter(Caracter,"v","#$_&_&/°")
    #W
    F_24_1=Formula_encriptar_caracter(Caracter,"W","#$&hht_[°")
    F_24_2=Formula_encriptar_caracter(Caracter,"w","er_WEH¨_°")
    #X
    F_25_1=Formula_encriptar_caracter(Caracter,"X","rgrt$%&//((°")
    F_25_2=Formula_encriptar_caracter(Caracter,"x","%%&//([]:_°")
    #Y
    F_26_1=Formula_encriptar_caracter(Caracter,"Y","$#&&&/&%grj°")
    F_26_2=Formula_encriptar_caracter(Caracter,"y","ARNIOBG_[*°")
    #Z
    F_27_1=Formula_encriptar_caracter(Caracter,"Z","*{+{´°")
    F_27_2=Formula_encriptar_caracter(Caracter,"z","{+}´{+A°")
    #simbolos
    F_28_1=Formula_encriptar_caracter(Caracter,"?","*77´°")
    F_28_2=Formula_encriptar_caracter(Caracter,"¿","*ETG°")
    F_28_3=Formula_encriptar_caracter(Caracter,".","*YUIL°")
    F_28_4=Formula_encriptar_caracter(Caracter,",","*7AWRG3°")
    
    Palabra+=F_1_1+F_1_2+F_1_3+F_1_4+F_2_1+F_2_2+F_3_1+F_3_2+F_4_1+F_4_2+F_5_1+F_5_2+F_5_3+F_5_4+F_6_1+F_6_2+F_7_1+F_7_2+F_8_1+F_8_2+F_9_1+F_9_2+F_9_3+F_9_4+F_10_1+F_10_2+F_11_1+F_11_2+F_12_1+F_12_2+F_13_1+F_13_2+F_14_1+F_14_2+F_15_1+F_15_2+F_16_1+F_16_2+F_16_3+F_16_4+F_17_1+F_17_2+F_18_1+F_18_2+F_19_1+F_19_2+F_20_1+F_20_2+F_21_1+F_21_2+F_22_1+F_22_2+F_22_3+F_22_4+F_23_1+F_23_2+F_24_1+F_24_2+F_25_1+F_25_2+F_26_1+F_26_2+F_27_1+F_27_2+F_28_1+F_28_2+F_28_3+F_28_4
    return(Palabra)

def Proceso_generar_lista_de_encriptar(Nombre_documento):
    Pregunta_existencia_de_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    Documento=open(Nombre_documento,"r")
    Lineas=Documento.readlines()
    Lista_de_palabras_a_encriptar=[]
    for L in Lineas:
        Lista_de_palabras_a_encriptar.append(L)
    Documento.close()
    return(Lista_de_palabras_a_encriptar)

def Proceso_encriptar_documento(Lista_de_comando2):
    Palabra_encriptada_caracter_por_caracter=""
    Nombre_documento=Lista_de_comando2[2]
    Nombre_documento+=".txt"
    Pregunta_existencia_de_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
    if Pregunta_existencia_de_archivo1=="si hay":
        Lista_de_palabras_a_encriptar=Proceso_generar_lista_de_encriptar(Nombre_documento)
        if Lista_de_palabras_a_encriptar==[]:
            print("No contiene texto para encriptar")
        for Palabra in Lista_de_palabras_a_encriptar:
            for Caracter in Palabra:
                if Caracter=="\n":
                    Palabra_encriptada_caracter_por_caracter+="ç"
                if Caracter==" ":
                    Palabra_encriptada_caracter_por_caracter+="ð"
                if Caracter!="\n" and Caracter!=" ":
                    Palabra_encriptada_caracter_por_caracter+=Encriptar_caracter(Caracter)
        Nombre_documento_archivo=""
        for N in Nombre_documento:
            if N!="." and N!="t" and N!="x":
                Nombre_documento_archivo+=N
        Nombre_documento_archivo+="_encriptado.txt"
        Proceso_ingresar_archivo_a_lista_de_archivos(Nombre_documento_archivo)
        print("Documento encriptado en ",Nombre_documento_archivo)
        Documento=open(Nombre_documento_archivo,"w")
        Documento.write(Palabra_encriptada_caracter_por_caracter)
        Documento.close()
        print("¡Finalizado!")
    else:
        print("El documento que desea encriptar no existe")

"""_________________________________________________desencriptar_________________________________________________________________________________"""
def Ingresar_nombre_encriptado_o_desencriptado_a_la_lista(Nombre_documento):
    Documento=open("[Guardar_datos_de_documentos].txt","w")
    Documento.write(Nombre_documento)
    Documento.close()

def Formula_desencriptar_caracter(Caracter,Valor_caracter,Caracter_a_comparar):
    if Caracter==Caracter_a_comparar:
        return(Valor_caracter)
    else:
        return("")

def Desencriptar_caracter(Caracter):
    Palabra=""
    #A
    F_1_1=Formula_desencriptar_caracter(Caracter,"A","#$&%/")
    F_1_2=Formula_desencriptar_caracter(Caracter,"a","#$[")
    F_1_3=Formula_desencriptar_caracter(Caracter,"á","A$Y&H")
    F_1_4=Formula_desencriptar_caracter(Caracter,"ä","E%&_[")
    #B
    F_2_1=Formula_desencriptar_caracter(Caracter,"B","!*/y")
    F_2_2=Formula_desencriptar_caracter(Caracter,"b","f;:_#")
    #C
    F_3_1=Formula_desencriptar_caracter(Caracter,"C","@EF_")
    F_3_2=Formula_desencriptar_caracter(Caracter,"c","Z_%45")
    #D
    F_4_1=Formula_desencriptar_caracter(Caracter,"D","sf_B/57")
    F_4_2=Formula_desencriptar_caracter(Caracter,"d","FIMNG}{+´")
    #E
    F_5_1=Formula_desencriptar_caracter(Caracter,"E","see_e")
    F_5_2=Formula_desencriptar_caracter(Caracter,"e","#$RG[")
    F_5_3=Formula_desencriptar_caracter(Caracter,"é","DERG!")
    F_5_4=Formula_desencriptar_caracter(Caracter,"ë","DF_s")
    #F
    F_6_1=Formula_desencriptar_caracter(Caracter,"F","fr_$#&[")
    F_6_2=Formula_desencriptar_caracter(Caracter,"f","][*")
    #G
    F_7_1=Formula_desencriptar_caracter(Caracter,"G","ee_#$1A")
    F_7_2=Formula_desencriptar_caracter(Caracter,"g","deOrs_1")
    #H
    F_8_1=Formula_desencriptar_caracter(Caracter,"H","03_soww!")
    F_8_2=Formula_desencriptar_caracter(Caracter,"h","deg_24")
    #I
    F_9_1=Formula_desencriptar_caracter(Caracter,"I","%&%F[]")
    F_9_2=Formula_desencriptar_caracter(Caracter,"i","DQ_3")
    F_9_3=Formula_desencriptar_caracter(Caracter,"í","$%/[**¡\!")
    F_9_4=Formula_desencriptar_caracter(Caracter,"ï","o¨[")
    #J
    F_10_1=Formula_desencriptar_caracter(Caracter,"J","RTB_;#")
    F_10_2=Formula_desencriptar_caracter(Caracter,"j","987_AUSUS!")
    #K
    F_11_1=Formula_desencriptar_caracter(Caracter,"K","rwg_25=¨[*")
    F_11_2=Formula_desencriptar_caracter(Caracter,"k","12#")
    #L
    F_12_1=Formula_desencriptar_caracter(Caracter,"L","_$TQWTG/")
    F_12_2=Formula_desencriptar_caracter(Caracter,"l","wgerh[")
    #M
    F_13_1=Formula_desencriptar_caracter(Caracter,"M","qwe_[\[")
    F_13_2=Formula_desencriptar_caracter(Caracter,"m","erg%$/([=")
    #N
    F_14_1=Formula_desencriptar_caracter(Caracter,"N","_#U(#$%&")
    F_14_2=Formula_desencriptar_caracter(Caracter,"n","fdnFDF")
    #Ñ
    F_15_1=Formula_desencriptar_caracter(Caracter,"Ñ","!$tfs_GG[Ñ¨")
    F_15_2=Formula_desencriptar_caracter(Caracter,"ñ","%&(_SG_")
    #O
    F_16_1=Formula_desencriptar_caracter(Caracter,"O","varjh_1#%")
    F_16_2=Formula_desencriptar_caracter(Caracter,"o","AR_3457!$$")
    F_16_3=Formula_desencriptar_caracter(Caracter,"ó","[]*_:[[")
    F_16_4=Formula_desencriptar_caracter(Caracter,"ö","[[¨\¡*]")
    #P
    F_17_1=Formula_desencriptar_caracter(Caracter,"P","[¨\%&//")
    F_17_2=Formula_desencriptar_caracter(Caracter,"p","!#%/%$&[¨_:")
    #Q
    F_18_1=Formula_desencriptar_caracter(Caracter,"Q",")/&%&)[_:")
    F_18_2=Formula_desencriptar_caracter(Caracter,"q","¨[*]*%")
    #R
    F_19_1=Formula_desencriptar_caracter(Caracter,"R","[¨*][")
    F_19_2=Formula_desencriptar_caracter(Caracter,"r","a_RTH")
    #S
    F_20_1=Formula_desencriptar_caracter(Caracter,"S","wagr_WRG")
    F_20_2=Formula_desencriptar_caracter(Caracter,"s","awb_(o)%/")
    #T
    F_21_1=Formula_desencriptar_caracter(Caracter,"T","egbE_&/")
    F_21_2=Formula_desencriptar_caracter(Caracter,"t","ARHC_weg345")
    #U
    F_22_1=Formula_desencriptar_caracter(Caracter,"U","{\'\{")
    F_22_2=Formula_desencriptar_caracter(Caracter,"u","{+\'5g")
    F_22_3=Formula_desencriptar_caracter(Caracter,"ú","35wd")
    F_22_4=Formula_desencriptar_caracter(Caracter,"ü","CER&/04__:2")
    #V
    F_23_1=Formula_desencriptar_caracter(Caracter,"V","FWGR_[\[")
    F_23_2=Formula_desencriptar_caracter(Caracter,"v","#$_&_&/")
    #W
    F_24_1=Formula_desencriptar_caracter(Caracter,"W","#$&hht_[")
    F_24_2=Formula_desencriptar_caracter(Caracter,"w","er_WEH¨_")
    #X
    F_25_1=Formula_desencriptar_caracter(Caracter,"X","rgrt$%&//((")
    F_25_2=Formula_desencriptar_caracter(Caracter,"x","%%&//([]:_")
    #Y
    F_26_1=Formula_desencriptar_caracter(Caracter,"Y","$#&&&/&%grj")
    F_26_2=Formula_desencriptar_caracter(Caracter,"y","ARNIOBG_[*")
    #Z
    F_27_1=Formula_desencriptar_caracter(Caracter,"Z","*{+{´")
    F_27_2=Formula_desencriptar_caracter(Caracter,"z","{+}´{+A")
    #simbolos
    F_28_0_1=Formula_desencriptar_caracter(Caracter,"_","ð")
    F_28_0_2=Formula_desencriptar_caracter(Caracter,"<","ç")
    F_28_1=Formula_desencriptar_caracter(Caracter,"?","*77´")
    F_28_2=Formula_desencriptar_caracter(Caracter,"¿","*ETG")
    F_28_3=Formula_desencriptar_caracter(Caracter,".","*YUIL")
    F_28_4=Formula_desencriptar_caracter(Caracter,",","*7AWRG3")


    Palabra+=F_1_1+F_1_2+F_1_3+F_1_4+F_2_1+F_2_2+F_3_1+F_3_2+F_4_1+F_4_2+F_5_1+F_5_2+F_5_3+F_5_4+F_6_1+F_6_2+F_7_1+F_7_2+F_8_1+F_8_2+F_9_1+F_9_2+F_9_3+F_9_4+F_10_1+F_10_2+F_11_1+F_11_2+F_12_1+F_12_2+F_13_1+F_13_2+F_14_1+F_14_2+F_15_1+F_15_2+F_16_1+F_16_2+F_16_3+F_16_4+F_17_1+F_17_2+F_18_1+F_18_2+F_19_1+F_19_2+F_20_1+F_20_2+F_21_1+F_21_2+F_22_1+F_22_2+F_22_3+F_22_4+F_23_1+F_23_2+F_24_1+F_24_2+F_25_1+F_25_2+F_26_1+F_26_2+F_27_1+F_27_2+F_28_1+F_28_2+F_28_3+F_28_4+F_28_0_1+F_28_0_2
    return(Palabra)

def Proceso_generar_lista_a_desencriptar(Nombre_documento_encriptado):
    Documento=open(Nombre_documento_encriptado,"r")
    Lineas=Documento.readlines()
    Lista_de_palabras_a_encriptar=[]
    for L in Lineas:
        Lista_de_palabras_a_encriptar.append(L)
    Documento.close()
    return(Lista_de_palabras_a_encriptar)

def Desencriptar_archivo(Nombre_documento_encriptado):
    Lista_de_palabras_a_encriptar=Proceso_generar_lista_a_desencriptar(Nombre_documento_encriptado)
    Lista_contenedora_de_caracteres_temporal=[]
    Cadena_contenedora_de_caracteres_temporal=""
    for Buscador in Lista_de_palabras_a_encriptar:
        for Buscador_1 in Buscador:
            if Buscador_1=="°":
                Lista_contenedora_de_caracteres_temporal.append(Cadena_contenedora_de_caracteres_temporal)
                Cadena_contenedora_de_caracteres_temporal=""
            if Buscador_1=="ð":
                Lista_contenedora_de_caracteres_temporal.append("ð")
            if Buscador_1=="ç":
                Lista_contenedora_de_caracteres_temporal.append("ç")
            if Buscador_1!="°" and Buscador_1!="ð" and Buscador_1!="ç":
                Cadena_contenedora_de_caracteres_temporal+=Buscador_1
    return(Lista_contenedora_de_caracteres_temporal)

def Proceso_desencriptar_documento(Lista_de_comando2):
    Lista_finalmente_desencriptada=[]
    Nombre_documento=Lista_de_comando2[2]
    Nombre_documento_encriptado=Nombre_documento
    Nombre_documento+="_desencriptado.txt"
    Nombre_documento_encriptado+="_encriptado.txt"
    Pregunta_existencia_de_archivo1=Analizar_existencia_de_archivo(Nombre_documento_encriptado)
    if Pregunta_existencia_de_archivo1=="si hay":
        Lista_palabras_encriptadas=Desencriptar_archivo(Nombre_documento_encriptado)
        for Palabra in Lista_palabras_encriptadas:
            Lista_finalmente_desencriptada.append(Desencriptar_caracter(Palabra))
        Palabra_desencriptada_final=""
        for Letra in Lista_finalmente_desencriptada:
            Palabra_desencriptada_final+=Letra
        Palabra_desencriptada_final=Palabra_desencriptada_final.replace("<","\n")
        Palabra_desencriptada_final=Palabra_desencriptada_final.replace("_"," ")
        Documento=open(Nombre_documento,"w")
        Documento.write(Palabra_desencriptada_final)
        Documento.close()
        Proceso_ingresar_archivo_a_lista_de_archivos(Nombre_documento)
        print("Documento desencriptado en ",Nombre_documento)
        print("!Finalizado¡")
    else:
        print("El documento que desea desencriptar no existe")

#---------------------------------------------------------proceso1---documento-----------------------------------------------------------------------------

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
    
#------------------------------------------proceso2---documento----------------------------------------------------------------------------------------------

#Bloqueo_proceso_documento2 =si el usuario toma la desicion de "cambiar nombre" el bloqueo se desbloquea debido a que el proceso se debe repetir hasta "Pregunta_inicial2=str(input(""))"
#Pregunta_crear_archivo1=cuando no exista el archivo con el mismo nombre digitado se realiza el procedimiento de crear archivo.
#Pregunta_crear_archivo2= cuando el usurio tome la desicion de sobrescribir se realiza el procedimiento de crear archivo.

#_____________________desicion_crear_documento____________________________________________________________________
def Proceso_crear_archivo(Bloqueo_proceso_documento1,Lista_de_comando2,Pregunta_crear_archivo2):
    Nombre_documento=Lista_de_comando2[2]
    Pregunta_importante= Evaluar_documentos_importantes(Nombre_documento)
    while Pregunta_importante=="No es documento importante":
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
        Pregunta_importante="finalizo"

def Proceso_borrar_archivo(Lista_de_comando2):
    Nombre_documento=Lista_de_comando2[2]
    Pregunta_importante= Evaluar_documentos_importantes(Nombre_documento)
    while Pregunta_importante=="No es documento importante":
        Nombre_documento+=".txt"
        Pregunta_borrar_archivo1=Analizar_existencia_de_archivo(Nombre_documento)
        if Pregunta_borrar_archivo1=="si hay":
            os.remove(Nombre_documento)
            Proceso_eliminar_nombre_de_la_lista_de_archivos(Nombre_documento)
            print("¡Finalizado!")
        else:
            print("El documento que desea borrar no existe")
        Pregunta_importante="finalizo"

def Proceso_renombrar_archivo(Lista_de_comando2):
    Nombre_documento_original=Lista_de_comando2[2]
    Nombre_documento_nuevo=Lista_de_comando2[4]
    Pregunta_importante= Evaluar_documentos_importantes(Nombre_documento_original)
    while Pregunta_importante=="No es documento importante":
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
        Pregunta_importante="finalizo"

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
        print("El documento que desea leer no existe")

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
*Encriptar documento "ejemplo(data)"
*Desencriptar documento "ejemplo(data)"
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
                Proceso_encriptar_documento(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="desencriptar" and Lista_de_comando2[1]=="documento" and Lista_de_comando2[2]!=[]:
                Proceso_desencriptar_documento(Lista_de_comando2)
        except:
            print("!ERROR DE SINTAXIS!")

#---------------------------------------------------proceso-1--crear-cita--------------------------------------------------

def Proceso_mostrar_categorias_llenas(Datos):
    for Categoria,Valor in Datos.items():
        print(Categoria,Valor)

def Proceso_verificar_areas_vacias(Datos,Categoria_evaluada):
    Si_hay=0
    for Categoria in Datos:
        if Categoria==Categoria_evaluada:
            Si_hay+=1
    if Si_hay==0:
        print(Categoria_evaluada)

def Proceso_mostrar_categorias_faltantes(Datos):
    Proceso_verificar_areas_vacias(Datos,"Nombre")
    Proceso_verificar_areas_vacias(Datos,"Apellido")
    Proceso_verificar_areas_vacias(Datos,"Empresa")
    Proceso_verificar_areas_vacias(Datos,"Cargo")
    Proceso_verificar_areas_vacias(Datos,"Departamento")
    Proceso_verificar_areas_vacias(Datos,"Telefono")
    Proceso_verificar_areas_vacias(Datos,"Direccion")
    Proceso_verificar_areas_vacias(Datos,"Ciudad")
    Proceso_verificar_areas_vacias(Datos,"Correo")
    Proceso_verificar_areas_vacias(Datos,"Nit")
    Proceso_verificar_areas_vacias(Datos,"Observaciones")
#---------------------------------------------------proceso-2--crear-cita--------------------------------------------------
    
def formato_crear_cita(Valor_asignado,Datos,Lista_de_comando_cita):
    Palabra_ingresar=""
    Posicion_comando=1
    Palabra_ingresar+=Lista_de_comando_cita[Posicion_comando]
    Posicion_comando=2
    while Posicion_comando<len(Lista_de_comando_cita):
        Palabra_ingresar+=" "+Lista_de_comando_cita[Posicion_comando]
        Posicion_comando+=1
    Datos[Valor_asignado]=[Palabra_ingresar]
    return(Datos)

def Proceso_crear_una_cita():
    Bloqueo1_crear_cita="bloqueado"
    Datos={}
    while Bloqueo1_crear_cita=="bloqueado":
        Pregunta_cita=str(input(""))
        Lista_de_comando_cita=Pregunta_cita.split(" ")
        for Comando in Lista_de_comando_cita:
            if Comando=="ayuda":
                print("""Actualmente usted se encuentra realizando el proceso de crear cita
Comando Actuales:
*Categorias sin llenar
*Categorias llenas
""")
            if Comando=="salir":
                print("!Finalizado¡")
                Bloqueo1_crear_cita="desbloqueado"
                Documento_escribir_citas=open("[Datos_Citas].txt","a")
                Datos=str(Datos)
                Datos+="\n"
                Documento_escribir_citas.write(Datos)
                Documento_escribir_citas.close()
            try:
                if Comando=="nombre":
                    formato_crear_cita("Nombre",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="apellido":
                    formato_crear_cita("Apellido",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="empresa":
                    formato_crear_cita("Empresa",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="cargo":
                    formato_crear_cita("Cargo",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="departamento":
                    formato_crear_cita("Departamento",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="telefono":
                    formato_crear_cita("Telefono",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="direccion":
                    formato_crear_cita("Direccion",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="ciudad":
                    formato_crear_cita("Ciudad",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="correo":
                    formato_crear_cita("Correo",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="nit":
                    formato_crear_cita("Nit",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
            try:
                if Comando=="observaciones":
                    formato_crear_cita("Observaciones",Datos,Lista_de_comando_cita)
            except:
                print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando_cita[0]=="categorias" and Lista_de_comando_cita[1]=="sin" and Lista_de_comando_cita[2]=="llenar":
                Proceso_mostrar_categorias_faltantes(Datos)
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando_cita[0]=="categorias" and Lista_de_comando_cita[1]=="llenas":
                Proceso_mostrar_categorias_llenas(Datos)
        except:
            print("!ERROR DE SINTAXIS!")
#--------------------------proceso--2-----borrar---------cita-------------------------------------------------------

def Proceso_borrar_una_cita():
    print("trabajando en ello")

#___________________________________________menu_citas______________________________________________________________

def Proceso_cita():
    Bloqueo_proceso_documento1="bloqueado"
    while Bloqueo_proceso_documento1=="bloqueado":
        Pregunta_inicial2=str(input(""))
        Lista_de_comando2=Pregunta_inicial2.split(" ")
        if Lista_de_comando2[0]=="ayuda":
            print("""Actualmente usted se encuentra en el menu citas.
Comandos Actuales:
*Crear cita
*Borrar cita
""")
        if Lista_de_comando2[0]=="salir":
            Bloqueo_proceso_documento1="desbloqueado"
            print("Finalizado")
        try:
            if Lista_de_comando2[0]=="crear"and Lista_de_comando2[1]=="cita":
                Proceso_crear_una_cita()
        except:
            print("!ERROR DE SINTAXIS!")
        try:
            if Lista_de_comando2[0]=="borrar"and Lista_de_comando2[1]=="cita":
                Proceso_borrar_una_cita()
        except:
            print("!ERROR DE SINTAXIS!")

#________________________________________menu_principal____________________________________________________________
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
        Proceso_cita()
