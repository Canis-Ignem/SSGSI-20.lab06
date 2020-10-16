import md5
import copy
import time
import uuid
import os

#Recive las lineas de ambos ficheros y el parametro para la ultima linea
#Si no coinciden es falso
def sameLines(of , ff):
    for i in range(len(of)-1):
        if ff[i] == of[i]:
            pass
        else:
            print("Error1")
            return False
    return True

#recibe por parametro las lineas del fichero falso y la ultima linea leida 
def isHex(fl, ultLinea):
    
    #Letras no hexadecimales
    resto = "ghijklnmñopqrstuvwxyz"
    #Linea apendice hexadecimal
    s = fl[ultLinea]
    S = s.split(" ")
    print(S[0])
    if len(S) != 2:
        print("Error2.1")
        return False

    if S[1] != "G13151719":
        print("Error2.2")
        return False
    #Para cada char en s comprobamos si es un numero o esta en resto
    #Si no es numero y esta en resto entonces es falso
    for c in S[0]:
        if not str(c).isalnum() and c in resto:
            print("error2.3")
            return False
    
    return True

#Recive por parametro un resumen md5
def start0(brief):
    #Lo casteamos a string y comprobamos si su primer caracter es 0 si no lo es devolvemos falso
    if str(brief)[0] != "0":
        print("error3")
        return False
    return True
            
def isFake(f_original_file, fake_file):
    
    #Por defecto lo ponemos a falso, es decir no es una falsificacion
    #abrimos ambos ficheros
    f_original = open(f_original_file)
    f_falso = open(fake_file)
    
    #Cogemos las lineas de los dos
    original_lineas = f_original.readlines()
    fake_lines = f_falso.readlines()
    


    #Si no coinciden en el contenido de las lineas es un fichero falso
    if not sameLines(original_lineas, fake_lines):

        return True
    #Si la ultima linea del fichero falso no es exadecimal es falso
    if not isHex(fake_lines, len(original_lineas)):

        return True
    
    #Calculamos el md5
    brief = md5.md5(f_falso.name)
    
    #Si su resumen MD5 no empieza por 0 es falso
    if not start0(brief):
        return True
    
    #Si ninguno de los anteriores se cumple es un fichero valido  
    return False


#Si el fichero no es falso que no lo es, si lo es printeamos que no es
print("El fichero no es falso" if not isFake("SGSSI-20.CB.06.txt","ficheroResultado13.txt") else "El fichero es falso")