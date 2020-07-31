import platform
import os

def clear():
    so=platform.system()
    if so=='Windows':
        os.system("cls")
    elif so=='Linux':
        os.system("clear")



clear()
so=platform.system()
print("\n")
print("################################################")
print("---------ESPECIFICACIONES DE LA PC----------")
print("################################################")
print("\n")
if so=='Windows':
    os.system("systeminfo > caracteristica.txt")
elif so=='Linux':
    os.system("lscpu | head -24 | tee caracteristica.txt")


