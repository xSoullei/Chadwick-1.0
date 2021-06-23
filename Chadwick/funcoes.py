from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

#Inicialização <
ev3 = EV3Brick()
#sensorUltrassonico_garra = UltrasonicSensor(Port.S1) #Declaração do sensor ultrassonico da garra
sultrassonico_dianteiro = UltrasonicSensor(Port.S1)
scor_direita = ColorSensor(Port.S4)
scor_esquerda = ColorSensor(Port.S3)
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.A)
robo = DriveBase(motor_esquerdo, motor_direito, wheel_diameter=65.5, axle_track=195) #Declaração da base do robô
#>

#FUNÇÃO SEGUIR LINHA:
def seguirLinha():
    robo.stop()
    ev3.speaker.beep() # <-Beep para indicar a inicialização de uma nova função
    while True: # <-Loop
        verificaPretoEsquerda() 
        verificaObstaculo()
        verificaPretoDireita()
        verificaObstaculo()
##
#FUNÇÃO VERIFICA ESQUERDA SENSOR ESQUERDO:
def verificaPretoEsquerda():
    while not (scor_esquerda.rgb()[0] >= 0) and (scor_esquerda.rgb*(1)[0] <= 7) and (scor_esquerda.rgb()[1] >= 0) and (scor_esquerda.rgb*(1)[1] <= 7) and (scor_esquerda.rgb()[2] >= 0) and (scor_esquerda.rgb*(1)[2] <= 7): # <-Enquanto a cor ESQUERDA NÃO FOR PRETO, faça:
            motor_direito.run(velocidade_padrao * 0)  # <-Motor direito desativado
            motor_esquerdo.run(velocidade_padrao) # <-Motor esquerdo rodando na força padrão
##
#FUNÇÃO VERIFICA ESQUERDA SENSOR DIREITO:
def verificaPretoDireita():
    while not (scor_esquerda.rgb()[0] >= 0) and (scor_direita.rgb*(1)[0] <= 7) and (scor_direita.rgb()[1] >= 0) and (scor_direita.rgb*(1)[1] <= 7) and (scor_direita.rgb()[2] >= 0) and (scor_direita.rgb*(1)[2] <= 7): # <-Enquanto a cor ESQUERDA NÃO FOR PRETO, faça:
            motor_direito.run(velocidade_padrao * 0)  # <-Motor direito desativado
            motor_esquerdo.run(velocidade_padrao) # <-Motor esquerdo rodando na força padrão
#FUNÇÃO VERIFICA OBSTÁCULOS:
def verificaObstaculo():
    if sultrassonico_dianteiro.distance() <= 70: #Se a distancia do sensor ultrassonico dianteiro >= 5cm, faça:
        desviaObstaculo() #Chama a função desviar obstáculo
    else:
        pass
##
#FUNÇÃO DESVIAR DE OBSTÁCULOS:
def desviaObstaculo():
    pass
    #ev3.speaker.beep() # <-Beep para indicar a inicialização de uma nova função
    #robo.straight(100)
    #robo.turn(90)
    #robo.straight(-100)
    #while True: # <-Loop
        #while not (scor_esquerda.reflection() <= preto) or (scor_direita.reflection() <= preto):
            #robo.drive(-200 ,-30)
            #if scor_esquerda.reflection() <= 20 or scor_direita.reflection() <= 20:
                #robo.turn(110)
                #main()
##
#FUNÇÃO ENCRUZILHADA:
def encruzilhada(direcao):
    pass