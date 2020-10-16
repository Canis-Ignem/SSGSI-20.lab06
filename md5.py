#Libreria con algoritmos de encriptacion
import hashlib as hs



def md5(filename):
    #Usando el fichero que se habre como variable 'f'
    with open(filename,"rb") as f:
        #Leemos Byte a Byte
        bytes = f.read() # read file as bytes
        #Cogemos el conjunto de bytes y sacamos el resumen md5
        readable_hash = hs.md5(bytes).hexdigest();
        return readable_hash
#print(md5("SGSSI-20.Lab5.13.JPER.pdf"))