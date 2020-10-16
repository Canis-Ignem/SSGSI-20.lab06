import hashlib as hs



def sha(filename):
    #filename = input("Escribe el nombre d etu fichero")
    with open(filename,"rb") as f:
        bytes = f.read() # read file as bytes
        readable_hash = hs.sha256(bytes).hexdigest();
        return readable_hash

