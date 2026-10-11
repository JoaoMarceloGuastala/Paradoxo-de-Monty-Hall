# 4/10/26 22:05 - Base do projeto: O paradoxo de Monty Hall é um problema de probabilidade baseado em um porgrama de televisão. O problema é o seguinte: você está em um programa onde o apresentador te apresenta três portas, atrás de uma porta há um carro e atrás das outras duas há cabras, você é obrigado a escolher uma porta e nesse momento cada porta tem 1/3, ou 33,333...%, de chance de ser a correta, após sua escolha o apresentador abre uma das portás que contém uma cabra. A matematica probabilista afirma que a melhor estratégia após o apresentador abrir uma porta com cabra é trocar de porta, pois a probabilidade de ganahr o carro aumenta para 2/3, ou 66,666...%, enquanto a porta escolhida inicialmente continua com 1/3, ou 33,333...%, de chance de ser a correta.

# 4/10/26 22:10 - Objetivo do projeto: O objetivo do código abaixo é fazer uma sequencia de simulações automatizada para testar se a probabilidade de ganahr o carro é realmente maior ao trocar de porta.

import random
from colorama import Fore
tamanho_barra = 40

while True:
    depuracao = "N"
    print("="*68)
    print("Bem vindo ao simulador do paradoxo de Monty Hall!") # Pequena introdução para deixar mais facil pra interagir.

    # Famoso sistema anti-usuario-burro
    try:
        testes = (input("Quantas rodadas você deseja simular? (MANTENHA ABAIXO DE 5.000.000)\n>>> "))
        testes = testes.replace(".", "").replace(",", "")
        testes = int(testes)
        print(f"{testes:,.0f}".replace(",", ".")) 

    except ValueError:
        print("Número de rodadas inválido!")
        continue

    print("="*68)

    if testes >= 10_000:
         pass
    else:
        depuracao = input("Ativar depuração? (S/N)\n>>> ").strip().upper()[0] # Com o modo depuração ativado é possivel ver cada resultaodd individualmente.
        if depuracao == "S":
            depuracao = "S"
            print("Depuração ativada! (Isso vai mostrar o resultado de cada rodada, então se você escolher muitas rodadas, vai ficar muito poluído!)")
                
    if testes <= 5_000_000 and testes > 0:
            ganhou_mantendo = 0
            ganhou_trocando = 0

            print(f"Rodando {testes:,.0f} jogos do Monty Hall...\n".replace(",", "."))

            for _ in range(testes):
                portas = [1, 0, 0] # 1 é o carro, 0 são as cabras
                random.shuffle(portas) # Embaralha a lista anterior
                
                escolha = random.choice([0, 1, 2]) # Escolhe uma porta aleatoriamente

                if depuracao == "S": # Com o modo depuração ativado é possivel ver cada resultaodd individualmente.
                    if portas[escolha] == 1: # Se a porta que você escolheu tem o carro, você ganha pontos em ganhou_mantendo
                        print(f"Rodada {_+1}: Você escolheu a porta {escolha+1} e {Fore.GREEN}GANHOU{Fore.RESET} o carro! {Fore.GREEN}(Mantendo){Fore.RESET}")
                        ganhou_mantendo += 1
                    else:
                        print(f"Rodada {_+1}: Você escolheu a porta {escolha+1} e {Fore.RED}PERDEU!{Fore.RESET} o carro! {Fore.RED}(Trocando){Fore.RESET}")
                        ganhou_trocando += 1 # Se você escolheu uma cabra (0), o apresentador é obrigado a abrir a outra cabra, ou seja, você ganha pontos em ganhou_trocando

                else:
                    if portas[escolha] == 1: # Se a porta que você escolheu tem o carro, você ganha pontos em ganhou_mantendo
                        ganhou_mantendo += 1
                    else:
                        ganhou_trocando += 1 # Se você escolheu uma cabra (0), o apresentador é obrigado a abrir a outra cabra, ou seja, você ganha pontos em ganhou_trocando

                    # Adicionado recentemente esse codigo serve para mostrar uma barra de progresso que aprendi a fazer recentemente.
                    if _ % 50000 == 0 or _ == testes - 1:
                        progresso = _ / testes
                        bloquinhos = int(tamanho_barra * progresso) 
                        
                        desenho = f"{Fore.GREEN}█{Fore.RESET}" * bloquinhos + f"{Fore.RED}─{Fore.RESET}" * (tamanho_barra - bloquinhos)
                        print(f'\r[{desenho}] {progresso:.1%} de testes realizados...', end='', flush=True)
                

            print(f"Resultado após {testes}:")
            print(f"Vitórias mantendo a porta escolhida: {ganhou_mantendo} ({(ganhou_mantendo/testes)*100:.1f}%)")
            print(f"Vitórias trocando da primeira escolha: {ganhou_trocando} ({(ganhou_trocando/testes)*100:.1f}%)")

            # Pergunta se o usuario quer jogar novamente, se nçao quiser da um break e finaliza.
            novamente = input("Deseja simular novamente? (S/N)\n>>> ").strip().upper()[0]
            if novamente != "S":
                print("Obrigado por usar o simulador do paradoxo de Monty Hall!")
                break
# 4/10/26 23:15 - Fim do códgo.
# 10/10/26 23:40 - Atualização
