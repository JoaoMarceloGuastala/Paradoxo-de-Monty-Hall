import random

print("="*30)
print("Cópia do jogo GrapWar")
print("="*30)

alvo_x = random.randint(-15, 40)
alvo_y = random.randint(-15, 40)

print(f"O inimigo está posicionado em: X = {alvo_x} | Y = {alvo_y}")
print("Digite uma equação em função de 'x' que passe por esse ponto.")

tentativas = 3
while tentativas > 0:
    tiro = input(f"Tentativa {4 - tentativas}/3 - Digite a equação (y = ): ")
    
    try:
        x = alvo_x
        resultado = eval(tiro)
        
        if resultado == alvo_y:
            print(f"Na mosca. O alvo em Y={alvo_y} foi desintegrado!")
            break
        else:
            print(f"eu tiro passou raspando em Y={resultado}. O alvo era {alvo_y}.")
    except Exception:
        print("Equação inválida! Use o formato certo (ex: x**2 + 3).")
    
    tentativas -= 1
    print("-" * 30)

if tentativas == 0:
    print("Fim de jogo. O alvo fugiu!")