import sys
import time

def slowprint(texto, delay=0.07): #o slowprint é só pra deixar o print bonitinho :)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

lista_de_alunos = []
lista_de_notas = []
slowprint(('-' * 10) +'Programa de notas e Alunos' + ('-' * 10)) #introdução do programa

def menu_notas(lista_de_notas):
    notas = (input('''
    Qual operação deseja fazer? 
1.Adicionar uma nova nota
2.Calcular a média de notas da turma
3.Contar o número de notas acima da média (7)
4.Contar o número de notas abaixo da média (7)
5.Zerar a lista de notas
6.Sair do programa
7.Voltar ao menu inicial
Digite a opção que deseja: '''))
    
    while (notas not in['1', '2', '3', '4', '5', '6', '7']): #isso é uma validação caso o usuário tente digitar uma opção não existente
        notas = (input('Opção inválida! Digite um número de 1 a 7: '))
    
    operacoesnotas(notas, lista_de_notas)

def menu_alunos(lista_de_alunos):
        alunos = input('''
        Qual operação deseja fazer?
1.Adicionar um novo aluno
2.Editar o nome de um aluno
3.Remover um aluno pelo seu nome
4.Remover um aluno pela sua posição
5.Exibir todos os alunos numerados
6.Sair do programa 
7.Retornar para o menu inicial
Digite a opção que deseja:  ''')

        while (alunos not in ['1', '2', '3', '4', '5', '6', '7']): #isso também é uma validação
                alunos = input("Opção inválida! Digite um número de 1 a 7: ")
                    
        operacoesalunos(alunos, lista_de_alunos) 
    
def querercontinuar_ou_nao(menu_funcao, lista): #essa função é para saber se o usuário deseja continuar realizando operações ou não, para ele não ficar voltando sempre para o menu inicial.
    continuar = input('Você deseja continuar realizando operações? [1 para sim, 2 para não]: ')
    
    while continuar not in ['1', '2']: #isso é uma validação 
        continuar = input('Opção inválida. Digite 1 para continuar ou 2 para encerrar: ')

    if continuar == '1':
        slowprint('Ok! Voltando para o menu...')
        menu_funcao(lista)  # Chama a função de menu que foi passada como argumento
    else:
        slowprint('Ok... Finalizando, aguarde...')
        slowprint('Finalizado!')
                    
def operacoesalunos(alunos, lista_de_alunos ): 
    while True:
         if alunos == '1':
              adicionar = input('Informe o aluno que deseja adicionar: ')
              lista_de_alunos.append(adicionar)
              slowprint('O nome foi adicionado :), veja: {}'.format(lista_de_alunos))
              querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
              break

         elif alunos == '2':
            leitura = len(lista_de_alunos)
            if leitura == 0:
                slowprint('Não é possível editar pois a lista está vazia.')
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break
            else:
                editar = input('Informe o nome que você deseja editar: ')
                if editar in lista_de_alunos: 
                    edicao = input('Informe a ediçao desejada: ')
                    encontrar = lista_de_alunos.index(editar)
                    lista_de_alunos[encontrar] = edicao
                    slowprint('A edição foi realizada :) Veja: {}'.format(lista_de_alunos))
                    querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                    break
                else: 
                    slowprint('O nome não foi encontrado :(, tente novamente.')
                    querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                    break

         elif alunos == '3': 
            nome = input('Informe o aluno que deseja remover pelo nome: ')
            if nome in lista_de_alunos: 
                lista_de_alunos.remove(nome)
                slowprint('O nome foi removido, veja: {}'.format(lista_de_alunos))
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break
            else:
                slowprint('Esse nome não existe na lista, tente novamente.')
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break

         elif alunos == '4':
            indice = int(input('Informe a posição do aluno que deseja remover: ')) 
            if 0 <= indice < len(lista_de_alunos):
                lista_de_alunos.pop(indice)
                slowprint('O nome foi removido :). Veja: {}'.format(lista_de_alunos))
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break
            else:
                slowprint('Posição inválida :( Tente novamente!')
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break

         elif alunos == '5':
            leitura = len(lista_de_alunos)
            if leitura == 0:
                slowprint('Não é possível numerar pois a lista está vazia.')
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break
            else:
                slowprint("Lista de alunos:")
                for c, aluno in enumerate(lista_de_alunos, 1): #o enumerate numera a lista :)
                    slowprint('{}.{}'.format(c, aluno))
                querercontinuar_ou_nao(menu_alunos, lista_de_alunos)
                break
         
         elif alunos == '6':
            slowprint('Ok, saindo do programa, aguarde...')
            slowprint('Finalizado :)')
            return
         elif alunos == '7': 
            slowprint('Ok, retornando para o menu inicial...')
            menu_inicial(lista_de_alunos, lista_de_notas)
            break

def operacoesnotas(notas, lista_de_notas):
    while True:
        if notas == '1':
            adicionarnotas = float(input('Informe a nota que deseja adicionar: '))
            while True: 
                if adicionarnotas>10 or adicionarnotas<0:
                    adicionarnotas = float(input('Digite uma nota válida: '))
                else: 
                    lista_de_notas.append(adicionarnotas)
                    slowprint('A nota foi adicionada :) Veja: {}'.format(lista_de_notas))
                    break
            querercontinuar_ou_nao(menu_notas, lista_de_notas)
            break

        elif notas == '2':
            leituranotas = len(lista_de_notas)
            if leituranotas == 0:
                slowprint('Não é possível calcular a média, pois não existem notas registradas')
                querercontinuar_ou_nao(menu_notas, lista_de_notas)
                break
            else:
                calculo = sum(lista_de_notas)/leituranotas #o sum soma as notas e a leitura são quantas notas existem na lista
                slowprint('A média da turma é {}'.format(calculo)) 
                querercontinuar_ou_nao(menu_notas, lista_de_notas)
                break
        
        elif notas == '3':
            leituranotas = len(lista_de_notas)
            if leituranotas == 0:
                print('Não é possível fazer a leitura de notas, pois não existem notas registradas')
                querercontinuar_ou_nao(menu_notas, lista_de_notas)
                break
            else:
                 contador = 0  # Inicializa a contagem
                 for nota in lista_de_notas:
                    if float(nota) >= 7:  # Converte a string para float e verifica se é maior ou igual a 7
                        contador += 1  
                 slowprint('O número de notas acima da média (7) é {}'.format(contador))
                 querercontinuar_ou_nao(menu_notas, lista_de_notas)
                 break
        
        elif notas == '4':
            leituranotas = len(lista_de_notas)
            if leituranotas == 0:
                slowprint('Não é possível fazer a leitura de notas, pois não existem notas registradas')
                querercontinuar_ou_nao(menu_notas, lista_de_notas)
                break
            else:
                 contador = 0  # Inicializa a contagem
                 for nota in lista_de_notas:
                    if float(nota) < 7:  # Converte a string para float e verifica se é menor que 7
                        contador += 1  
                 slowprint('O número de notas abaixo da média (7) é {}'.format(contador))
                 querercontinuar_ou_nao(menu_notas, lista_de_notas)
                 break
            
        elif notas == '5':
            lista_de_notas.clear()
            slowprint('A lista foi esvaziada :) Veja: {}'.format(lista_de_notas))
            querercontinuar_ou_nao(menu_notas, lista_de_notas)
            break

        elif notas == '6':
            slowprint('Ok, saindo do programa, aguarde...')
            slowprint('Finalizado :)')
            return
        elif notas == '7': 
            slowprint('Ok, retornando para o menu inicial...')
            menu_inicial(lista_de_alunos, lista_de_notas)
            break

def menu_inicial(lista_de_alunos, lista_de_notas):
    menu = input('Escolha: [1 - Alunos, 2 - Notas, 3 - Sair]: ')
    while menu not in ['1', '2', '3']:
        menu = input('Opção inválida. Digite 1, 2 ou 3: ')

    if menu == '1':
        menu_alunos(lista_de_alunos)
    elif menu == '2':
        menu_notas(lista_de_notas)
    else:
        slowprint("Saindo...")
        return

menu_inicial(lista_de_alunos, lista_de_notas) 
