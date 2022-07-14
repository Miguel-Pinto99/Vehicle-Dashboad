#!/usr/bin/env python3
import kivy
import rospy
from std_msgs.msg import String
from can_receiver.msg import Can_msg
from can_receiver.msg import Warning_msg

from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton,\
    MDRoundFlatButton
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.uix.videoplayer import VideoPlayer
import time

from kivy.uix.screenmanager import ScreenManager, Screen





class MyLayout(Screen):


#------------------------------------------------------------------
# ------------- Inicialização dos nós -----------------------------
#------------------------------------------------------------------

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Start timer
        Clock.schedule_once(self.start)


    def start(self,dt):

        rospy.init_node('dashboard_node', anonymous=True)
        rospy.Subscriber('warning_messages', Warning_msg, self.callback1)
        rospy.Subscriber("can_messages", Can_msg, self.callback2)
        global notification

        #Inicialize variables
        self.notification=True

        self.espera1 = False
        self.espera2 = False
        self.espera3 = False
        self.espera4 = False
        self.contagem=0


#------------------------------------------------------------------
#---- Frist calback: Mensages Warnings ----------------------------
#------------------------------------------------------------------

    def callback1(self,msg):


        global notification
        self.notification= notification
        # Inicialize variables with data from the messages
        self.warn_carregar=msg.carregar
        self.warn_porta=msg.porta
        self.warn_cinto=msg.cinto
        self.warn_ac=msg.ac
        self.warn_reverse=msg.reverse
        self.warn_autonomia=msg.autonomia
        self.warn_velocidade= msg.limite_velocidade
        self.warn_proximidade=msg.proximidade

        # Set color theme of the window
        self.cor_clara = [0.0, 0.0, 0.0, 0.12]
        self.cor_escura = [1.0, 1.0, 1.0, 0.12]
        self.cor_vermelha = [1.0, 0.0, 0.0, 0.6]

        if self.ids.mdcard1.md_bg_color == self.cor_escura:
            self.fundo_escuro = True
        elif self.ids.mdcard1.md_bg_color == self.cor_clara:
            self.fundo_escuro = False

        #Change screen
        if self.warn_reverse is True :
            Clock.schedule_once(self.changescreen1)
        else:
            Clock.schedule_once(self.changescreen2)

        if self.warn_proximidade is True :
            Clock.schedule_once(self.changescreen3)
        else:
            Clock.schedule_once(self.changescreen4)


        #Warnings and Pop-ups
        if self.notification is True:

            if self.warn_carregar is True and self.espera1 is False:
                #self.espera1= True
                #Clock.schedule_once(self.show_alert_dialog1)
                self.ids.warnings.text = "Vehicle Charging"
                self.warn_background()


            if self.warn_porta is True and self.espera1 is False:
                #self.espera1 = True
                #Clock.schedule_once(self.show_alert_dialog2)
                self.ids.warnings.text = "Close the door"
                self.warn_background()



            if self.warn_cinto is True and self.espera1 is False:
                #self.espera1 = True
                #Clock.schedule_once(self.show_alert_dialog3)
                self.ids.warnings.text = "Seat belt"
                self.warn_background()



            if self.warn_ac is True and self.espera1 is False:
                self.espera1 = True
                Clock.schedule_once(self.show_alert_dialog4)



            if self.warn_autonomia is True and self.espera4 is False:
                self.espera4 = True
                Clock.schedule_once(self.show_alert_dialog6)



            if self.autonomia_perc > 11 and self.espera4 is True:
                self.espera4 = False




            if self.warn_velocidade is True and self.espera3 is False:
                self.espera3 = True

                self.cor_clara = [0.0, 0.0, 0.0, 0.12]
                self.cor_escura = [1.0, 1.0, 1.0, 0.12]
                self.cor_vermelha = [1.0, 0.0, 0.0, 0.6]


                if self.ids.mdcard1.md_bg_color == self.cor_escura:
                    self.fundo_escuro=True
                elif self.ids.mdcard1.md_bg_color == self.cor_clara:
                    self.fundo_escuro=False

                Clock.schedule_once(self.vel_warn1,0.85)
                Clock.schedule_once(self.play_sound1,0.85)

            elif self.warn_velocidade is False:
                if self.fundo_escuro:
                    self.ids.mdcard_velocidade.md_bg_color = self.cor_escura
                else:
                    self.ids.mdcard_velocidade.md_bg_color = self.cor_clara



        if self.warn_carregar is False and self.warn_cinto is False and self.warn_porta is False:
            if self.fundo_escuro is True:
                self.ids.mdcard_warns.md_bg_color = self.cor_escura
                self.ids.warnings.text = ""
            else:
                self.ids.mdcard_warns.md_bg_color = self.cor_clara
                self.ids.warnings.text = ""


    #Function that makes the background color of the warnings module
    def warn_background(self):
        self.espera1 = True
        Clock.schedule_once(self.warn_warn2, 0.85)
        Clock.schedule_once(self.play_sound1, 0.85)


#------------------------------------------------------------------
#------------- Segundo calback: Mensagens CAN----------------------
#------------------------------------------------------------------

    def callback2(self,msg):

        #Store variables from message
        autonomia_perc= msg.autonomia_perc
        autonomia_km= msg.autonomia_km
        contador_km= msg.contador_km
        velocidade= msg.velocidade
        temperatura_ac= msg.temperatura_acz
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

        self.autonomia_perc = msg.autonomia_perc
        self.contador_km = msg.contador_km

        self.ids.autonomia_km_label.text = str(autonomia_km)
        self.ids.autonomia_perc_label.text = str(autonomia_perc)
        self.ids.contador_km_label.text = str(contador_km)
        self.ids.velocidade_label.text = str(velocidade)

        self.manager.get_screen("reverse_screen").ids.velocidade_label2.text = str(velocidade)
        self.manager.get_screen("reverse_screen").ids.dist3.text = str(autonomia_perc)
        self.manager.get_screen("close_screen").ids.velocidade_label3.text = str(velocidade)
        self.manager.get_screen("close_screen").ids.dist4.text = str(autonomia_perc)
        self.manager.get_screen("close_screen").ids.icon_mudancas1.icon = self.ids.icon_mudancas.icon

        #Shift position icon
        if mudanca == "Park" :
            self.ids.icon_mudancas.icon = "alpha-p-box-outline"
        elif mudanca == "Reverse":
            self.ids.icon_mudancas.icon = "alpha-r-box-outline"
        elif mudanca == "Neutral":
            self.ids.icon_mudancas.icon = "alpha-n-box-outline"
        elif mudanca == "Foward":
            self.ids.icon_mudancas.icon = "alpha-d-box-outline"

        #Battery icon
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

        #Door icon
        if porta_condutor is True or porta_outras is True:
            self.ids.icon_portas.icon = "car-door"
        else:
            self.ids.icon_portas.icon = ""

        #Lights icon
        if medios is True or maximos is True:
            self.ids.lights_icon.icon="car-parking-lights"
        else:
            self.ids.lights_icon.icon = ""

        #Lights icon
        if pisca_esq is True:
            self.ids.pisca_esq_icon.icon="arrow-left-bold-outline"
        else:
            self.ids.pisca_esq_icon.icon= ""

        #Blinkers icon
        if pisca_dir is True:
            self.ids.pisca_dir_icon.icon="arrow-right-bold-outline"
        else:
            self.ids.pisca_dir_icon.icon= ""

        #Windshield icon
        if parabrisas_frente is True or parabrisas_atras:
            self.ids.parabrisas_icon.icon = "car-windshield-outline"
        else:
            self.ids.parabrisas_icon.icon = ""


        #AC icons and labels
        if temperatura_ac == 0:
            self.ids.ac_temp_label.text= "Off"
        elif temperatura_ac == 1:
            self.ids.ac_temp_label.text= "Cold-6"
        elif temperatura_ac == 2:
            self.ids.ac_temp_label.text= "Cold-5"
        elif temperatura_ac == 3:
            self.ids.ac_temp_label.text= "Cold-4"
        elif temperatura_ac == 4:
            self.ids.ac_temp_label.text= "Cold-3"
        elif temperatura_ac == 5:
            self.ids.ac_temp_label.text= "Cold-2"
        elif temperatura_ac == 6:
            self.ids.ac_temp_label.text= "Cold-1"
        elif temperatura_ac == 7:
            self.ids.ac_temp_label.text= "Neutral"
        elif temperatura_ac == 8:
            self.ids.ac_temp_label.text= "Hot-1"
        elif temperatura_ac == 9:
            self.ids.ac_temp_label.text= "Hot-2"
        elif temperatura_ac == 10:
            self.ids.ac_temp_label.text= "Hot-3"
        elif temperatura_ac == 11:
            self.ids.ac_temp_label.text= "Hot-4"
        elif temperatura_ac == 12:
            self.ids.ac_temp_label.text= "Hot-5"
        elif temperatura_ac == 13:
            self.ids.ac_temp_label.text= "Hot-6"

        if intensidade_ac == 0:
            self.ids.ac_int_label.text= "Off"
        elif intensidade_ac == 1:
            self.ids.ac_int_label.text= "Level 1"
        elif intensidade_ac == 2:
            self.ids.ac_int_label.text= "Level 2"
        elif intensidade_ac == 3:
            self.ids.ac_int_label.text= "Level 3"
        elif intensidade_ac == 4:
            self.ids.ac_int_label.text= "Level 4"
        elif intensidade_ac == 5:
            self.ids.ac_int_label.text= "Level 5"
        elif intensidade_ac == 6:
            self.ids.ac_int_label.text= "Level 6"
        elif intensidade_ac == 7:
            self.ids.ac_int_label.text= "Level 7"
        elif intensidade_ac == 8:
            self.ids.ac_int_label.text= "Level 8"

        if btn_imax is True:
            self.ids.icon_ac_imax.icon = "alpha-m-circle"
        else:
            self.ids.icon_ac_imax.icon = ""

        if btn_tmax is True:
            self.ids.icon_solf.icon = "air-filter"
        else:
            self.ids.icon_solf.icon = ""


#------------------------------------------------------------------
# ---- Warning messages and PopUps ------------------------------------
#------------------------------------------------------------------
    dialog1 = None
    dialog2 = None
    dialog3 = None
    dialog4 = None
    dialog5 = None
    dialog6 = None

    def show_alert_dialog1(self, dt):
        if not self.dialog1:
            self.dialog1 = MDDialog(
                auto_dismiss= False,
                title="Warning",
                text="Veiculo a carregar. Coloque em ponto morto!",
                buttons=[
                    MDRectangleFlatButton(
                        text="Close",
                        on_release=self.close_dialog1,
                        text_color= (1, 1, 1, 1),
                        line_color=(1, 1, 1, 1),
                    ),
                ],
            )
        self.play_sound2()
        self.dialog1.open()


    def show_alert_dialog2(self, dt):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                auto_dismiss= False,
                title="Warning",
                text= "Veiculo em andamento. Feche as portas!",
                buttons=[
                    MDRectangleFlatButton(
                        text="Close",
                        on_release=self.close_dialog2
                    ),
                ],
            )
        self.play_sound2()
        self.dialog2.open()

    def show_alert_dialog3(self, dt):
        if not self.dialog3:
            self.dialog3 = MDDialog(
                auto_dismiss= False,
                title="Warning",
                text= "Veiculo em andamento. Coloque o Cinto!",
                buttons=[
                    MDRectangleFlatButton(
                        text="Close",
                        on_release=self.close_dialog3
                    ),
                ],
            )
        self.play_sound2()
        self.dialog3.open()

    def show_alert_dialog4(self, dt):
        if not self.dialog4:
            self.dialog4 = MDDialog(
                auto_dismiss= False,
                title="Warning",
                text= "Low autonomy. Turn off the air conditioner!",
                buttons=[
                    MDRectangleFlatButton(
                        text="Close",
                        on_release=self.close_dialog4
                    ),
                ],
            )
        self.play_sound2()
        self.dialog4.open()


    def show_alert_dialog5(self, dt):
        self.popup = Popup(
            title='Câmara Traseira',
            content=VideoPlayer(source="video/reverse.webm",state='play',
                                options={'allow_stretch': True,
                                         'eos': 'loop'},
                                ),
            size_hint=(None, None),
            size=(800, 800),
            auto_dismiss= False)

        self.play_sound2()
        self.popup.open()


    def show_alert_dialog6(self, dt):
        if not self.dialog6:
            self.dialog6 = MDDialog(
                auto_dismiss= False,
                title="Warning",
                text= "Low autonomy! 15%",
                buttons=[
                    MDRectangleFlatButton(
                        text="Close",
                        on_release=self.close_dialog6
                    ),
                ],
            )
        self.play_sound2()
        self.dialog6.open()


    def close_dialog1(self, obj):
        Clock.schedule_once(self.delay1, 5)
        self.dialog1.dismiss()

    def close_dialog2(self, obj):
        Clock.schedule_once(self.delay1, 5)
        self.dialog2.dismiss()

    def close_dialog3(self, obj):
        Clock.schedule_once(self.delay1, 5)
        self.dialog3.dismiss()

    def close_dialog4(self, obj):
        Clock.schedule_once(self.delay1, 5)
        self.dialog4.dismiss()

    def close_dialog5(self, obj):
        Clock.schedule_once(self.delay1, 5)

    def close_dialog6(self, obj):
        Clock.schedule_once(self.delay2, 1)
        self.dialog6.dismiss()




    def delay1(self,dt):
        self.espera1= False

    def delay2(self,dt):

        if self.autonomia_perc > 10 :

            self.espera4= False


    #Velocity Warning
    def vel_warn1(self,dt):

        if self.fundo_escuro is True:

            if self.ids.mdcard_velocidade.md_bg_color == self.cor_escura:
                self.ids.mdcard_velocidade.md_bg_color = self.cor_vermelha
                self.espera3 = False
            else:
                self.ids.mdcard_velocidade.md_bg_color = self.cor_escura
                self.espera3 = False

        else:

            if self.ids.mdcard_velocidade.md_bg_color == self.cor_clara:
                self.ids.mdcard_velocidade.md_bg_color = self.cor_vermelha
                self.espera3 = False
            else:
                self.ids.mdcard_velocidade.md_bg_color = self.cor_clara
                self.espera3 = False

    def warn_warn2(self,dt):

        if self.fundo_escuro is True:

            if self.ids.mdcard_warns.md_bg_color == self.cor_escura:
                self.ids.mdcard_warns.md_bg_color = self.cor_vermelha
                self.espera1 = False
            else:
                self.ids.mdcard_warns.md_bg_color = self.cor_escura
                self.espera1 = False

        else:
            if self.ids.mdcard_warns.md_bg_color == self.cor_clara:
                self.ids.mdcard_warns.md_bg_color = self.cor_vermelha
                self.espera1 = False
            else:
                self.ids.mdcard_warns.md_bg_color = self.cor_clara
                self.espera1 = False



#------------------------------------------------------------------
# ---- Sound Notifications ----------------------------------------
#------------------------------------------------------------------



    def play_sound1(self,*args):
        sound = SoundLoader.load('audio/audio1.mp3')
        if sound:
            sound.volume = 1
            sound.play()

    def play_sound2(self):
        sound = SoundLoader.load('audio/audio2.mp3')
        if sound:
            sound.volume = 1
            sound.play()

    def play_video(self):
        player = VideoPlayer(source = "videos/intro.mp4")
        player.state = 'play'
        player.option = {'eos': 'loop'}
        player.allow_strech = True
        player.play()



#------------------------------------------------------------------
# ---- Switch -----------------------------------------------------
#------------------------------------------------------------------



    def changescreen1(self,dt):

        if self.manager.current == 'main_screen':
            self.manager.current = 'reverse_screen'
            self.manager.transition.direction = "right"

    def changescreen2(self,dt):

        if self.manager.current == 'reverse_screen':
            self.manager.current = 'main_screen'
            self.manager.transition.direction = "left"

    def changescreen3(self,dt):

        if self.manager.current == 'main_screen':
            self.manager.current = 'close_screen'
            self.manager.transition.direction = "left"

    def changescreen4(self,dt):

        if self.manager.current == 'close_screen':
            self.manager.current = 'main_screen'
            self.manager.transition.direction = "right"

#------------------------------------------------------------------
# ---- Relative Odometer --------------------------------------------------
#------------------------------------------------------------------
    def restart(self):
        self.contador_fixo = self.contador_km
        Clock.schedule_interval(self.refresh_contador, 0.5)

    def refresh_contador(self, dt):
        self.contagem= self.contador_km

        contador= (self.contagem - self.contador_fixo)
        self.ids.contador_parcial.text = str(contador)



class ContentNavigationDrawer(BoxLayout):

    #Settings tab
    global notification
    notification = True

    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


    def switch_click1(self,switchObject,switchValue1):
        global notification
        notification=switchValue1



class ReverseLayout(Screen):
    #Reverse layout initialization
    pass

class CloseLayout(Screen):
    #Close layout initialization
    pass


class WindowManager(ScreenManager):
    #Layout manager
    reverse_screen = ObjectProperty()
    main_screen = ObjectProperty()



class MyWidget(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.start,0.5)
        #Clock.schedule_interval(self.start, 0.5)

    def start(self, dt):

        self.ids.time.title = time.asctime()

class Gps(MapView):
    #GPS window initialization
    pass



class DisplayApp(MDApp):

    #Get hours
    hours=time.asctime()

    def build(self):
        #Window.borderless = True
        #Window.fullscreen = 'auto'

        #Set letter fonts
        self.font1="fonts/digital-dream/digital-7.ttf"
        self.font2="fonts/rubik/Rubik-Light.ttf"
        self.font3 = "fonts/bebas/Bebas-Regular.ttf"

        #Load kv file
        Builder.load_file('build.kv')

        #Set themes
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"


        return MyWidget()



if __name__ == '__main__':
    DisplayApp().run()


