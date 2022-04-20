#!/usr/bin/env python3
from pprint import pprint

import rospy
import can
import codecs
import time

def callback(msg):
    rospy.loginfo('Receive message')

def main():

    #bustype = 'socketcan_native'
    bustype = 'socketcan'
    channel= 'vcan0'
    #channel= 'can0'
    bitrate = 50000

    while True:
        bus = can.interface.Bus(channel=channel, interface=bustype, bitrate=bitrate)
        message = bus.recv() #LER MENSAGENS DO CAN

        #O DATA É UM BYTEARRAY

        if (message != None):
            if (len(message.data) > 0):
                try:
                    id =hex(message.arbitration_id)

                    B0=(message.data[0])
                    B1=(message.data[1])
                    B2=(message.data[2])
                    B3=(message.data[3])
                    B4=(message.data[4])
                    B5=(message.data[5])
                    B6=(message.data[6])
                    B7=(message.data[7])

                    #print(B0)
                    #print(B0)
                    #print(B1)
                    #print(B2)
                    #print(B3)
                    #print(B4)
                    #print(B5)
                    #print(B6)
                    #print(B7)

                    #print(message.data)
                    #int_val = int.from_bytes(message.data, "big")
                    #data= codecs.decode(message.data, 'UTF-8')
                    #print(int_val)
                    #print(data)
                    print(message)

                    #data_bytes = (message.data[0])
                    #data_bites = bin(message.data[0])
                    #print(id)
                    #print(hex(data_bytes)[2:])
                    #print(data_bites)



                    if id == hex(0x412): #Velocity,Range
                        Velocity = B1
                        TotalRange = (B2*65536)+(B3*256)+B4



                    if id == hex(0x418): #Gearbox
                        if B0 == 0x44:
                            Gearbox="Park"
                        elif B0 == 0x4e:
                            Gearbox="Reverse"
                        elif B0 == 0x50:
                            Gearbox="Neutral"
                        elif B0 == 0x11111:
                            Gearbox="Drive"
                        else:
                            Gearbox=Gearbox


                    if id == hex(0x346): #Range em KM
                        RangeKm=B7


                    if id == hex(0x374): #Range em
                        RangePerc=(B1-10)/10


                    if id == hex(0x373):
                        batery_state= (((B2)*256)+(B3-128)*128)/100
                        if batery_state < 0 :
                            Charger= "charging"
                        else:
                            Charger=" not charging"


                    Dados = {'Range (%)': RangePerc,
                              'Range (Km)': RangeKm,
                              'Mudanças': Gearbox,
                              'Velocidade': Velocity,
                              'Contador de Km': TotalRange,
                              'Carregador': Charger}

                    pprint(Dados)
                except:
                    print('Erro a guardar Dados')


    #can.Message(arbitration_id=123, is_extended_id=True,
    #           data=[0x11, 0x22, 0x33])


    #rospy.init_node('can_receiver', anonymous=True)
    #rospy.Subscriber("CAN_RAW", String, callback)
    #rospy.spin()

if __name__ == '__main__':
    main()
