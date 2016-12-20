import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.lang import ParserException

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.storage.jsonstore import JsonStore

class PlaygroundScreen(Screen):
    content_pane = ObjectProperty(None)
    editor_pane = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(PlaygroundScreen,self).__init__(**kwargs)
        self.creation = Builder.load_string(self.editor_pane.text)
        self.content_pane.add_widget(self.creation)
    
    def on_text(self,val):

        try:
            creation = Builder.load_string(val)
        except SyntaxError as se:
            print("Not valid syntax.")
            return
        except ParserException as pe:
            print("Parser error: {0}".format(pe))
            return
        except Exception as e:
            print(type(e))
            print(e)
            return

        try:
            self.content_pane.clear_widgets()
            self.content_pane.add_widget(creation)
        except Exception as e:
            print(e)
        

class PGScreenManager(ScreenManager):
    pass

class PlaygroundApp(App):

    def build(self):
        self.sm = PGScreenManager()
        self.pgs = PlaygroundScreen(name='pgs')
        self.sm.add_widget(self.pgs)
        self.sm.current='pgs'
        return self.sm


if __name__ == '__main__':
    PlaygroundApp().run()
