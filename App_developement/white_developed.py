from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
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
from kivy.config import Config
import os
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Window.size = (300, 100)

class MainApp(MDApp):
    def build(self):
        self.title='Dashboard'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"


MainApp().run()
