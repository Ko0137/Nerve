from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='НЕРВ'))
