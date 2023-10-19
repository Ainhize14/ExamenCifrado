import os
import hashlib

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = "/home/ainhize/imagen"

# Valor MD5 dado para la comparación
valor_md5_dado = "e5ed313192776744b9b93b1320b5e268"


# Función para calcular el hash MD5 de un archivo
def calcular_md5_archivo(archivo_ruta):
    hasher = hashlib.md5()
    with open(archivo_ruta, 'rb') as archivo:
        while True:
            datos = archivo.read(8192)
            if not datos:
                break
            hasher.update(datos)
    return hasher.hexdigest()


# Lista para almacenar los nombres de archivos con coincidencia MD5
archivos_coincidentes = []


# Itera a través de los archivos en la carpeta
for archivo_nombre in os.listdir(carpeta_imagenes):
    archivo_ruta = os.path.join(carpeta_imagenes, archivo_nombre)
    if os.path.isfile(archivo_ruta):
        md5_calculado = calcular_md5_archivo(archivo_ruta)
        if md5_calculado == valor_md5_dado:
            archivos_coincidentes.append(archivo_nombre)


# Imprime los archivos que coinciden
if archivos_coincidentes:
    print("Archivos con hash MD5 coincidente:")
    for archivo in archivos_coincidentes:
        print(archivo)
else:
    print("No se encontraron archivos con hash MD5 coincidente.")

