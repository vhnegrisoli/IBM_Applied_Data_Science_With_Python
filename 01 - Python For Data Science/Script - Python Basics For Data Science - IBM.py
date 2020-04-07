#!/usr/bin/env python
# coding: utf-8

# ## Módulo 1 - Python Basics

# In[6]:


print("Hello\nWorld!")


# In[9]:


type('5668.413')


# In[10]:


type(True)


# In[4]:


int(1.0)


# In[21]:


# Usar // irá dividir para um int
25 // 5


# In[28]:


30 * (2 * 60)


# In[52]:


indices = "O índice"
len(indices)


# In[62]:


concat = " é top"
(3 * indices) + 2 * concat


# In[63]:


print("Teste pular\nlinha")


# In[61]:


print("Teste tab\tlinha")


# In[66]:


print("Uma barra\\ no meio da String!")


# In[68]:


upper = "upper case?"


# In[69]:


upper.upper()


# In[71]:


upper.replace("upper", "LOWER")


# In[75]:


upper.find("?")


# ## Módulo 2 - Python Data Structures

# In[76]:


# Lists e Tuples


# In[77]:


ratings = (1, 2, 3)


# In[79]:


ratings[2]


# In[80]:


new_tuple = (3, 5)


# In[81]:


concat_tuple = ratings + new_tuple


# In[86]:


concat_tuple[2:4]


# In[90]:


sorted(ratings)


# In[108]:


# Nesting (uma tuple dentro de uma tuple)
NT = (1, (2, 3), 4, 5, 6)
NT[1][0]


# In[120]:


# Lists
l = ["Teste", 1, 1.2]
l[0:3]


# In[122]:


l.extend([4, 5])


# In[124]:


l.append(7)


# In[126]:


l


# In[129]:


l[0] = 156


# In[131]:


del(l[0])


# In[133]:


"Split;By;Delimiter".split(";")


# In[136]:


# Copiar uma lista

A = [1,2,3,4,5]
B = A[:]
B


# In[138]:


B=["a","b","c"] 
B[1:]


# In[142]:


B[2]


# In[143]:


# Sets


# In[151]:


set1 = {1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7}
set1
set(A)
set1.add(41)
set1.remove(2)
set1
# Usar o IN para verificar se há um item no set
121 in set1


# In[152]:


set2 = {1,2,3,89,99}


# In[162]:


set2.issubset(set2)


# In[165]:


S={'A','B','C'}
U={'A','Z','C'}
S & U


# In[166]:


S.union(U)


# In[10]:


# Dictionaries

dict1 = {"Crisis": 1985, "Kingdom": 1996, "Identity": 2004}
"Crisis" in dict1


# In[11]:


dict1.values()


# ## Módulo 3 - Python Programming Fundamentals

# In[12]:


a = 6
a == 6


# In[20]:


age = 18
if (age > 18):
    print("Menor de idade")
elif(age == 18):
    print("Acabou de fazer 18")
else:
    print("Maior de idade")


# In[24]:


if (age > 18 and age <= 30 or age == 10):
    print("Age is {}".format(str(age)))
elif (age <= 5):
    print("Too young")
else:
    print("I don't know anymore")


# In[27]:


list = range(1, 10)
for i in (list):
    print(str(i))


# In[40]:


squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(len(squares)):
    squares[i] = 'white'
print(squares)

for square in squares:
    square = 'red'
    print(square)
    
for i, square in enumerate(squares):
    print("Index: {}, Square: {}".format(str(i), square))


# In[46]:


newSquares = []
i = 0
while (i < len(squares) and squares[i] == 'white'):
    newSquares.append(squares[i])
    i += 1
    
newSquares


# In[48]:


A=[3,4,5]

for a in A:
    print(a)


# In[49]:


# Funções
def calculate(a, b):
    return a + b

calculate(1, 4)


# In[58]:


lista = [1, 8, 7, 5, 3, 2, 4, 8, 19]

for i in range(len(lista)):
    if (i < len(lista) - 1):
        print(str(calculate(lista[i], lista[i + 1])))
sum(lista)


# In[59]:


listaOrdenada = sorted(lista)
listaOrdenada


# In[63]:


lista.sort()
lista


# In[64]:


def ordenar(lista):
    return sorted(lista)


# In[65]:


novaLista = [8, 9, 5, 1, 3, 4, 6]
print(ordenar(novaLista))


# In[66]:


def printNames(*names):
    for name in names:
        print(name)


# In[67]:


printNames("Nome 1", "Nome 2", "Nome 3", "Nome 4")


# In[68]:


type(1)


# In[69]:


type(lista)


# In[71]:


type(a)


# In[94]:


class Circle(object):
    
    def __init__(self, radius = 10, color = 'red'):
        self.radius = radius
        self.color = color
    
    def addRadius(self, radius):
        self.radius = self.radius + radius
        
    def changeColor(self, color):
        self.color = color
    
class Rectangle(object):
    
    def __init__(self, color, height, width):
        self.color = color
        self.height = height
        self.width = width


# In[95]:


redCircle = Circle(10, 'red')
redCircle.color = "green"
redCircle.color


# In[96]:


redCircle.addRadius(10)
redCircle.radius


# In[97]:


redCircle.changeColor('Blue')
redCircle.color


# In[99]:


dir(redCircle)


# In[123]:


newCircle = Circle(radius = 20, color = 'red')
newCircle.color


# ## Módulo 4 - Working With Data In Python

# In[213]:


file1 = open("dados/example1.txt", "w")


# In[214]:


file1.name


# In[215]:


file1.mode
print(file1.closed)
file1.write("File 1\nFile 2\nFile 3")


# In[216]:


with open("dados/example1.txt", "r") as file1:
    stuff = file1.read()
print(file1.closed)
print(stuff)


# In[217]:


stuff


# In[218]:


with open("dados/example1.txt", "r") as file1:
    stuff = file1.readlines()
print(file1.closed)
print(stuff)
stuff


# In[219]:


with open("dados/example1.txt", "r") as file1:
    stuff = file1.readlines(14)
    print(stuff)


# In[220]:


with open("dados/example2.txt", "w") as file2:
    file2.write("New file using With Open")

file2.closed


# In[221]:


lines = ["Linha 1\n", "Linha 2\n", "Linha 3\n", "Linha 4\n"]

with open("dados/example3.txt", "w") as file3:
    for line in lines:
        file3.write(line)
with open("dados/example3.txt", "r") as wfile3:
    writtenFile = wfile3.readlines()
writtenFile


# In[229]:


# Copiando os dados de um arquivo existente para outro arquivo, criando um example5.txt e copiando os dados de example4.txt
with open("dados/example3.txt", "r") as file3:
    with open("dados/example4.txt", "w") as file4:
        for line in file3:
            file4.write(line)

# Comparando os arquivos copiados
file3Str = ""
file4Str = ""

with open("dados/example3.txt", "r") as file3:
    file3Str = file3.readlines()

with open("dados/example4.txt", "r") as file4:
    file4Str = file4.readlines()

if (file3Str == file4Str):
    print("File3 and File4 are equals")
else:
    print("File3 and File4 are different")


# In[247]:


import pandas as pd

# Gerar um arquivo CSV para estudo
with open("dados/csv_data.csv", "w") as csvFile:
    csvFile.write("Id;Description;Data\n")
    csvFile.write("1;Car;206\n")
    csvFile.write("2;Bus;1511\n")
    csvFile.write("3;Bike;13\n")
    csvFile.write("4;Motorcycle;895\n")
    csvFile.write("5;Truck;332\n")
    csvFile.write("6;Plane;60\n")

df = pd.read_csv("dados/csv_data.csv", delimiter = ";")
df.head()


# In[248]:


# Criando um dataframe
dictionary = {
    'Id': [1, 2, 3, 4, 5],
    'Description': ['Car', 'Bus', 'Bike', 'Motorcycle', 'Truck'],
    'Data': [206, 1511, 13, 895, 332]
}
df2 = pd.DataFrame(dictionary)
df2.head()


# In[255]:


# Particionar partes de um DataFrame em outro

df3 = pd.DataFrame(df2[['Id', 'Description']])
df3.head()


# In[294]:


item = df3.iloc[0, 1]
item


# In[296]:


df4 = pd.DataFrame({
  'years': [1998, 1998, 1997, 1982, 2005, 2004, 2005, 2005, 2004, 2001]    
})


# In[301]:


# Dados distintos, sem duplicatas
df4["years"].unique()


# In[307]:


# Filtrando o DataFrame apenas pelos anos maiores que 2000
df4[df4["years"] > 2000]


# In[311]:


df3.to_csv("dados/data_frame.csv")


# In[317]:


df5 = pd.DataFrame({'a':[1,2,1],'b':[1,1,1]}) 
df5['a'] == 1


# ## Módulo 5 - Working With NumPy Arrays

# In[334]:


import numpy as np

# Arrays 1D - 1 Dimensão

a = np.array([1, 2, 3, 4, 5])
type(nparray)


# In[335]:


a.size


# In[336]:


a.ndim


# In[337]:


a.shape


# In[338]:


a.dtype


# In[339]:


f = np.array([1.5, 1.2, 5.3, 12.0, 14.1])
f.dtype


# In[340]:


f[0:2]


# In[348]:


f[0:2] = 85.4, 12.3
f[0:2]


# In[358]:


# Soma de dois vetores sem numpy
u = [0, 1]
v = [1, 0]
z = []

for i, j in zip(u, v):
    z.append(i + j)

print(z)
# Soma de dois vetores com numpy
    
u = np.array([0, 1])
v = np.array([1, 0])
z = np.array(u + v)

z


# In[360]:


y = np.array([1, 2])
z = 2 * y
z


# In[398]:


z = np.dot(u, v)
z


# In[363]:


z = u + 1
z


# In[364]:


z.mean()


# In[365]:


z.max()


# In[366]:


z.min()


# In[367]:


z.std()


# In[372]:


np.linspace(-5, 5, num = 5)


# In[373]:


np.linspace(-5, 5, num = 100)


# In[379]:


np.sin(u)


# In[382]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.gcf().set_size_inches(16, 8)
plt.plot(x, y)


# In[390]:


# Arrays 2D - 2 Dimensões (Matrizes)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[395]:


n = a.ndim
n


# In[399]:


a.shape


# In[400]:


a.size


# In[415]:


a[0, 0:3]


# In[416]:


a[2, 2:4]


# In[417]:


a[1, 0]


# In[425]:


m1 = np.array([[0, 1, 2], [3, 4, 5]])
m2 = np.array([[4, 3, 5], [2, 0, 1]])
mr = m1 + m2
mr


# In[427]:


mr2 = m1 * m2
mr2


# In[429]:


mr3 = 2 * m1 
mr3


# In[1]:


# Multiplicação matricial
m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[1, 2], [3, 4], [5, 6]])

mr = np.dot(m1, m2)
mr


# In[2]:


int(3.2)


# In[3]:


A='1234567'


# In[4]:


A[1::2]


# In[5]:


Name="Michael Jackson" 


# In[6]:


Name.find('el')


# In[7]:


A='1' 


# In[8]:


B='2'


# In[9]:


A+B


# In[10]:


'1,2,3,4'.split(',')


# In[11]:


A=[1,'a']
B=[2,1,'d']
A+B


# In[12]:


V={'A','B'}
V.add('C')


# In[13]:


V


# In[ ]:





# In[14]:


V={'A','B','C'}
V.add('C')
V


# In[16]:


A=['1','2','3']
for a in A:
    print(2*a)


# In[17]:


def Add(x,y):
    z=y+x
    return(y)


# In[19]:


Add('1', '1')


# In[ ]:




