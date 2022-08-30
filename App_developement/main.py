from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from cgitb import text
import email
from select import select
from tkinter import Grid, font
from kivy.app import App
from kivy.uix.label import Label #class Label import from the label module
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import time
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Line
# from kivy.graphics import Color
import kivy
from kivy.uix.label import Label
from database import DataBase
from kivy.core.window import Window
import time

from cgitb import text
import email
from select import select
from tkinter import Grid, font
from kivy.app import App
from kivy.uix.label import Label #class Label import from the label module
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.popup import Popupimport
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


import time
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Line
# from kivy.graphics import Color
import os
import kivy


os.environ["KIVY_AUDIO"] = "ffpyplayer"

# tic toc functions --------------------------


def TicTocGenerator():
    # Generator that returns time differences
    ti = 0  # initial time
    tf = time.time()  # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf - ti  # returns the time difference


TicToc = TicTocGenerator()  # create an instance of the TicTocGen generator


# This will be the main function through which we define both tic() and toc()
def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print("Elapsed time: %f seconds.\n" % tempTimeInterval)


def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)
# --------------------------------

tic()
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(20,30,400,500,60,500))
            Color(1,0,0,0.5, mode="rgba")
            self.rect = Rectangle(pos=(0,0), size=(50,50))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos


class Parameter(Screen) : #class name my grid inherits from widget
    name = ObjectProperty(None) #none,  actual object poperty until it sees the kv file
    email = ObjectProperty(None)


    checks = [] # open list to be appended
    def checkbox_click(self, instance, value, option): # instance is address in memory, value would pass true or false, unclick you pass false

        if value == True:
            Parameter.checks.append(option)
            outputs = ''
            for x in Parameter.checks:
                outputs= f'{outputs} {x}'
            self.ids.SLM.text = f'Selected: {outputs}'
            pass
        else:
            outputs = ''
            Parameter.checks.remove(option)
            self.ids.SLM.text = f'Selected: {outputs}'
            pass


    material_checks = []
    def material_checkbox_click(self, instance, value, option_2): # instance is address in memory, value would pass true or false, unclick you pass false

        if value == True:
            Parameter.checks.append(option_2)
            outputs = ''
            for x in Parameter.checks:
                outputs= f'{outputs} {x}'
            self.ids.material.text = f'Selected: {outputs}'
            pass
        else:
            outputs = ''
            Parameter.checks.remove(option_2)
            self.ids.material.text = f'Selected: {outputs}'
            pass

    def btn(self):
        print("Diameter: ", self.diameter.text, "Angle: ", self.angle.text, "Printer:", self.printer.text, "Material:", self.material.text) # self since we are referencing variables from the class
        self.diameter.text ="" # blank
        self.angle.text = ""
        # self.printer.text = ""
        # self.material.text = ""


class EmptyWindow(Screen):
    pass

class Login2Window(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        # self.sound = SoundLoader.load("lock.mp3")
        sm.current = "login"


    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        markup = True
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


class SecondWindow(Screen):
    music = SoundLoader.load('lock.mp3')

    def play_music(self):
        music = SoundLoader.load('music.mp3')

        # check the exisitence of the music
        if music:
            music.play()

        return Label(text="Music is playing")

    # path = "lock.mp3"  # It can be a local file or a web address http://XXX/apple.wav , or mp3
    # b = SoundLoader.load(filename=path)  # load file
    # b.play()  # Play sound

    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")
# Builder.load_file('i')

sm = WindowManager()
db = DataBase("users.txt")

# screens = [Parameter(name="parameter")]
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"), Login2Window(name="login2"), SecondWindow(name="second"), Parameter(name="parameter"), EmptyWindow(name="empty")]

# login2 delete there is no need for it
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"

toc()

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
