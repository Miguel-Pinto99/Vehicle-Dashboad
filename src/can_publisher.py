#!/usr/bin/env python3
from pprint import pprint

import can

import rospy
from std_msgs.msg import String
from can_receiver.msg import Can_msg

import codecs
import time

def convert(bits):

    if len(bits) != 8:
        if len(bits) == 7 :
            bits= '0' + bits
        elif len(bits) == 6 :
            bits= '00' + bits
        elif len(bits) == 5 :
            bits= '000' + bits
        elif len(bits) == 4 :
            bits= '0000' + bits
        elif len(bits) == 3 :
            bits= '00000' + bits
        elif len(bits) == 2 :
            bits= '000000' + bits
        elif len(bits) == 1 :
            bits= '0000000' + bits


    else:
        bits=bits
    return (bits)


def main():

    #bustype = 'socketcan_native'
    bustype = 'socketcan'
    channel= 'vcan0'
    #channel= 'can0'
    bitrate = 500000

    AutonomiaPerc=0
    AutonomiaKm=0
    Mudanca= str('Nada')
    Velocidade=0
    Contador_Km=0
    Carregador=0
    Porta_Condutor=0
    Porta_Outras= 0
    ParaBrisas_Frente = 0
    ParaBrisas_Atras = 0
    Temperatura_AC = 0
    Intensidade_AC = 0
    Btn_Tmax=0
    Btn_Imax=0
    Btn_Solf=0
    Alerta_CintoC=0
    Alerta_CintoP=0
    Pisca_Dir=0
    Pisca_Esq=0
    Medios=0
    Maximos=0

    pub = rospy.Publisher('can_messages', Can_msg, queue_size=10)
    rospy.init_node('can_node', anonymous=True)  # nome do publisher
    rate = rospy.Rate(10)

    while True:
        bus = can.interface.Bus(channel=channel, interface=bustype, bitrate=bitrate)
        message = bus.recv() #LER MENSAGENS DO CAN

        #O DATA É UM BYTEARRAY

        if (message != None):
            if (len(message.data) > 0):
                if (len(message.data) > 0):


                    id =hex(message.arbitration_id)

                    try:
                        B0=(message.data[0])
                        b0=(bin(message.data[0]))[2:]
                        b0=convert(b0)

                    except:
                        pass
                    try:
                        B1=(message.data[1])
                        b1 = (bin(message.data[1]))[2:]
                        b1 = convert(b1)
                    except:
                        pass
                    try:
                        B2=(message.data[2])
                        b2 = (bin(message.data[2]))[2:]
                        b2 = convert(b2)
                    except:
                        pass
                    try:
                        B3=(message.data[3])
                        b3 = (bin(message.data[3]))[2:]
                        b3 = convert(b3)
                    except:
                        pass
                    try:
                        B4=(message.data[4])
                        b4 = (bin(message.data[4]))[2:]
                        b4 = convert(b4)
                    except:
                        pass
                    try:
                        B5=(message.data[5])
                        b5 = (bin(message.data[5]))[2:]
                        b5 = convert(b5)
                    except:
                        pass
                    try:
                        B6=(message.data[6])
                        b6 = (bin(message.data[6]))[2:]
                        b6 = convert(b6)
                    except:
                        pass
                    try:
                        B7=(message.data[7])
                        b7 = (bin(message.data[7]))[2:]
                        b7 = convert(b7)
                    except:
                        pass


                    if id == hex(0x424):
                        if int(b0[2]) == 1:
                            Alerta_CintoC = True
                        else:
                            Alerta_CintoC = False

                        if int(b0[0]) == 1:
                            Alerta_CintoP = True
                        else:
                            Alerta_CintoP = False

                        if int(b2[6]) == 1 :
                            Porta_Condutor = True
                        else:
                            Porta_Condutor = False

                        if int(b2[7]) == 1 :
                            Porta_Outras = True
                        else:
                            Porta_Outras = False

                        if int(b1[4]) == 1 :
                            ParaBrisas_Frente = True
                        else:
                            ParaBrisas_Frente = False

                        if int(b1[3]) == 1 :
                            ParaBrisas_Atras = True
                        else:
                            ParaBrisas_Atras = False



                        if int(b1[6]) == 1 :
                            Pisca_Esq = True
                        else:
                            Pisca_Esq = False

                        if int(b1[7]) == 1 :
                            Pisca_Dir = True
                        else:
                            Pisca_Dir = False

                        if int(b1[1]) == 1 :
                            Medios = True
                        else:
                            Medios = False

                        if int(b1[2]) == 1 :
                            Maximos = True
                        else:
                            Maximos = False





                    if id == hex(0x3A4):
                        Temperatura_AC = int(b0[7]) + int(b0[6])*2 + int(b0[5])*4 + int(b0[4])*8
                        Intensidade_AC = int(b1[7]) + int(b1[6])*2 + int(b1[5])*4 + int(b1[4])*8

                        if int(b0[2]) == 1 :
                            Btn_Tmax = True
                        else:
                            Btn_Tmax = False

                        if int(b0[1]) == 1 :
                            Btn_Solf = True
                        else:
                            Btn_Solf = False

                        if int(b0[0]) == 1 :
                            Btn_Imax = True
                        else:
                            Btn_Imax = False





                    if id == hex(0x412): #Velocity,Range
                        Velocidade = B1
                        Contador_Km = (B2*65536)+(B3*256)+B4
                        #Porta = (B0 & 0b01001000) == 0b01001000




                    if id == hex(0x418): #Mudancas
                        if B0 == 0x50:
                            Mudanca="Park"
                        elif B0 == 0x52:
                            Mudanca="Reverse"
                        elif B0 == 0x4E:
                            Mudanca="Neutral"
                        elif B0 == 0x44:
                            Mudanca="Foward"
                        else:
                            Mudanca=Mudanca



                    if id == hex(0x346): #Range em KM
                        AutonomiaKm=B7



                    if id == hex(0x374): #Range em
                        AutonomiaPerc=(B1-10)/2



                    if id == hex(0x373):
                        EstadoBateria= (((B2)*256)+(B3-128)*128)/100
                        if EstadoBateria < 0 :
                            Carregador= True
                        else:
                            Carregador= False



                #except:
                    #'DATA ERROR'


                Dados = {'Autonomia (%)': AutonomiaPerc,
                          'Autonomia (Km)': AutonomiaKm,
                          'Mudanças': Mudanca,
                          'Velocidade': Velocidade,
                          'Contador de Km': Contador_Km,
                          'Porta_Condutor': Porta_Condutor,
                          'Porta_Outras': Porta_Outras,
                          'Para Brisas Frente': ParaBrisas_Frente,
                          'Para Brisas Atras': ParaBrisas_Atras,
                          'Temperatura AC': Temperatura_AC,
                          'Intensidade AC': Intensidade_AC,
                          'Botão Temp.Max': Btn_Tmax,
                          'Botão Int.Max': Btn_Imax,
                          'Botão Solfagem': Btn_Solf,
                          'Alerta Cinto Passageiro': Alerta_CintoP,
                          'Alerta Cinto Condutor': Alerta_CintoC,
                          'Pisca Direito': Pisca_Dir,
                          'Pisca Esquerdo': Pisca_Esq,
                          'Médios': Medios,
                          'Máximos': Maximos,
                          'Carregador': Carregador}

                pprint(Dados)


        msg = Can_msg()
        msg.autonomia_perc= int(AutonomiaPerc)
        msg.autonomia_km= int(AutonomiaKm)
        msg.contador_km= int(Contador_Km)
        msg.velocidade= int(Velocidade)
        msg.temperatura_ac= int(Temperatura_AC)
        msg.intensidade_ac= int(Intensidade_AC)
        msg.mudanca= str(Mudanca)
        msg.porta_condutor= bool(Porta_Condutor)
        msg.porta_outras = bool(Porta_Outras)
        msg.parabrisas_frente = bool(ParaBrisas_Frente)
        msg.parabrisas_atras = bool(ParaBrisas_Atras)
        msg.btn_tmax = bool(Btn_Tmax)
        msg.btn_imax = bool(Btn_Imax)
        msg.alerta_cintop = bool(Alerta_CintoP)
        msg.alerta_cintoc = bool(Alerta_CintoC)
        msg.pisca_dir = bool(Pisca_Dir)
        msg.pisca_esq = bool(Pisca_Esq)
        msg.medios = bool(Medios)
        msg.maximos = bool(Maximos)
        msg.carregador = bool(Carregador)


        pub.publish(msg)
        #rate.sleep()

if __name__ == '__main__':
    main()