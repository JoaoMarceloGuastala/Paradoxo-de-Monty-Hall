import keyboard
import time

texto = """O Brasil é reconhecido como uma das maiores potências do agronegócio. No entanto, esse destaque custa caro para o meio ambiente causando desgaste do solo e poluição das águas. Para que o país tenha um futuro sustentável, é preciso encontrar um equilíbrio entre produzir e preservar a natureza. Esse desafio acontece, principalmente, pela falta de reaproveitamento de recursos e pela dificuldade de acesso à tecnologia limpa no campo.

Em primeiro lugar, é preciso mudar a ideia de que o setor agrícola só deve extrair da natureza. Um bom exemplo de inovação acontece no estado do Paraná onde empresas de saneamento transformam o lodo do esgoto tratado em adubo para as plantações. Essa prática não só melhora a qualidade da terra para o plantio, mas também resolve o problema do descarte do lixo urbano. Porém, por falta de incentivo do governo e de informação, ideias boas como essa não chegam a todas as fazendas do Brasil.

Além disso, a desigualdade financeira é um grande obstáculo para a sustentabilidade. Enquanto as grandes empresas do agronegócio conseguem investir em tecnologias modernas e ecológicas para exportar mais, os pequenos e médios produtores rurais não tem condição para isso. Sem apoio esses trabalhadores acabam dependendo de adubos químicos e métodos antigos que prejudicam a terra e a água a longo prazo, dificultando a preservação ambiental.

Portanto, medidas são necessárias para garantir a produtividade agrícola sem destruir a natureza. O Ministério da Agricultura e Pecuária, em parceria com os governos estaduais, deve criar um programa de incentivo sustentável. Essa ação vai oferecer ajuda financeira e cursos práticos para que os pequenos produtores aprendam a usar alternativas mais ecológicas, como o adubo feito de resíduos urbanos. Com esse apoio, será possível manter o agro forte e, ao mesmo tempo, proteger o nosso planeta para as próximas gerações."""

# Pausa para você trocar de tela e clicar onde o Python deve começar a digitar
print("Você tem 5 segundos para clicar na caixa de texto...")
time.sleep(5)

# A função write do 'keyboard' simula a digitação perfeita, respeitando acentos e parágrafos
# O delay=0.02 significa que ele vai esperar 0.02 segundos entre cada tecla (parece um humano digitando rápido)
keyboard.write(texto, delay=0.02)

print("Digitação concluída!")