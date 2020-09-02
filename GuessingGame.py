import random #Biblioteca usada para randomizar o valor do numero secreto

tentativas = 10

def inicialize():
    print("**********************************")
    print("    Bem Vindo ao Guessing Game    ")
    print("**********************************")
    print()
    print("Você terá {} tentativas para acertar o numero secreto".format(tentativas)) #Deixei fixo o numero de tentativas conforme enunciado do exercicio, mas poderia receber como input do usuario neste metodo de inicilização também
    print()
    global menor_valor #Defino variaveis globais que seram usadas na funcao NovoJogo para criar o numero secreto da partida
    global maior_valor

    #Garante que os valores selecionados pelo usuario sejam validos
    while(True): 
        menor_valor = int(input("Defina o menor valor possível para o numero secreto: "))
        if menor_valor >= 0:
            break

        print()
        print("Apenas valores positivos por aqui, tente de novo!")

    while(True):
        maior_valor = int(input("Defina o maior valor possível para o numero secreto: "))
        if maior_valor > menor_valor:
            break

        print()
        print("Achou que ia me enganar, não é mesmo?")
        print("Digite um valor maior que o menor valor selecionado para continuarmos!")


def maior_menor(list_palpites): #Essa função percorre a lista de palpites do usuario e retorna uma tupla contendo o menor e maior valores do vetor
    maior = 0
    menor = list_palpites[0]
    for i in list_palpites:
        if(i > maior):
            maior = i
        if(i < menor):
            menor = i

    return (menor, maior)
    

def NovoJogo(): #Essa função implementa o jogo em si e é chamada pelo menu quando o usuario escolhe iniciar nova partida
    numero_oculto = random.randint(menor_valor, maior_valor) #Define um numero aleatório entre os valores selecionados na inicialização do programa como numero secreto
    lista_chutes = []

    print("O número secreto foi selecionado, faça seu primeiro palpite!")
    palpite = int(input()) #Recebe o primeiro palpite do usuario
    print()
    lista_chutes.append(palpite)
    if palpite == numero_oculto: #Apresenta uma mensagem personalizada caso o usuario acerte o número de primeira e encerra o jogo
        print("Parabéns, você acertou de primeira! Hoje parece um bom dia para jogar na mega sena!") 
        return (palpite, palpite)

    while(len(lista_chutes) < tentativas): #Enquanto o numeor de tentativas do usuário não acaba e o numero secreto não é adivinhado...
        print("Você ainda tem {} tentativas".format(tentativas - len(lista_chutes))) #Avisa quantas tentativas o usuário ainda tem
        print()

        print("Seu último palpite, {} foi {} que o numero secreto".format(palpite, "menor" if palpite < numero_oculto else "maior")) #informa se o palpite anterior do usuario é maior ou menor que o numero secreto

        novo = int(input("Digite seu próximo palpite:")) #usa uma variavel intermediaria "novo" para validar se o jogador vai repetir o palpite
        print()

        repetido = False #Valida se o usuario ja tentou esse numero 
        for i in lista_chutes:
            if i == novo:
                repetido = True
                break

        if repetido: #Caso o usuario repita o palpite, não conta a tentativa
            print("Você ja tentou esse número!") 
            print("Vou ser bonzinho e não vou contar essa, vamos de novo")
            continue

        palpite = novo
        lista_chutes.append(palpite)

        if palpite == numero_oculto: #Se o usuario acertar o número, apresenta mensagem de vitória e encerra a partida
            print("Parabéns você descobriu o numero secreto em {} tentativas!".format(len(lista_chutes)))
            print("Você deve ser uma pessoa muito sábia!")
            return maior_menor(lista_chutes)

    #Se o numero de tentativas acabar, apresenta mensagem de derrota e encerra o jogo
    print("Dessa vez eu ganhei!! hahahaha")
    print("O número secreto era ", numero_oculto)
    print("Mais sorte da próxima vez!")
    return maior_menor(lista_chutes)

#Inicio da execução do programa
inicialize()

while(True): #Como foi tratado de um menu na aula passada eu decidi implementar um pequeno menu para o jogo, possibilitanto diversas partidas com uma execução do programa 
    print()
    print("Selecione uma opção:")
    print(" 0 - Iniciar nova partida")
    print()
    print(" 9 - Sair")

    selecao = input()
    print()

    if selecao == "0":
        palpites = NovoJogo() #recebo como retorno da funcao de jogo o enor e maior numeros palpitados pelo usuario, respectivamente
        print()
        print("O menor numero chutado foi {}, e o maior foi {}".format(palpites[0], palpites[1]))
        print()
        print("O que deseja fazer agora?")
        continue

    if selecao == "9":
        print("Obrigado pro jogar Guessing Game, até a próxima!")
        break

    print("Comando não reconhecido!")