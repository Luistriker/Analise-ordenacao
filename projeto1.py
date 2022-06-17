#====IMPORTS==============================================================================

from cProfile import Profile
from math import isqrt
from math import fmod
import random
import timeit
from heapq import heappop, heappush

#====CASOS================================================================================

# Recupera o tamanho do vetor
tamanho = int(input("Digite o tamanho do caso:"))

# Função que gera um arquivo com uma lista de números já ordenados
def ordenado():
    list =[]
    for i in range(tamanho): 
        list.append(i+1)

    with open('ordenado.txt', 'w') as arv:
        for i in list:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()

# Função 1 que gera um arquivo com uma lista de números aleatórios
def aleatorio1():
    list =[]
    for i in range(tamanho):
        list.append(random.randrange(1, 1001))

    with open('aleatorio1.txt', 'w') as arv:
        for i in list:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()

# Função 2 que gera um arquivo com uma lista de números aleatórios
def aleatorio2():
    list =[]
    for i in range(tamanho):
        list.append(random.randrange(1, 1001))

    with open('aleatorio2.txt', 'w') as arv:
        for i in list:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()

ordenado()
aleatorio1()
aleatorio2()

#====LEITURA==============================================================================

# Listas para ordenar
l1 =[]; l2 =[];

# Função que recupera os dados de um arquivo
def leitura(l1,l2):
    path = input("Digite o nome do arquivo:")
    print("\n")
    with open(path,"r") as pl:
        for line in pl:
            line = line.replace("\n","").split(" ")
            for i in line:
                l1.append(int(i))
                l2.append(int(i))

leitura(l1,l2)

#====ORDENAÇÃO===========================================================================

#====BubbleSort==========================================================================

def bubbleSort(list):
    n = len( list )
    for i in range( n - 1 ) :
        flag = 0
        for j in range(n - 1) :
            if list[j] > list[j + 1] : 
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
                flag = 1
        if flag == 0:
            break

    return list

#====SqrtBubbleSort============================================================================

@profile # Cálculo do uso de memória
def sqrtBubbleSort(list):
    tamanho = len(list)
    raiz = isqrt(tamanho)
    loop = tamanho//raiz
    resto = int(fmod(tamanho,raiz))
    partes=[];ordem=[]; 
    #======================================
    for i in range(loop):
        start = int(i*raiz)
        end = int((i+1)*raiz)
        
        if(i+1 == raiz):
            end = end + resto

        x = list[start:end]
        partes.append(x)
        # print(start,end,"\n")
        partes[i] = bubbleSort(partes[i])
    # print("partes:",partes)
    #======================================
    for i in range(raiz):
        # print(i)
        for j in range(raiz):
            y = partes[j]
            t = len(y)
            ordem.append(int(y[t-1]))
            partes[j].remove(y[t-1])
            if(i+1 == raiz and j+1 == raiz):
                for k in range(len(y),0,-1):
                    # print("tamanho",len(y),"index",k)
                    ordem.append(int(y[k-1]))
                    partes[raiz-1].remove(y[k-1])
            ordem = bubbleSort(ordem)
            # print("Ordem:",ordem)
    return ordem

#====HeapSort============================================================================

def heapSort(list):
    heap = []
    for element in list:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

#====SqrtHeapSort============================================================================

@profile # Cálculo do uso de memória
def sqrtHeapSort(list):
    tamanho = len(list)
    raiz = isqrt(tamanho)
    loop = tamanho//raiz
    resto = int(fmod(tamanho,raiz))
    partes=[];ordem=[]; 
    #======================================
    for i in range(loop):
        start = int(i*raiz)
        end = int((i+1)*raiz)
        
        if(i+1 == raiz):
            end = end + resto
    
        x = list[start:end]
        partes.append(x)
        # print(start,end,"\n")
        partes[i] = heapSort(partes[i]) 
    # print("partes:",partes)
    #======================================
    for i in range(raiz):
        # print(i)
        for j in range(raiz):
            y = partes[j]
            t = len(y)
            ordem.append(int(y[t-1]))
            partes[j].remove(y[t-1])
            if(i+1 == raiz and j+1 == raiz):
                for k in range(len(y),0,-1):
                    # print("tamanho",len(y),"index",k)
                    ordem.append(int(y[k-1]))
                    partes[raiz-1].remove(y[k-1])
            ordem =  heapSort(ordem)
            # print("Ordem:",ordem)
    return ordem

#====Dados==============================================================================

# Bubblesort
print("=====SqrtBubbleSort=====")
inicio = timeit.default_timer() # Contagem de tempo
ordem1 = sqrtBubbleSort(l1)
fim = timeit.default_timer()
# print(l1)
# print('Ordenado:',ordem1)
print('Duracao: %.3fs' % (fim - inicio))
print("\n")

print("=====SqrtHeapSort=====")
inicio = timeit.default_timer() # Contagem de tempo
ordem2 = sqrtHeapSort(l2)
fim = timeit.default_timer()
# print(l2)
# print('Ordenado:',ordem2)
print('Duracao: %.3fs' % (fim - inicio))
print("\n")



