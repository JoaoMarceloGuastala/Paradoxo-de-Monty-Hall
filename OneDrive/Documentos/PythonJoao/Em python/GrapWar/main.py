import random
import time
from colorama import Fore, Style

LARGURA = 20
ALTURA = 12

# Sorteia as posições no início da partida

p_x, p_y = random.randint(0, 4), random.randint(0, ALTURA)
e_x, e_y = random.randint(15, LARGURA), random.randint(0, ALTURA)



vida_jogador = 3
vida_inimigo = 3

def renderizar_grade(trajetoria=[], tiro_inimigo=False):
    print("\n    " + "".join([f"{x:<3}" for x in range(LARGURA + 1)]))
    print("  +" + "-" * (LARGURA * 3 + 2))
    
    for y in range(ALTURA, -1, -1):
        linha = f"{y:<2}| "
        for x in range(LARGURA + 1):
            if x == p_x and y == p_y:
                linha += f"{Fore.GREEN}P  {Style.RESET_ALL}"
            elif x == e_x and y == e_y:
                linha += f"{Fore.RED}E  {Style.RESET_ALL}"
            elif (x, y) in trajetoria:
                # O tiro do inimigo deixa um rastro de 'x', o seu de '*'
                linha += f"{Fore.YELLOW}x  {Style.RESET_ALL}" if tiro_inimigo else f"{Fore.BLUE}*  {Style.RESET_ALL}"
            else:
                linha += ".  "
        print(linha)
    print("  +" + "-" * (LARGURA * 3 + 2) + "\n")

print("="*50)
print("🎯 GRAPHWAR ASCII: O DUELO FINAL")
print("="*50)
print("A regra é clara: A equação OBRIGATORIAMENTE tem que passar por você (P)!")
print(f"Você está posicionado em: X = {p_x} | Y = {p_y}")
print(f"O inimigo está posicionado em: X = {e_x} | Y = {e_y}")

while vida_jogador > 0 and vida_inimigo > 0:
    print(f"❤️  Sua vida: {vida_jogador}  |  🤖 Vida Inimigo: {vida_inimigo}")
    renderizar_grade()
    
    # --- SEU TURNO ---
    tiro = input(f"Sua vez! Digite a equação (X={p_x}, Y={p_y}):\n>>> y = ")
    
    trajetoria = []
    acertou_inimigo = False
    tiro_valido = False
    
    try:
        # TESTE DE ORIGEM: O tiro realmente saiu de você?
        x = p_x
        y_origem = eval(tiro)
        
        if round(y_origem) == p_y:
            tiro_valido = True
            for x in range(LARGURA + 1):
                y = int(eval(tiro))
                if 0 <= y <= ALTURA: 
                    trajetoria.append((x, y))
                if x == e_x and y == e_y:
                    acertou_inimigo = True
        else:
            print(f"\n⚠️ TRAPAÇA DETECTADA! Com X={p_x}, sua equação bateu no Y={round(y_origem)}.")
            print(f"O tiro precisa sair exatamente da sua origem em Y={p_y}!")
    except Exception:
        print("\n⚠️ Arma engasgou! Equação inválida.")
        
    if tiro_valido:
        renderizar_grade(trajetoria)
        if acertou_inimigo:
            print("💥 KABUM! Na fuça do robô!")
            vida_inimigo -= 1
        else:
            print("💨 Passou no vácuo!")
            
    if vida_inimigo <= 0:
        break
        
    # --- TURNO DO INIMIGO ---
    print("-" * 50)
    print("🤖 O Inimigo está calculando a parábola da vingança...")
    time.sleep(2)
    
    # IA burra/esperta: O robô tenta achar o coeficiente angular (a) entre vocês dois
    # Coloquei uma chance de ele errar o cálculo em 1 ou 2 blocos de altura
    erro = random.choice([-2, -1, 0, 0, 1, 2]) 
    
    delta_y = (p_y + erro) - e_y 
    delta_x = p_x - e_x
    a = delta_y / delta_x
    b = e_y - (a * e_x)
    
    # O robô atira de volta usando os coeficientes que calculou
    traj_inimigo = []
    acertou_jogador = False
    
    for x in range(LARGURA + 1):
        y = int(round((a * x) + b))
        if 0 <= y <= ALTURA:
            traj_inimigo.append((x, y))
        if x == p_x and y == p_y:
            acertou_jogador = True
            
    # O inimigo desenha o rastro do tiro dele
    renderizar_grade(traj_inimigo, tiro_inimigo=True)
    print(f"🤖 Inimigo atirou usando: y = ({a:.2f})*x + ({b:.2f})")
    
    if acertou_jogador:
        print("🔥 BOOM! Você foi pego em cheio!")
        vida_jogador -= 1
    else:
        print("🛡️ Sorte que esse robô é míope, passou raspando!")
        
    print("="*50)

    # --- O PULO DO GATO: CORRERIA GERAL ---
    # Se os dois ainda estiverem vivos, todo mundo muda de lugar para o próximo turno
    if vida_jogador > 0 and vida_inimigo > 0:
        print("🏃‍♂️💨 Recarregando armas e trocando de posição...\n")
        time.sleep(2)
        p_x, p_y = random.randint(0, 4), random.randint(0, ALTURA)
        e_x, e_y = random.randint(15, LARGURA), random.randint(0, ALTURA)

# --- RESULTADO FINAL ---   
if vida_jogador <= 0:
    print("💀 GAME OVER! O robô mandou abraços. Hora de dormir.")
else:
    print("🏆 VITÓRIA! O cérebro humano ganha mais uma.")