import kivy

print(kivy.__version__)

kivy.require('1.9.1') # this is my current version of kivy

from kivy.app import App
from kivy.uix.label import Label

class JenApp(App):
    def build(self):
        return Label(text='Hello World')

if __name__=="__main__":
    JenApp().run()
