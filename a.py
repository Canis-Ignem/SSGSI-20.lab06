import hashlib
import copy
import time
import uuid
import os



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


text = open("./ejemplo.txt")
lineas = text.readlines()

s = uuid.uuid4().hex

newFile = open("nuevoFicherocon00.txt","w+")
lineas.append("\n")

newFile.writelines(lineas)
newFile.write((str(s)[:8]))
newFile.close()

brief = hashlib.sha256(newFile.name)
max0 = count0(str(brief))
res = brief

start = time.time()
end = time.time()


while end - start < 60 :

    t1 = time.time()
    os.remove("nuevoFicherocon00.txt")

    s = uuid.uuid4().hex

    newFile = open("nuevoFicherocon00.txt","a")
    newFile.writelines(lineas)
    newFile.write((str(s)[:8]))
    newFile.close()

    brief = hashlib.sha256(newFile.name)
    step = count0(str(brief))
    print(step)
    if step > max0:
        max0 = step
        res = brief
    end = time.time()
    print(end- start)


print(res)