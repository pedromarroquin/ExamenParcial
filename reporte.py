import platform
import os

def clear():
    so=platform.system()
    if so=='Windows':
        so.system("cls")
    elif so=='Linux':
        so.system("clear")



clear()
so=platform.system()
print("\n")
print("################################################")
print("---------ESPECIFICACIONES DE LA PC----------")
print("################################################")
print("\n")
if so=='Windows':
    so.system("systeminfo")
elif so=='Linux':
    so.system("lscpu | head -24")


