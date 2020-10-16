import copy
import time
import uuid
import os
import sha

#Tiempo en segundos
MAXTIME = 60

#Para mas informacion sobre esta implementacion por favor revisar AlteracionFicheros.py

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
    

def AlteracionFicheroSHA(F):
    text = open(F)
    lineas = text.readlines()

    s = uuid.uuid4().hex
    
    start = time.time()
    end = time.time()
    max0 = 0

    while end - start < 60 :
        
        try:
            os.remove("nuevoFichero.txt")
        except :
            pass
        
        s = uuid.uuid4().hex
        
        newFile = open("nuevoFichero.txt","a")
        newFile.writelines(lineas)
        newFile.write( str(s)[:8]+ " G13151719" )
        newFile.close()

        brief = sha.sha(newFile.name)
        ceros = count0(str(brief))
        print(ceros)
        if ceros > max0:
            max0 = ceros
            res = brief
            try:
                os.remove("./ficheroResultadoSHA.txt")
            except:
                pass
            os.rename(r"./nuevoFichero.txt",r"./ficheroResultadoSHA.txt")
        end = time.time()
        print(end- start)

    try:
        os.remove("nuevoFichero.txt")
    except :
        pass
    print(res)