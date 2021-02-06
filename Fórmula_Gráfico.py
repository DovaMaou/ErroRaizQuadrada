#Matheus Duarte Francisco - Dova Maou

#Bibliotecas utilizadas

import numpy as np
import matplotlib.pyplot as plt

xg, yg = [0,1], [0,1]
RSR = [np.sqrt(i) for i in range(501)]

Erro, Erro_per = [],[]

x = 2 #começaremos com x =2




#Função que descobre a raíz perfeita mais próxima
def closest_root(x):
    xpe = x-1
    xpd = x+1
    
    while np.sqrt(xpe) != int(np.sqrt(xpe)):
        xpe -= 1
    while np.sqrt(xpd) != int(np.sqrt(xpd)):
        xpd += 1
    
    if abs(xpd-x) > abs(xpe-x):
        return xpe
    else:
        return xpd
    
    
    
#Calcula a raíz pela fórmula dada
while x <= 200:
    if np.sqrt(x) != int(np.sqrt(x)):
        y = closest_root(x)
        
        V = (x+y)/(2*np.sqrt(y))
    else:
        V = np.sqrt(x)
    
    xg.append(x)
    yg.append(V)
    
    x += 1


#Calcula os erros absolutos e percentuais#
for i in range(len(xg)):
    erro = yg[i] - RSR[i]
    Erro.append(erro)
    
    if erro == 0:
        Erro_per.append(0)
    else:
        erro_per = 100*(erro/RSR[i])
        Erro_per.append(erro_per)

#Cria os Gráficos#
plt.figure()
plt.scatter(xg,Erro, s=1)
plt.title("Erro Absoluto")
plt.xlabel("X")
plt.ylabel("Erro")
plt.show()

plt.figure()
plt.scatter(xg,Erro_per, s=1)
plt.title("Erro Percentual")
plt.xlabel("X")
plt.ylabel("Erro")
plt.show()
    
    


    
    
    