from kivy.app import App
from kivy.uix.label import Label

class NervaApp(App):
    def build(self):
        return Label(text='Nerva App Running!')

if __name__ == '__main__':
    NervaApp().run()
