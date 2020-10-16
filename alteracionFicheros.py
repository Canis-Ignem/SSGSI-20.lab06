
import md5
import time
import uuid
import os

#Tiempo en segundos
MAXTIME = 60

#Contamos por cuantos 0s empieza el resumen
def count0(s):
    i =0
    count = 0
    while i < len(s):
        if s[i] == "0":
            count += 1
        else:
            break
        i += 1
    return count


def AlteracionFicheroMD5(F):
    #abrimos el fichero original de texto
    text = open(F)
    #guardamos en una lista las lineas escritas
    lineas = text.readlines()
    
    #Establecemos los parametros de inicio
    start = time.time()
    end = time.time()
    max0 = 0

    while end - start < MAXTIME :
        #eliminamos el fichero del intento anterior
        try:
            os.remove("nuevoFichero.txt")
        except :
            pass
        #Generamos un string hexadecimal aleatorio
        s = uuid.uuid4().hex
        #Creamos nuestro nuevo fichero con permisos de escribit extra 'w+'
        newFile = open("nuevoFichero.txt","a")
        #Escribimos las lineas del otro fichero ademas de añadir los 8 primeros caracteres de s
        newFile.writelines(lineas)
        #Combertimos s a un string con un casteo str('')
        newFile.write( str(s)[:8]+ " G13151719" )
        #Cerramos el fichero para guardar los cambios
        newFile.close()
        #obtenemos su resumen md5 y contamos sus 0s
        brief = md5.md5(newFile.name)
        ceros = count0(str(brief))
        #Si tenemos mas 0s que el maximo anterior actualizamos los valores del resumen y el maximo de 0s
        if ceros > max0:
            max0 = ceros
            res = brief
            #Borramos el resultado anterior si existe
            try:
                os.remove("./ficheroResultado13.txt")
            except:
                pass
            #Renombramos el fichero para no eliminarlo en la siguiente rotacion
            os.rename(r"./nuevoFichero.txt",r"./ficheroResultado13.txt")
        #Calculamos el tiempo al terminar
        end = time.time()
        #Sacamos cuanto hemos tardado en segundos
        print(end- start)
        
    #Eliminar el fichero basura en caso de haberlo
    try:
        os.remove("nuevoFichero.txt")
    except :
        pass

    print(res)

#AlteracionFicheroMD5("SGSSI-20.CB.06.txt")