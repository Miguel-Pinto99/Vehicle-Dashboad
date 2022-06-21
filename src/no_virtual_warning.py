#!/usr/bin/env python3
import sys

import rospy
from std_msgs.msg import String
from can_receiver.msg import Can_msg
from can_receiver.msg import Warning_msg
import time
import readchar
import cv2


def main():

    pub = rospy.Publisher('warning_messages', Warning_msg, queue_size=10)
    warn=Warning_msg()

    warn.carregar=False
    warn.porta=False
    warn.cinto=False
    warn.ac=False
    warn.reverse=False
    warn.autonomia=False
    warn.limite_velocidade=False
    warn.proximidade=False

    while True:

        key = readchar.readkey()

        if key == -1:
            pass

        if key == ('i'):
            warn.carregar = True

        if key == ('o'):
            warn.carregar = False

        if key == ('k'):
            warn.porta = True

        if key == ('l'):
            warn.porta = False


        if key == ('n'):
            warn.cinto = True

        if key == ('m'):
            warn.cinto = False

        if key == ('w'):
            warn.ac = True

        if key == ('e'):
            warn.ac = False


        if key == ('s'):
            warn.reverse = True

        if key == ('d'):
            warn.reverse = False


        if key == ('x'):
            warn.autonomia = True

        if key == ('c'):
            warn.autonomia = False


        if key == ('r'):
            warn.limite_velocidade = True

        if key == ('t'):
            warn.limite_velocidade = False

        if key == ('f'):
            warn.proximidade = True

        if key == ('g'):
            warn.proximidade = False

        if key == ('q'):
            print('You pressed "q" (quit). Program Finished!')
            exit()

        print(warn)
        pub.publish(warn)



if __name__ == '__main__':
    rospy.init_node('no_virtual_warning', anonymous=True)
    main()



