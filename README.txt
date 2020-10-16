Las instrucciones para alterar ficheros es la siguiente:

MD5:
    -Tener acceso en el equipo al fichero que se desea modificar
    -Asegurarse que el ambiente de ejecucion es la carpeta con todo el codigo disponible
    -Entrar al fichero alteracionFicheros.py y en la ultima linea escribir lo siguiente: AlteracionFicheroMD5(PATH)
        .Siendo PATH un string con la direccion del fichero que se desea modificar.
    -En caso de querer que el programa se ejecute durante mas tiempo cambiar la variable MAXTIME al comienzo del fichero, esta en segundos

SHA:
    -Seguir las instrucciones de arriba en el fichero AlteracionSHA.py
    -Entrar al fichero alteracionFicheros.py y en la ultima linea escribir lo siguiente: AlteracionFicheroSHA(PATH)
        .Siendo PATH un string con la direccion del fichero que se desea modificar.
    -En caso de querer que el programa se ejecute durante mas tiempo cambiar la variable MAXTIME al comienzo del fichero, esta en segundos


Si lo que se desea comprobar que la alteracion cumple los requisitos establecidos seguir la siguientes isntrucciones.

    -Tener acceso en el equipo a los ficheros que se desa comprobar
    -Asegurarse que el ambiente de ejecucion es la carpeta con todo el codigo disponible
    -Abrir el fichero comprobacionFicheros.py y en la ultima linea escribir: print("El fichero no es falso" if not isFake("PATH","PATH2") else "El fichero es falso")
        .Donde PATH es la direccion del fichero original y PATH2 es la direccion del fichero modificado, 
        IMPORTANTE! si se cambia el orden no funcionara de manera correcta.