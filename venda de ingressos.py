nome = input('Qual é o seu nome? ')
idade = int(input('E qual a sua idade? '))
py = input('Você é estudante de python?(Responda Apenas com sim ou não): ')
if idade<0:
    print('Digite uma idade válida.')
elif idade<18 or idade==18:
    print('Opa {}, parece que você ainda não pode reservar o seu ingresso :('.format(nome))
elif idade>18:
    print('{}, você pode reservar um igresso!'.format(nome))
    r = input('{}, você deseja reservar a entrada padão(custando R$20,00), ou a entrada VIP (Custando R$50,00)?\nResponda apenas com padrão ou VIP: '.format(nome))
    if r=='padrão' or r=='VIP':
        print('Certo! Reservado.')
    elif r!='padrão' or r!='VIP':
        print('Digite uma resposta válida.')
if py=='sim' and idade>18 and (r=='padrão' or r=='VIP'):
            print('E olha {}, por você ser um(a) estudante de python, você ainda ganha um desconto de 50% na reserva do seu ingresso!'.format(nome))
elif py=='não' and idade>18 and (r=='padrão' or r=='VIP'):
    print('Se torne um estudante de pyhton para obter 50% de desconto em!')
