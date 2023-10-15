import numpy as np
import control as cnt
import matplotlib.pyplot as plt
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k=2
tau=4.995
Theta = 1.975 # atraso de propagação
#parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s
kpCC=1.5
TiCC=4.2
TdCC=0.67

kpIMC=1.082
TiIMC=4.932
TdIMC=0.824


#escrevendo a função de transferência da planta
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

# Controlador proporcional - IMC
numkpIMC = np. array ([kpIMC])
denkpIMC = np. array ([1])
#integral
numkiIMC = np. array ([kpIMC])
denkiIMC = np. array ([TiIMC,0])
#derivativo
numkdIMC = np. array ([kpIMC*TdIMC,0])
denkdIMC = np. array ([1])
#Construindo o controlador PID
HkpIMC = cnt.tf(numkpIMC , denkpIMC)
HkiIMC=cnt.tf(numkiIMC , denkiIMC)
HkdIMC=cnt.tf(numkdIMC , denkdIMC)
Hctrl1IMC = cnt.parallel (HkpIMC , HkiIMC)
HctrlIMC = cnt.parallel (Hctrl1IMC , HkdIMC)
HdelIMC = cnt.series (Hs , HctrlIMC)
#Fazendo a realimentação
HclIMC = cnt.feedback(HdelIMC, 1)


# Controlador proporcional - Cohen Coon
numkpCC = np. array ([kpCC])
denkpCC = np. array ([1])
#integral
numkiCC = np. array ([kpCC])
denkiCC = np. array ([TiCC,0])
#derivativo
numkdCC = np. array ([kpCC*TdCC,0])
denkdCC = np. array ([1])
#Construindo o controlador PID
HkpCC = cnt.tf(numkpCC , denkpCC)
HkiCC=cnt.tf(numkiCC , denkiCC)
HkdCC=cnt.tf(numkdCC , denkdCC)
Hctrl1CC = cnt.parallel (HkpCC , HkiCC)
HctrlCC = cnt.parallel (Hctrl1CC , HkdCC)
HdelCC = cnt.series (Hs , HctrlCC)
#Fazendo a realimentação
HclCC = cnt.feedback(HdelCC, 1)

#IMC
tIMC = np . linspace (0 , 40 , 100)
(tIMC , yIMC ) = cnt.step_response ( HclIMC, tIMC )

plt.subplot(1,2,1)
plt.plot (tIMC , yIMC )
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('IMC')
plt.grid ()

#Cohen Coon
tCC = np . linspace (0 , 40 , 100)
(tCC , yCC ) = cnt.step_response ( HclCC, tCC )

plt.subplot(1,2,2)
plt.plot (tCC , yCC )
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Choen Coon')
plt.grid ()



plt.show()