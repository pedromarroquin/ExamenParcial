import platform
import os

""" def clear():
    so=platform.system()
    if so=='Windows':
        os.system("cls")
    elif so=='Linux':
        os.system("clear") """

rarch = "reporte_arquitectura.txt"

class arch:    
    so=platform.system()
    archivo = open(rarch,"w+")
    """archivo.write("################################################" + os.linesep)
    archivo.write("-----------ESPECIFICACIONES DE LA PC------------" + os.linesep)
    archivo.write("################################################" + os.linesep) """
    if so=='Windows':
        archivo.write(os.system("systeminfo > reporte_arquitectura.txt"))
    elif so=='Linux':
        archivo.write(os.system("lscpu | head -24 | tee reporte_arquitectura.txt"))
    archivo.close()