import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# exercício 8

# considerando as variáveis da função de transferência
k = 2
tau = 4.995
theta = 1.975

def imc():
    lambida = 0.8 * theta
    kp = ((2 * tau + theta) / (k * (2 * lambida + theta)))
    ti = tau + (theta / 2)
    td = (tau * theta) / (2 * tau + theta)

    print('Kp calculado por IMC = ', kp)
    print('Ti calculado por IMC = ', ti)
    print('Td calculado por IMC = ', td)
    print('')

def cc():
    ke= (1 / k) * (tau / theta) * ((4 / 3) + ((1 / 4) * (theta / tau)))
    ti = theta * ((32 + (6 * (theta / tau))) / (13 + (8 * (theta / tau))))
    td = theta * (4 / (11 + (2 * (theta / tau))))

    print('Ke calculado por CC = ', ke)
    print('Ti calculado por CC = ', ti)
    print('Td calculado por CC = ', td)
    print('')

def controle():
    print('Entre com os dados dos parâmetros')
    k = float(input('k = '))
    tau = float(input('tau = '))
    theta = float(input('theta = '))
    print('')

    print('Entre com os dados dos parâmetros PID')
    kp = float(input('Kp = '))
    ti = float(input('Ti = '))
    td = float(input('Td = '))
    sp = float(input('SetPoint = '))
    print('')

    # construindo a função de transferência da planta
    num = np.array([k])
    den = np.array([tau, 1])
    H = cnt.tf(num, den)
    n_pade = 20
    (num_pade, den_pade) = cnt.pade(theta, n_pade)
    H_pade = cnt.tf(num_pade, den_pade)
    Hs = cnt.series(H, H_pade)

    # controlador proporcional
    numkp = np.array([kp])
    denkp = np.array([1])
    # controlador ntegrativo
    numki = np.array([kp])
    denki = np.array([ti, 0])

    # controlador derivativo
    numkd = np.array([kp * td, 0])
    denkd = np.array([1])

    # construindo o controlador PID
    Hkp = cnt.tf(numkp, denkp)
    Hki = cnt.tf(numki, denki)
    Hkd = cnt.tf(numkd, denkd)
    Hctrl1 = cnt.parallel(Hkp, Hki)
    Hctrl = cnt.parallel(Hctrl1, Hkd)
    Hdel = cnt.series(Hs, Hctrl)

    # fazendo a realimentação
    Hcl = cnt.feedback(Hdel, 1)

    t = np.linspace(0, 40, 100)
    (t, y) = cnt.step_response(sp * Hcl, t)
    plt.plot(t, y)
    plt.xlabel(' t [ s ] ')
    plt.ylabel('Amplitude')
    plt.title('Controle PID')

    plt.grid()
    plt.show()

while True:
    print('Escolha um método do controlador PID: ')
    print('[1] - Método IMC')
    print('[2] - Método CC')
    print('[3] - Entre com os parâmetros do PID')
    print('[3] - Sair')

    op = int(input('Escolha uma opção: '))
    print('')

    if(op == 1):
        imc()
    elif(op == 2):
        cc()
    elif (op == 3):
        controle()
    elif(op == 4):
        break
    else:
        print('Opção Inválida')