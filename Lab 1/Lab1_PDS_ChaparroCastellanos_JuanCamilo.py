#!/usr/bin/env python
# coding: utf-8

# # Laboratorio PDS

# # Juan Camilo Chaparro Castellanos
# ## 1039466438

# # Laboratorio #1.1

# #### 4.1) programa que al ingresar la edad el usuario, se determine si es mayor o no

# In[1]:


edad= int(input("Señor usuario ingrese su edad: "))
if edad<18:
    print("\n\tusted es menor de edad")
else:
    print("\n\tusted es mayor de edad")


# #### 4.2) programa que al ingresar la edad, muestre la cancion del cumpleaños y cuente hasta llegar a la edad

# In[2]:


nombre= input("Señor usuario ingrese su nombre: ")
miedad= int(input(f'Señor {nombre} ingrese su edad:'))
print(f'''feliz cumpleaños a ti\nfeliz cumpleaños querido '''+nombre+'''Feliz cumpleaños a ti\nque cumplas feliz y que los sigas cumpliendo hasta el año 3000''')
for i in range(edad):
    print(i+1)     
j=1
while (j<=miedad):
    print(j)
    j+=1


# #### 4.3) Programa que solicite iterativamente un caracter ingresado por consola (saber si es mayuscula o minuscula). El programa debe finalizar cuando se ingrese un caracter especial

# In[3]:


print("para salir ingrese 0 ")
caracter=0
while caracter!=48:
    caracter=ord(input("ingrese un caracter: "))
    if ((caracter>64) and (caracter<91)):
        print("es una mayuscula")
    elif ((caracter>96) and (caracter<123)):
        print("es una minuscula")
    elif(caracter==48):
        print("hasta luego")
    else:
        print("el caracter ingresado no es una letra")


# #### 5.3 manejo de señales

# #### 5.3.1) señal senosoidal

# In[4]:


#librerias
import numpy as np
import matplotlib.pyplot as plt
# para que la grafica se incruste en el notebook
get_ipython().run_line_magic('matplotlib', 'inline')

f=1.0 # Frecuencia de la senal
fs=5.0 # Frecuencia de muestreo
t=np.arange(0, 2.0, 1.0/fs) # Vector de tiempo
x = np.sin(2*np.pi*f*t)
print(x)
plt.plot(t,x)
plt.grid()
plt.xlabel('Time',fontsize=18)
plt.ylabel('Amplitude',fontsize=18)
plt.show()


# #### la señal auque tiene comportamiento senosoidal tiene un aspecto brusco ya que la frecuencia de muestreo es muy poca para construir la señal, es decir, al ser fs=0.5 solo se utilizan 10 puntos en 0 a 2 seg para construirla

# #### 5.3.2) cambiar la frecuencia de muestreo fs=20Hz

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
f=1.0 # Frecuencia de la senal
fs=20.0 # Frecuencia de muestreo
t=np.arange(0, 2.0, 1.0/fs) # Vector de tiempo
x = np.sin(2*np.pi*f*t)
print(x)
plt.plot(t,x)
plt.grid()
plt.xlabel('Time',fontsize=18)
plt.ylabel('Amplitude',fontsize=18)
plt.show()


# #### se evidencia que al aumentar la frecuencia de muestreo se tiene mas puntos de muestra debidamente espaciados por lo que se puede contruir una señal senosoidal

# #### 5.3.3) tasa de desempleo en colombia del periodo 2001-2017

# In[6]:


import pandas as pd # libreria para el manejo de datos
# Leer datos
TD = pd.read_excel("TD.xlsx")
# Cambio de formato de los datos
TD = pd.DataFrame(TD)
# Extraigo una de las columnas del archivo de excel
TDC = TD["TD"]
index = TD["Index"]
#grafica de la tasa de desempleo
plt.plot(index, TDC)
plt.grid()
plt.title("Tasa de desempleo en Colombia")


# #### #### la figura muestra que se tomaron alrrededor de 192 muestras, de las cuales cada una representa la tasa de desempleo en colombia de cada mes durante el periodo (2001-2017), donde se evidencia que los primeros tres años se tuvo una tasa de desempleo mayor al 14% y con el pasar de los años pudo bajar a una tasa menor al 12%

# #### 5.3.4) señal de auido

# In[7]:


from scipy.io.wavfile import read # libreria para lectura de archivos de audio
from IPython.display import Audio # para escuchar la senal
audio=('senal.wav') # Ruta del archivo con la senal
fs,x=read(audio) # Cargar el archivo
x=x/float(max(abs(x))) # escala la amplitud de la senal
t=np.arange(0, float(len(x))/fs, 1.0/fs) # Vector de tiempo
plt.plot(t,x) # Dibujar la grafica
# Los siguientes dos comandos dibujan las etiquetas de los ejes
plt.xlabel('Time',fontsize=18) # Etiqueta eje X
plt.ylabel('Amplitude',fontsize=18) # Etiqueta eje Y
plt.show() # Mostrar la grafica
Audio(x, rate=fs) # para escuchar la senal, si se desea


# #### 5.3.5) señal invertida

# In[8]:


from scipy.io.wavfile import read # libreria para lectura de archivos de audio
from IPython.display import Audio # para escuchar la senal
audio=('senal.wav') # Ruta del archivo con la senal
fs,x=read(audio) # Cargar el archivo
x=x/float(max(abs(x))) # escala la amplitud de la senal
t=-np.arange(0, float(len(x))/fs, 1.0/fs) # Vector de tiempo
plt.plot(t,x) # Dibujar la grafica
# Los siguientes dos comandos dibujan las etiquetas de los ejes
plt.xlabel('Time',fontsize=18) # Etiqueta eje X
plt.ylabel('Amplitude',fontsize=18) # Etiqueta eje Y
plt.show() # Mostrar la grafica
Audio(x[::-1], rate=fs)


# #### al invertir la señal no se puede escuchar de forma clara el mensaje

# #### 5.3.6) Valor DC y energia de la señal

# In[9]:


def logEnergy(sig): # Definir la funcion
    sig2=np.square(sig) # Elevar al cuadrado las muestras de la senal
    sumsig2=np.sum(sig2) # Sumatoria
    logE=10*np.log10(sumsig2) # Convertir a dB
    dc=np.mean(sig) # Promedio
    return logE, dc
# Ahora se usa la funcion anterior para calcular las medidas de la senal
Energy, DCvalue = logEnergy(x)
print('Energia='+str(Energy))
print('Valor DC='+str(DCvalue))


# # Laboratorio 1.2

# #### 2) numero de euler

# In[10]:


def mifactorial(z): 
    if z==0 or z==1:  #funcion que determina el factorial de 0 y/o 1
        solucion=1
        return solucion
    else:
        solucion=z*mifactorial(z-1)  #calcula factorial diferente a c0 y/o 1
        return solucion
def mieuler(x):        
    i=0
    suma=0
    while i<=numero:
        suma=suma+(1/mifactorial(numero-i)) #utilizando el factorial, genera una suma progresiva para la aproximacion del euler
        i+=1
    return suma

#ingreso de dato por parte del usuario
numero=int(input("ingrese el numero de elementos a utilizar: "))
sol=mieuler(numero)
#impresion de dato
print("e es aproximadamente: {}".format(sol))


# #### 2.2) nombre y edad

# In[11]:


lista=[]
nombre=0
edad=0
while nombre!="no mas":
    nombre=str(input("digite su nombre:"))
    if nombre != "no mas":
        edad=int(input("digite su edad:"))
        lista.append([edad,nombre])   
for x1,x2 in lista:
    print(f"Hola {x1}, su edad es: {x2}")
    if x1>17:
        print("Usted es mayor de edad")
    else:
        print("usted es menor de edad")


# #### 3) una metrica

# In[12]:


import random #se importa la funcion random, genera numero aleatorio
dimension=int(input("ingrese las dimensiones de la matriz: ")) #dimension de la matriz
matriz=[]                                          
suma=0          
traza=0                                           
for i in range(dimension):                                  
    matriz.append([])                               
    for j in range(dimension):                              
        matriz[i].append(random.randrange(100))      
        suma=suma+matriz[i][j]              
        if i==j:                                    
            traza=traza+matriz[i][j]              
print("la metrica de la matriz es:",traza/suma) 
print("matriz generada de forma aleatoria: {}".format(matriz))


# #### 4) señal de longitud variable

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#ingreso de edad
edad= int(input("Señor usuario ingrese su edad: "))
senal=np.empty((0,))
matriz=np.empty((0,100))
mmedi=[]
mdesvi=[]
for i in range(edad):
    ventana=np.random.rand()*np.random.randn(100)+np.random.rand()
    senal=np.hstack((senal,ventana))
    matriz=np.vstack((matriz,ventana))
    
#imprimir señal
plt.plot(senal)
plt.xlabel('Tiempo',fontsize=18)
plt.ylabel('Amplitud',fontsize=18)
plt.show()
for i in matriz:
    media=np.mean(i)  #media o promedio de una lista
    desvi=np.std(i)   #desviacion estandar
    mmedi.append(media) 
    mdesvi.append(desvi)
    print('la matriz \n',i)
    print("\n media: {}".format(media))
    print("desviacion estandar: {} \n".format(desvi))
plt.plot(mdesvi)
plt.plot(mmedi)
plt.xlabel('Edad',fontsize=18)
plt.ylabel('Amplitud',fontsize=18)
plt.show()


# #### se puede apreciar anteriormente que la media y la desviancion estandar sobre la misma grafica tienden a ser parecida a la señal original, es decir, tanto la media como la desviacion estandar describen la envolvente de la señal original

# ## CONCLUISONES

# #### * A medida de se genera cada uno de los puntos de este laboratorio se puede apreciar que se puede realizar diferentes analisis a una señal analoga como lo son (datos aleatorios, datos estadisticos, señales de audio) y que los resultados son parametros unicos de la misma como son (la media, la metrica, la desviacion estandar, punto maximo de energia, valor DC, tasa de muestreo, maximos, minimo, muestas anomalas, entre otros)
# 
# #### * se puede apreciar que al realizar un muestreo de una señal sin cumplir con el  teorema de Nyquist no se puede construis la señal correctamente
