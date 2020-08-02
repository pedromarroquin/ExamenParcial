from os.path import isfile
import platform
import os


class report:
     
    def __init__(self, nombre):
        self.nombre=nombre
        archivox = open(nombre, "w")
        archivox.close()


    def setName(self):
        return self.nombre

    def logging(self,captexto):
        archivo = open(self.nombre,"a")
        archivo.write(captexto)
        archivo.close()

    def timing(self,captured,nombre):
        if isfile(nombre):
            archivo = open(nombre,"a")
            archivo.write(captured+"\n")
            archivo.close()
        else:
            archivo = open(nombre,"w")
            archivo.write("Tecla\t\t\tInicio\t\t\t\t\tFin\n")
            archivo.close()

    def arch(self):
        so=platform.system()
        if so=='Windows':
            command="systeminfo > "+self.nombre
            os.system(command)
        elif so=='Linux':
            command="lscpu | head -24 | tee "+self.nombre
            os.system(command)
    
    def joinFiles(self,file1,file2,newReport):
        txt1 = open(file1,"r").read()
        txt2 = open(file2,"r").read()
        #Invocar al nuevo file
        file3 = open(newReport,"w")
        file3.write(txt1+'\n'+txt2)

    def weight(self,name):
        return os.stat(name).st_size   
