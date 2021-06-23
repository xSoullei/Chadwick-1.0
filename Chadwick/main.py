#!/usr/bin/env pybricks-micropython

#______________________________________________________________________________________________________________________________________
#IMPORTANDO BIBLIOTECAS:
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#INICIALIZAÇÃO DO EV3, PORTAS E BASE DO ROBÔ:
ev3 = EV3Brick()
sensorUltrassonico_garra = UltrasonicSensor(Port.S1) # <--Declaração do sensor ultrassonico da garra
sultrassonico_dianteiro = UltrasonicSensor(Port.S1) # <-- Declaração do sensor ultrassonico dianteiro
scor_direita = ColorSensor(Port.S4) # <-- Declaração do sensor de cor do lado direito
scor_esquerda = ColorSensor(Port.S3) # <-- Declaração do sensor de cor do lado esquerdo
motor_esquerdo = Motor(Port.B) # <-- Declaração do motor esquerdo
motor_direito = Motor(Port.A) # <-- Declaração do motor direito
motor_garra = Motor(Port.A) # <-- Declaração do motor da garra
robo = DriveBase(motor_esquerdo, motor_direito, wheel_diameter=65.5, axle_track=195) #Declaração da base do robô
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#PARÂMETROS PADRÕES:
ev3.speaker.beep() # <-- Beep para indicar a inicialização do programa
preto = 9 # <-- Porcentagem máxima de luminosidade para preto.
branco = 85 # <-- Porcentagem mínima de luminosidade para branco.
verde = [5, 15] # <-- Luminosidade para verde em RGB
velocidade_padrao = -250 # <-- Velocidade padrão.
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#DECLARAÇÃO DO ÍNDICE DAS CORES:
sem_cor = int(0) # <--  Nennhuma cor identificada = 0
preto = int(1) # <--    Preto identificado = 1
azul = int(2) # <--     Azul identificado = 2
verde = int(3) # <--    Verde identificado = 3
amarelo = int(4) # <--  Amarelo identificado = 4
vermelho = int(5) # <-- Vermelho identificado = 5
branco = int(6) # <--   Branco identificado = 6
marrom = int(7) # <--   Marrom identificado = 7
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO PARA VERIFICA OBSTÁCULO TRASEIRO:
def verificaParedeTraseira():
    if sultrassonico_traseiro.distance() <= 70: # <-- Se a distancia do sensor ultrassonico traseiro >= 7cm, faça:
        robo.turn(100) # <-- Robô vira 100°
        main() # <-- Chama a função principal
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO CAPTURA VÍTIMA:
def capturaVitima():
    if sultrassonico_dianteiro.distance() <= 70:
        robo.turn(180) # <-- Robô vira 180°
        motor_garra.turn(180) # <-- Garra gira 180° (desce)
        robo.turn(90) # <-- Robô vira 90°
        main() # <-- Chama a função principal

#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO VERIFICA OBSTÁCULO:
def verificaObstaculo():
    if sultrassonico_dianteiro.distance() <= 70: # <-- Se a distancia do sensor ultrassonico dianteiro >= 7cm, faça:
        desviaObstaculo() # <-- Chama a função desviar obstáculo
    else: # <-- Senão, faça:
        pass # <-- Passe
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO VERIFICA VERDE:
def verificaVerde()
    if scor_esquerda.color() == verde: # <-- Se o verde for detectado na esquerda, faça:
        x_direcao = 0 # <-- Variável para indicar lado esquerdo
        encruzilhada(x_direcao) # <-- Chamada da função encruzilhada, com esquerda como parâmetro
    elif scor_direita.color() == verde: # <-- Se o verde for detectado na direita, faça:
        x_direcao = 1 # <-- Variável para indicar lado direito
        encruzilhada(x_direcao) # <-- Chamada da função encruzilhada, com direita como parâmetro
    else: # <-- Caso nenhuma cor seja identificada, faça:
        pass # <-- Passe
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO SEGUIR LINHA:
def seguirLinha():
    robo.stop()
    ev3.speaker.beep() # <-- Beep para indicar a inicialização de uma nova função
    while True: # <-- Loop
        while not scor_direita.reflection() <= preto: # <-- Enquanto a cor ESQUERDA NÃO FOR PRETO, faça:
            motor_direito.run(velocidade_padrao * 0.5)  # <-- Motor direito com metade da potência
            motor_esquerdo.run(velocidade_padrao) # <-- Motor esquerdo rodando na força padrão       

            verificaObstaculo() # <-- Verificação contínua de possíveis obstáculos
            verificaVerde() # <-- Verificação contínua de possível verde
            
        while not scor_esquerda.reflection() <= preto: # <-- Enquanto a cor DIREITA NÃO FOR PRETO, faça:
            motor_direito.run(velocidade_padrao) # <-- Motor direito rodando na força padrão
            motor_esquerdo.run(velocidade_padrao * 0.5) # <-- Motor esquerdo com metade da potência

            verificaObstaculo() # <-- Verificação contínua de possíveis obstáculos
            verificaVerde() # <-- Verificação contínua de possível verde
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO DESVIAR DE OBSTÁCULOS:
def desviaObstaculo():

    ev3.speaker.beep() # <-- Beep para indicar a inicialização de uma nova função
    robo.straight(100) # <-- Robô recua 10cm
    robo.turn(90) # <-- Robô vira 90°
    robo.straight(-100) # <-- Robô avança 10 cm
    while True: # <-- Loop
        while not (scor_esquerda.reflection() <= preto) or (scor_direita.reflection() <= preto): # <-- Enquanto os sensores não identificarem preto, faça:
            robo.drive(-200 ,-30) # <-- Curva com velocidade 200 e angulação 30°
            if scor_esquerda.reflection() <= 20 or scor_direita.reflection() <= 20: # <-- Se os sensores identificarem preto, faça:
                robo.turn(110) # <-- # <-- Robô vira 110°, para ajustar-se na linha
                main() # <-- Chama a função principal
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO ENCRUZILHADA:
def encruzilhada(direcao):
    ev3.speaker.beep() # <-- Beep para indicar a inicialização de uma nova função
    if direcao == 0: # <-- Se o verde for detectado na esquerda, faça:
        while not (scor_esquerda.reflection() <= preto) or (scor_direita.reflection() <= preto): # <-- Enquanto os sensores não identificarem preto, faça:
            robo.drive(-80 ,60) #Robô inicia curva com velocidade 80 e angulação 60°
        if scor_esquerda.reflection() <= preto or scor_direita.reflection() <= preto:# <-- Se os sensores identificarem preto, faça:
                robo.turn(110) # <-- Robô vira 110°, para ajustar-se na linha
                main() # <-- Chama a função principal
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO PRINCIPAL:
def main():
    ev3.speaker.beep() # <-- Beep para indicar a inicialização de uma nova função
    seguirLinha()
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#FUNÇÃO PARA TESTES:
def teste():    
    pass
#______________________________________________________________________________________________________________________________________

#______________________________________________________________________________________________________________________________________
#PROGRAMA PRINCIPAL:
ev3.speaker.beep(5) # <-- Beep para indicar a inicialização do programa principal
main() # <-- Chamada da função principal
teste() # <-- Chamada da função de testes
#______________________________________________________________________________________________________________________________________