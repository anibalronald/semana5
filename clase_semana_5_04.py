#!/usr/bin/env python
# coding: utf-8

# semana5 -04
# 
# muñoz cosme anibal ronald
# 

# In[1]:


#problema 01 
#crear la siguiente clase
#clase: persona
#atributos: nombre, apellidos, fecha_nacimiento, dni


# In[12]:


class Persona:
    nombre="brandon"
    apellidos="isla conislla"
    dni="123456789"
    talla=1.6


# In[13]:


#creamos un objeto persona1 de la calse persona()
# y le asignamos valores

#creacion del objeto persona1
persona1 = Persona()

#asiganmos valores al bojeto

print("persona1")
print(f"nombre: {persona1.nombre}")
print(f"apellidos: {persona1.apellidos}")
print(f"DNI: {persona1.dni}")
print(f"talla: {persona1.talla}")


# In[14]:


#para usar constructores utilizamos: __init__
#¿que es un constructor?
#- clase: curso
#- atributos: codigo, nombre, horas, creditos


# In[17]:


#solucion

class curso:
    def __init__(self, codigo, nombre, horas, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.horas = horas 
        self.creditos= creditos
    def mostrar_datos_curso(self):
        print(f"curso:{self.nombre}")
        print(f"codigo:{self.codigo}")
        print(f"horas:{self.horas}")
        print(f"creditos:{self.creditos}")
        


# In[16]:





# In[18]:


#creamos el bojeto curso1 y le mandamos parametros


# In[19]:


curso1 = curso("C0501","LP3",6,3)


# In[20]:


#mostramos los datos completos 


# In[21]:


curso1.mostrar_datos_curso()


# In[ ]:




