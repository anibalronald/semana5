#!/usr/bin/env python
# coding: utf-8

# semana 05
# muñoz cosme anibal ronald

# In[4]:


def saludo():
    print("bienvenidos al curso de LP3")
    print("****python****")
saludo()


# In[8]:


def factorial(numero):
    fac=1
    for i in range (1,numero+1):
        fac*=i
        #fac = fac*i
    print(f"El factorial es: {fac}")


# In[ ]:





# In[9]:


numero = int(input("ingrese numero:"))
factorial(numero)


# In[10]:


def saludo2():
    mensaje = "Bienvenido a lp3"
    return mensaje


# In[11]:


def factorial2(numero):
    fac = 1
    for i in range(1,numero+1):
        fac*=i
        # fac = fac*i
    return fac


# In[12]:


numero = int (input("numero:"))
print(f"El factorial de {numero} es {factorial2(numero)}")


# In[13]:


#ejemplo calcular igv


# In[14]:


def obtenerigv(importe):
    return importe*0.19


# In[15]:


obtenerigv(150)


# In[16]:


factorial2(5)+10


# In[ ]:




