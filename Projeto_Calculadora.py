#!/usr/bin/env python
# coding: utf-8

# #                                          Calculadora

# In[2]:


nome_usuario = input('Por favor, informe seu nome: ')
print(f'Olá, {nome_usuario}. Seja bem vindo(a)!')

from time import sleep

resultado = float(input('Número: '))
while True:
    operaçao = input('Escolha uma operação [+ ou - ou / ou *]: ')
    outroNumero = float(input('Número: '))
    
    if operaçao == '+':
        resultado = resultado+outroNumero
        flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
        if flag == '=':
            print('Calculando...')
            sleep(1)
            print('-='*30)
            print(f'O resultado da operação é {resultado}')
            print('-='*30)
            flag = input("""[p] Parar
[z] zerar e recomeçar""")
            if flag == 'p':
                break
            if flag == 'z':
                numero = float(input('Número: '))
                
    if operaçao == '-':
        resultado = resultado-outroNumero
        flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
        if flag == '=':
            print('Calculando...')
            sleep(1)
            print('-='*30)
            print(f'O resultado da operação é {resultado}')
            print('-='*30)
            flag = input("""[p] Parar
[z] zerar e recomeçar""")
            if flag == 'p':
                break
            if flag == 'z':
                resultado = float(input('Número: '))
        
    if operaçao == '*':
        resultado = resultado*outroNumero
        flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
        if flag == '=':
            print('Calculando...')
            sleep(1)
            print('-='*30)
            print(f'O resultado da operação é {resultado}')
            print('-='*30)
            flag = input("""[p] Parar
[z] zerar e recomeçar""")
            if flag == 'p':
                break
            if flag == 'z':
                resultado = float(input('Número: '))
                
    if operaçao == '/':
        resultado = resultado/outroNumero
        flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
        if flag == '=':
            print('Calculando...')
            sleep(1)
            print('-='*30)
            print(f'O resultado da operação é {resultado}')
            print('-='*30)
            flag = input("""[p] Parar
[z] zerar e recomeçar""")
            if flag == 'p':
                break
            if flag == 'z':
                resultado = float(input('Número: '))

print('Finalizando...')
sleep(2)
print('-='*30)
print('>>>>>>>>>> VOCÊ FINALIZOU O PROGRAMA! VOLTE SEMPRE! <<<<<<<<<<')
print('-='*30)


# In[ ]:





# In[ ]:


# Falta a função de limpar o último dígito
# Falta a opção de limpar mais de um dígito
# Falta a operação de porcentagem
# Falta a operação de exponenciação
# Falta a operação de raiz quadrada
# Falta a operação de resto da divisão
# Obs: Faltam outras operações (Calculadora científica)
# Falta a opção de parênteses


# In[ ]:





# In[ ]:


## Em forma de função

def calculadora():
    nome_usuario = input('Por favor, informe seu nome: ')
    print(f'Olá, {nome_usuario}. Seja bem vindo(a)!')

    from time import sleep

    resultado = float(input('Número: '))
    while True:
        operaçao = input('Escolha uma operação [+ ou - ou / ou *]: ')
        outroNumero = float(input('Número: '))

        if operaçao == '+':
            resultado = resultado+outroNumero
            flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
            if flag == '=':
                print('Calculando...')
                sleep(1)
                print('-='*30)
                print(f'O resultado da operação é {resultado}')
                print('-='*30)
                flag = input("""[p] Parar
[z] zerar e recomeçar""")
                if flag == 'p':
                    print('Finalizando...')
                    sleep(2)
                    print('-='*30)
                    print('>>>>>>>>>> VOCÊ FINALIZOU O PROGRAMA! VOLTE SEMPRE! <<<<<<<<<<')
                    print('-='*30)
                    break
                if flag == 'z':
                    numero = float(input('Número: '))

        if operaçao == '-':
            resultado = resultado-outroNumero
            flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
            if flag == '=':
                print('Calculando...')
                sleep(1)
                print('-='*30)
                print(f'O resultado da operação é {resultado}')
                print('-='*30)
                flag = input("""[p] Parar
[z] zerar e recomeçar""")
                if flag == 'p':
                    print('Finalizando...')
                    sleep(2)
                    print('-='*30)
                    print('>>>>>>>>>> VOCÊ FINALIZOU O PROGRAMA! VOLTE SEMPRE! <<<<<<<<<<')
                    print('-='*30)
                    break
                if flag == 'z':
                    resultado = float(input('Número: '))

        if operaçao == '*':
            resultado = resultado*outroNumero
            flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
            if flag == '=':
                print('Calculando...')
                sleep(1)
                print('-='*30)
                print(f'O resultado da operação é {resultado}')
                print('-='*30)
                flag = input("""[p] Parar
[z] zerar e recomeçar""")
                if flag == 'p':
                    print('Finalizando...')
                    sleep(2)
                    print('-='*30)
                    print('>>>>>>>>>> VOCÊ FINALIZOU O PROGRAMA! VOLTE SEMPRE! <<<<<<<<<<')
                    print('-='*30)
                    break
                if flag == 'z':
                    resultado = float(input('Número: '))

        if operaçao == '/':
            resultado = resultado/outroNumero
            flag = input("""[=] Saber do resultado,
[a] adicionar mais um número""")
            if flag == '=':
                print('Calculando...')
                sleep(1)
                print('-='*30)
                print(f'O resultado da operação é {resultado}')
                print('-='*30)
                flag = input("""[p] Parar
[z] zerar e recomeçar""")
                if flag == 'p':
                    print('Finalizando...')
                    sleep(2)
                    print('-='*30)
                    print('>>>>>>>>>> VOCÊ FINALIZOU O PROGRAMA! VOLTE SEMPRE! <<<<<<<<<<')
                    print('-='*30)
                    break
                if flag == 'z':
                    resultado = float(input('Número: '))


# In[ ]:


calculadora()

