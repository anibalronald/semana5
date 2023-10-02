#!/usr/bin/env python
# coding: utf-8

# In[1]:


tupla_aula=('marcani','vegas','figueroa','navarro')
tupla_aula


# In[3]:


tupla[]


# In[4]:


tupla_aula[2]


# In[5]:


tupla_aula[0
          ]


# In[6]:


len(tupla_aula)


# In[7]:


conjunto_aula = {'ramon','moreno','pascacio','luque'}
conjunto_aula


# In[8]:


for alumno in conjunto_aula:
    print(alumno)


# In[9]:


conjunto_aula[2]


# In[10]:


len(conjunto_aula)


# In[11]:


conjunto_aula.add("muñoz")
conjunto_aula


# In[12]:


conjunto_aula.remove("luque")
conjunto_aula


# In[14]:


diccionario_aula = {2:'muñoz','1':'loque','dos':'pascacio','3':'navarro','0':'lopez'}
diccionario_aula


# In[15]:


diccionario_aula['0']


# In[16]:


diccionario_aula[2]


# In[17]:


diccionario_aula[dos]


# In[18]:


diccionario_aula['dos']


# In[19]:


diccionario_aula['3']


# In[20]:


diccionario_aula['1']


# In[21]:


diccionario_aula['20']='tenorio'
diccionario_aula


# In[22]:


diccionario_aula.pop(2)
diccionario_aula


# In[23]:


del(diccionario_aula["dos"])
diccionario_aula


# In[24]:


for indice in diccionario_aula:
    print(indice)


# In[25]:


for indice in diccionario_aula:
    print(diccionario_aula)


# In[26]:


for indice in diccionario_aula.items:
    print(indice, valor)


# In[27]:


for indice in diccionario_aula.items():
    print(indice, valor)


# In[28]:


for indice, valor in diccionario_aula.items():
    print(indice, valor)


# In[29]:


conjunto_salon ={FIGUEROA, GARCIA, GUTIERREZ, ISLA, LOPEZ, LUQUE, MAMANI, MARCANI, MONDRAGON, MORENO, MUÑOZ, NAVARRO, OTAZU, PASCACIO, RAMON, TENORIO, VEGAS
            }
conjunto_salon


# In[30]:


conjunto_salon ={'FIGUEROA', 'GARCIA', 'GUTIERREZ', 'ISLA', 'LOPEZ', 'LUQUE', 'MAMANI', 'MARCANI', 'MONDRAGON','MORENO', 'MUÑOZ', 'NAVARRO', 'OTAZU', 'PASCACIO', 'RAMON', 'TENORIO', 'VEGAS'
            }
conjunto_salon


# In[ ]:


nombre_estudiante = input("estudiante:")


# In[ ]:


nombre_estudiante = input("estudiante:")


# In[ ]:


nombre_estudiante = input("estudiante:")


# In[33]:


muñoz


# In[34]:


nombre_estudiante = input("nombre del estudiante: ")


# In[35]:


if nombre_estudiante in conjunto_salon:
    print(f"{nombre_estudiante} está en la lista de estudiantes.")
else:
    print(f"{nombre_estudiante} no está en la lista de estudiantes.")


# In[36]:


# Lista de nombres de estudiantes
conjunto_salon ={'FIGUEROA', 'GARCIA', 'GUTIERREZ', 'ISLA', 'LOPEZ', 'LUQUE', 'MAMANI', 'MARCANI', 'MONDRAGON','MORENO', 'MUÑOZ', 'NAVARRO', 'OTAZU', 'PASCACIO', 'RAMON', 'TENORIO', 'VEGAS'
            }

# Solicitar al usuario que ingrese un nombre
nombre_estudiante = input("nombre del estudiante: ")

# Verificar si el nombre está en la lista
if nombre_estudiante in conjunto_salon:
    print(f"{nombre_estudiante} está en la lista de estudiantes del salón.")
else:
    print(f"{nombre_estudiante} no está en la lista de estudiantes del salón.")


# In[ ]:




