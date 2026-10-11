# Simulador do Paradoxo de Monty Hall

## O que é o paradoxo de Monty Hall?

Conforme o google é:

> É um famoso problema de probabilidade baseado em um programa de TV americano, onde trocar de porta dobra a sua chance de ganhar o prêmio.

Ou seja, imagine que você está em um quadro de programa de TV (Estilo Silvio Santos), nesse quadro em 3 portas na sua frente [1], [2] e [3]. Atrás de uma tem um carro zero km, e nas outras duas tem cabras.

Vamos supor que você escolhe a porta [1]. O apresentador, que sabe exatamente onde está o carro, vai lá e abre a porta [3], revelando uma cabra, ele te olha e faz a seguinte pergunta: "Você quer manter a porta [1] ou quer trocar pra porta [2]?"

O mais comum de se pensar é que agora a chance de conseguir o carro é 50/50, mas isso está incorreto. Steve Selvin provou por esse paradoxo que se você trocar de porta, suas chances de ganhar dobram, ou seja, na primeira escolha vocÊ tinha 33,333...% de chance de acertar, mas ao trocar de porta você soma essa chance e agora tem 66,666...% de chance.

## O que esse código mostra?

Como foi dito antes, o mais comum é acreditar que as novas chances são 50/50, então esse script simula esse jogo milhares de vezes e faz o calculo para mostrar como esse paradoxo é real.

### Funções
&emsp; Simulação limitada a 5.000.000 para não foçar demais o PC.

&emsp; Modo de depuração caso queira ver cada resultado individualmente.

## O que é necessario instalar e como rodar

Clone o repositório ou baixe o arquivo `main.py`.

A unica biblioteca externa que usei for a `colorama`, para instalar ela use o comando abaixo no seu terminal python.

```
pip install colorama
```

Para rodar o script, cole o seguinte comando dentro do seu terminal (Lembre-se de estar dentro da pasta correta):
```
python main.py
```

# Simulador do Paradoxo de Monty Hall

## O que é o paradoxo de Monty Hall?

Conforme o google é:

> É um famoso problema de probabilidade baseado em um programa de TV americano, onde trocar de porta dobra a sua chance de ganhar o prêmio.

Ou seja, imagine que você está em um quadro de programa de TV (Estilo Silvio Santos), nesse quadro em 3 portas na sua frente [1], [2] e [3]. Atrás de uma tem um carro zero km, e nas outras duas tem cabras.

Vamos supor que você escolhe a porta [1]. O apresentador, que sabe exatamente onde está o carro, vai lá e abre a porta [3], revelando uma cabra, ele te olha e faz a seguinte pergunta: "Você quer manter a porta [1] ou quer trocar pra porta [2]?"

O mais comum de se pensar é que agora a chance de conseguir o carro é 50/50, mas isso está incorreto. Steve Selvin provou por esse paradoxo que se você trocar de porta, suas chances de ganhar dobram, ou seja, na primeira escolha vocÊ tinha 33,333...% de chance de acertar, mas ao trocar de porta você soma essa chance e agora tem 66,666...% de chance.

## O que esse código mostra?

Como foi dito antes, o mais comum é acreditar que as novas chances são 50/50, então esse script simula esse jogo milhares de vezes e faz o calculo para smostrar como esse paradoxo é real.

### Funções
&emsp; Simulação limitada a 5.000.000 para não foçar demais o PC.

&emsp; Modo de depuração caso queira ver cada resultado individualmente.

## O que é necessario instalar e como rodar

Clone o repositório ou baixe o arquivo `main.py`.

A unica biblioteca externa que usei for a `colorama`, para instalar ela use o comando abaixo no seu terminal python.

```
pip install colorama
```

Para rodar o script, cole o seguinte comando dentro do seu terminal (Lembre-se de estar dentro da pasta correta):
```
python main.py
```
