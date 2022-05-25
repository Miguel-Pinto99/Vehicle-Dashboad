#!/usr/bin/env python3
import kivy
import rospy
from std_msgs.msg import String
from can_receiver.msg import Can_msg

from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy_garden.speedmeter import SpeedMeter
from kivy.clock import Clock
from kivymd.uix.card import MDCard
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.graphics.svg import Svg
from kivy.clock import Clock
from datetime import datetime,timedelta

import time
#from kivy.garden.gauge import Gauge


Builder.load_file('build1.kv')

class MyLayout(Widget):

    def __int__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", Can_msg, self.callback)

    def on_start(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", Can_msg, self.callback)

    def callback(self,msg):
        autonomia_perc= msg.autonomia_perc
        autonomia_km= msg.autonomia_km
        contador_km= msg.contador_km
        velocidade= msg.velocidade
        temperatura_ac= msg.temperatura_ac
        intensidade_ac= msg.intensidade_ac
        mudanca= msg.mudanca
        porta_condutor= msg.porta_condutor
        porta_outras= msg.porta_outras
        parabrisas_frente= msg.parabrisas_frente
        parabrisas_atras= msg.parabrisas_atras
        btn_tmax= msg.btn_tmax
        btn_imax= msg.btn_imax
        alerta_cintop= msg.alerta_cintop
        alerta_cintoc= msg.alerta_cintoc
        pisca_dir= msg.pisca_dir
        pisca_esq=msg.pisca_esq
        medios= msg.medios
        maximos= msg.maximos
        carregador= msg.carregador


        self.ids.autonomia_km_label.text = str(autonomia_km)
        self.ids.autonomia_perc_label.text = str(autonomia_perc)
        self.ids.contador_km_label.text = str(contador_km)
        self.ids.velocidade_label.text = str(velocidade)


        if mudanca == "Park" :
            self.ids.icon_mudancas.icon = "alpha-p-box-outline"
        elif mudanca == "Reverse":
            self.ids.icon_mudancas.icon = "alpha-r-box-outline"
        elif mudanca == "Neutral":
            self.ids.icon_mudancas.icon = "alpha-n-box-outline"
        elif mudanca == "Foward":
            self.ids.icon_mudancas.icon = "alpha-f-box-outline"


        if autonomia_perc <=100 and autonomia_perc > 90 and carregador is False:
            self.ids.icon_bateria.icon = "battery"
        elif autonomia_perc <=90 and autonomia_perc > 80 and carregador is False:
            self.ids.icon_bateria.icon = "battery-90"
        elif autonomia_perc <=80 and autonomia_perc > 70 and carregador is False:
            self.ids.icon_bateria.icon = "battery-80"
        elif autonomia_perc <=70 and autonomia_perc > 60 and carregador is False:
            self.ids.icon_bateria.icon = "battery-70"
        elif autonomia_perc <=60 and autonomia_perc > 50 and carregador is False:
            self.ids.icon_bateria.icon = "battery-60"
        elif autonomia_perc <=50 and autonomia_perc > 40 and carregador is False:
            self.ids.icon_bateria.icon = "battery-50"
        elif autonomia_perc <=40 and autonomia_perc > 30 and carregador is False:
            self.ids.icon_bateria.icon = "battery-40"
        elif autonomia_perc <=30 and autonomia_perc > 20 and carregador is False:
            self.ids.icon_bateria.icon = "battery-30"
        elif autonomia_perc <=20 and autonomia_perc > 10 and carregador is False:
            self.ids.icon_bateria.icon = "battery-20"
        elif autonomia_perc <=10 and autonomia_perc >=0  and carregador is False:
            self.ids.icon_bateria.icon = "battery-10"
        elif autonomia_perc <=100 and autonomia_perc > 90 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-100"
        elif autonomia_perc <=90 and autonomia_perc > 80 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-90"
        elif autonomia_perc <=80 and autonomia_perc > 70 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-80"
        elif autonomia_perc <=70 and autonomia_perc > 60 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-70"
        elif autonomia_perc <=60 and autonomia_perc > 50 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-60"
        elif autonomia_perc <=50 and autonomia_perc > 40 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-50"
        elif autonomia_perc <=40 and autonomia_perc > 30 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-40"
        elif autonomia_perc <=30 and autonomia_perc > 20 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-30"
        elif autonomia_perc <=20 and autonomia_perc > 10 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-20"
        elif autonomia_perc <=10 and autonomia_perc >=0 and carregador is True:
            self.ids.icon_bateria.icon = "battery-charging-10"

        if porta_condutor is True or porta_outras is True:
            self.ids.icon_portas.icon = "car-door"
            #Svg("logos/car-door-lock.svg")
            #(source='logos/car-door-lock.png')
        else:
            self.ids.icon_portas.icon = "car-door-lock"


        if medios is True or maximos is True:
            self.ids.lights_icon.icon="car-parking-lights"
        else:
            self.ids.lights_icon.icon = ""


        if pisca_esq is True:
            self.ids.pisca_esq_icon.icon="arrow-left-bold-outline"
        else:
            self.ids.pisca_esq_icon.icon= ""


        if pisca_dir is True:
            self.ids.pisca_dir_icon.icon="arrow-right-bold-outline"
        else:
            self.ids.pisca_dir_icon.icon= ""


        if parabrisas_frente is True or parabrisas_atras:
            self.ids.parabrisas_icon.icon = "car-windshield-outline"
        else:
            self.ids.parabrisas_icon.icon = ""



        if intensidade_ac == 0:
            self.ids.ac_temp_label.text= "Off"
        elif intensidade_ac == 1:
            self.ids.ac_temp_label.text= "Cold-7"
        elif intensidade_ac == 2:
            self.ids.ac_temp_label.text= "Cold-6"
        elif intensidade_ac == 3:
            self.ids.ac_temp_label.text= "Cold-5"
        elif intensidade_ac == 4:
            self.ids.ac_temp_label.text= "Cold-4"
        elif intensidade_ac == 5:
            self.ids.ac_temp_label.text= "Cold-3"
        elif intensidade_ac == 6:
            self.ids.ac_temp_label.text= "Cold-2"
        elif intensidade_ac == 7:
            self.ids.ac_temp_label.text= "Cold-1"
        elif intensidade_ac == 8:
            self.ids.ac_temp_label.text= "Neutral"
        elif intensidade_ac == 9:
            self.ids.ac_temp_label.text= "Hot-1"
        elif intensidade_ac == 10:
            self.ids.ac_temp_label.text= "Hot-2"
        elif intensidade_ac == 11:
            self.ids.ac_temp_label.text= "Hot-3"
        elif intensidade_ac == 12:
            self.ids.ac_temp_label.text= "Hot-4"
        elif intensidade_ac == 13:
            self.ids.ac_temp_label.text= "Hot-5"
        elif intensidade_ac == 14:
            self.ids.ac_temp_label.text= "Hot-5"
        elif intensidade_ac == 15:
            self.ids.ac_temp_label.text= "Hot-7"


        if temperatura_ac == 0:
            self.ids.ac_int_label.text= "Off"
        elif temperatura_ac == 1:
            self.ids.ac_int_label.text= "Level 1"
        elif temperatura_ac == 2:
            self.ids.ac_int_label.text= "Level 2"
        elif temperatura_ac == 3:
            self.ids.ac_int_label.text= "Level 3"
        elif temperatura_ac == 4:
            self.ids.ac_int_label.text= "Level 4"
        elif temperatura_ac == 5:
            self.ids.ac_int_label.text= "Level 5"
        elif temperatura_ac == 6:
            self.ids.ac_int_label.text= "Level 6"
        elif temperatura_ac == 7:
            self.ids.ac_int_label.text= "Level 7"
        elif temperatura_ac == 8:
            self.ids.ac_int_label.text= "Level 8"
        elif temperatura_ac == 9:
            self.ids.ac_int_label.text= "Level 9"
        elif temperatura_ac == 10:
            self.ids.ac_int_label.text= "Level 10"
        elif temperatura_ac == 11:
            self.ids.ac_int_label.text= "Level 11"
        elif temperatura_ac == 12:
            self.ids.ac_int_label.text= "Level 12"
        elif temperatura_ac == 13:
            self.ids.ac_int_label.text= "Level 13"
        elif temperatura_ac == 14:
            self.ids.ac_int_label.text= "Level 14"
        elif temperatura_ac == 15:
            self.ids.ac_int_label.text= "Level 15"

        if btn_imax is True:
            self.ids.icon_ac_imax.icon = "alpha-m-circle"
        else:
            self.ids.icon_ac_imax.icon = ""

        if btn_tmax is True:
            self.ids.icon_solf.icon = "air-filter"
        else:
            self.ids.icon_solf.icon = ""

        #time = time.asctime()

        self.ids.time.title = time.asctime()


    def press(self):

        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", Can_msg, self.callback)


class Gps(MapView):
    pass


class DisplayApp(MDApp):
    time = time.asctime()
    def build(self):


        #Window.borderless = True
        Window.fullscreen = 'auto'

        self.font1="fonts/digital-dream/digital-7.ttf"
        self.font2="fonts/rubik/Rubik-Light.ttf"

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_accent_palette = "Red"

        return MyLayout()

if __name__ == '__main__':
    DisplayApp().run()


