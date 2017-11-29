import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd 

#calcula distancia
def dis_eucli(v1,v2):
    dim= len(v1)
    soma=0
    for i in range(dim -1):
        soma += math.pow(v1[i]- v2[i], 2)
        return math.sqrt(soma)

#Carrega os dados, dataset de atack BHP

amostras=[]
with open('attack.arff','r') as f:
    for linha in  f.readlines():
        atrib= linha.replace('\n','').split(',')
        amostras.append([float(atrib[1]),float(atrib[2]),float(atrib[8]),(atrib[21])])


#Soma os rotulos dentro do dataset
def info_dataset(amostras, verbose=True):
    if verbose:
        print ('total de amostras: %d' % len(amostras))
    rotulo1, rotulo2, rotulo3, rotulo4 = 0 ,0,0,0
    for amostra in amostras:
        if amostra[-1] == 'NB-No Block':
            rotulo1 +=1
        if amostra[-1] == 'Block':
                rotulo2 +=1
        if amostra[-1] == 'No Block':
                    rotulo3 +=1
        if amostra[-1] == 'NB-Wait':
                    rotulo4 +=1
               
        
                
    if verbose:
                print('total rotulo1: %d' %rotulo1)
                print('total rotulo2: %d' %rotulo2)
                print('total rotulo3: %d' %rotulo3)
                print('total rotulo4: %d' %rotulo4)
    return[len(amostras),rotulo1,rotulo2,rotulo3,rotulo4]

#cria as variaveis para utilizar os rotulos
_, rotulo1,rotulo2,rotulo3,rotulo4 = info_dataset(amostras)

#dividindo o dataset, em treinamento e teste, 70% treinam
total_rotulo1 ,total_rotulo2,total_rotulo3,total_rotulo4 = 0,0,0,0
for amostra in amostras:
    if (total_rotulo1 + total_rotulo2 + total_rotulo3 + total_rotulo4) < (max_rotulo1 + max_rotulo2 + max_rotulo3 + max_rotulo4):
        treinamento.append(amostra)
        if amostra[-1] == 'NB-No Block' and total_rotulo1 < max_rotulo1:
            total_rotulo1 += 1
        if amostra[-1] == 'Block' and total_rotulo2 < max_rotulo2:      
            total_rotulo2 += 1
        if amostra[-1] == 'No Block' and total_rotulo3 < max_rotulo3:
            total_rotulo3 += 1
        if amostra[-1] == 'NB-Wait' and total_rotulo4 < max_rotulo4:
            total_rotulo4 += 1
    else:
        teste.append(amostra)

#Função para executar o KNN, calcula a distancia euclideana
import math
def knn(treinamento, nova_amostra, k):
    dists, tam_treino = {} , len(treinamento)
    #calcula a distancia da nova amostra para todos os exemplos do trinamento
    for i in range(tam_treino):
        d= dis_eucli(treinamento[i],nova_amostra)
        dists[i] = d
    #Obtem chaves (indices ) dos k vizinhos mais proximos
    k_vizinhos = sorted(dists, key =dists.get)[:k]
    qtd_rotulo1, qtd_rotulo2,qtd_rotulo3,qtd_rotulo4 = 0,0,0,0
    for indice in k_vizinhos:
        if treinamento[indice][-1] == 'NB-No Block':
            qtd_rotulo1 += 1
        if treinamento[indice][-1] == 'Block':
            qtd_rotulo2 += 1
        if treinamento[indice][-1] == 'No Block':
            qtd_rotulo3 += 1
        if treinamento[indice][-1] == 'NB-Wait':
            qtd_rotulo3 += 1
        
            
    if qtd_rotulo1 > qtd_rotulo2 and qtd_rotulo1 > qtd_rotulo3 and qtd_rotulo1 > qtd_rotulo4 :
        return 'NB-No Block'
    
    if qtd_rotulo2 > qtd_rotulo1 and qtd_rotulo2 > qtd_rotulo3 and qtd_rotulo2 > qtd_rotulo4 :
        return 'Block'
    if qtd_rotulo3 > qtd_rotulo1 and qtd_rotulo3 > qtd_rotulo2 and qtd_rotulo3 > qtd_rotulo4 :
        return 'No Block'
    if qtd_rotulo4 > qtd_rotulo1 and qtd_rotulo4 > qtd_rotulo2 and qtd_rotulo4 > qtd_rotulo3 :
        return 'NB-Wait'
    

#Chama a função passando o dataset treinamento e logo apos valida a % de efetividade do algoritmo
acertos, k = 0,5
for amostra in teste:
    classe = knn(treinamento, amostra, k)
    if amostra[-1] ==  classe:
        acertos +=1
print ('total de treinamento %d' % len(treinamento))
print ('total de testes %d' % len(teste))

print ('total de acertos %d' % acertos)

print ('porcentagem de acertos %.2f%%' % (100 * acertos / len(teste)))