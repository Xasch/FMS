from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector

Window.size = (1000,700)
 
#Variabelen#

# KTW #

benKTW = "KTW"
pwKTW = "1234"
# RTW #
benRTW = "RTW"
pwRTW = "1234"


Builder.load_string("""
<Login>:
    ben: benName.text
    pw: passwort.text
    knopf: btn
                 
 
    GridLayout:
        cols: 1
        size: root.width,root.height
        GridLayout:
            cols: 2
            Label:
                id: lb1
                text: "Benutzername"
                font_size: 30
            TextInput:
                id: benName
                multiline: False
                font_size: 30
            Label:
                text: "Passwort"
                font_size: 30
            TextInput:
                password: True
                id: passwort
                multiline: False
                font_size: 30
        Button:
            size_hint: (1.,0.5)
            text:"anmelden"
            id: btn
            font_size: 30
            on_release: 
                root.loginPopup()
                
                root.manager.transition.direction = "left"
 
<FMSKTW>
    btn1: button_1
    GridLayout:
        cols: 1
        Label:
            id: LabelFMS
            text: "RotKreuz Meschede 1-KTW-1"
            font_size: 30
        GridLayout:
            cols: 3
            Button:
                id: button_1
                text: "1"
                font_size:30
                on_press:
                    root.sqlbutton1()
                    self.background_color = (0.0, 1.0, 0.0, 1.0)#grün
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_2
                text: "2"
                font_size:30
                on_press:
                    root.sqlbutton2() 
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_3
                text: "3"
                font_size:30
                on_press:
                    root.sqlbutton3()  
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_4                   
                text: "4"
                font_size:30
                on_press: 
                    root.sqlbutton4()  
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_5
                text: "5"
                font_size:30
                on_press: 
                    root.sqlbutton5()  
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_6
                text: "6"
                font_size:30
                on_press: 
                    root.sqlbutton6()  
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_7
                text: "7"
                font_size:30
                on_press: 
                    root.sqlbutton7()  
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_8
                text: "8"
                font_size:30
                on_press: 
                    root.sqlbutton8()  
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
            Button:
                id: button_9
                text: "9"
                font_size:30
                on_press:
                    root.sqlbutton9()   
                    self.background_color = (0.0, 1.0, 0.0, 1.0)
                    button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                    button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
        Button:
            text: "zurück"
            font_size: 30
            on_release:
                root.manager.current = "login"
                root.manager.transition.direction = "right"
            on_press: 
                button_1.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_2.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_3.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_4.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_5.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_6.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_7.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_8.background_color = (1.0, 1.0, 1.0, 1.0)#grau
                button_9.background_color = (1.0, 1.0, 1.0, 1.0)#grau
 
 
""")



class Login(Screen):
    
    ben = StringProperty()
    pw = StringProperty()
    knopf = ObjectProperty()


    def loginPopup(self):
        if self.ben =="" or self.pw == "":
            popup = Popup(title="Fehler",
                          content = Label(text="Felder nicht ausgefüllt"),
                          size_hint=(None,None),size=(400,400))
            popup.open()
        else:
            if self.ben == benKTW and self.pw == pwKTW or self.ben == benRTW and self.pw == pwRTW:
                self.knopf.background_color = [0.,1.,0.,1.]
                self.manager.current = 'FMSKTW'
                global lala
                lala = self.ben
                print(lala)

            elif self.ben == benRTW and self.pw == pwRTW:
                self.knopf.background_color = [0.,1.,0.,1.]
                self.manager.current = 'FMSKTW'
                lala = self.ben
                print(lala)

            else:
                self.knopf.background_color = [1.,0.,0.,1.]



class FMSKTW(Screen):
    global my_db
    global cursor
    my_db = mysql.connector.connect(
            host="31.47.241.40",
            user="web247_python",
            password="cny*zG*P^PJ8DlhK",
            database="web247_python"
        )
    cursor = my_db.cursor()

    def sqlbutton1(self):

        cursor.execute("UPDATE Status SET State= 1 WHERE ID=1")
        my_db.commit()
            
            #cursor.execute ("select * from Status")
            #for i in cursor.fetchall():
                #print(i[0], i[1], i[2])
        #self.ids.LabelFMS.text = lala
    def sqlbutton2(self):
    
            cursor.execute("UPDATE Status SET State= 2 WHERE ID=1")
            my_db.commit()  

    def sqlbutton3(self):
            
            cursor.execute("UPDATE Status SET State= 3 WHERE ID=1")
            my_db.commit()    

    def sqlbutton4(self):
    
            cursor.execute("UPDATE Status SET State= 4 WHERE ID=1")
            my_db.commit()  

    def sqlbutton5(self):
            
            cursor.execute("UPDATE Status SET State= 5 WHERE ID=1")
            my_db.commit()  
    def sqlbutton6(self):
    
            cursor.execute("UPDATE Status SET State= 6 WHERE ID=1")
            my_db.commit()  

    def sqlbutton7(self):
            
            cursor.execute("UPDATE Status SET State= 7 WHERE ID=1")
            my_db.commit()    

    def sqlbutton8(self):
    
            cursor.execute("UPDATE Status SET State= 8 WHERE ID=1")
            my_db.commit()  

    def sqlbutton9(self):
            
            cursor.execute("UPDATE Status SET State= 9 WHERE ID=1")
            my_db.commit() 
             
ms = ScreenManager()
ms.add_widget(Login(name='login'))
ms.add_widget(FMSKTW(name="FMSKTW"))

class StartApp(App):
    def build(self):
        
        return ms
    
if __name__ == "__main__":
    StartApp().run()
