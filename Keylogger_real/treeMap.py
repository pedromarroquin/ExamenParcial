import matplotlib.pyplot as plt
import squarify    # (algorithm for treemap)
import pandas as pd
from collections import Counter
import threading

def toList(objeto):
    dictionary=dict(Counter(objeto).most_common())
    lista = [[key, dictionary[key]] for key in dictionary.keys()]
    return lista

def saveTreeMap(lista,imgname):
    cantidad =[]
    key=[]
    for i in lista:
        key.append(i[0])
        cantidad.append(i[1])
    squarify.plot(sizes=cantidad, label=key, alpha=.8 )
    plt.axis('off')
    plt.title(imgname,fontsize=20,fontweight="bold")
    plt.savefig(imgname)
    
