import kivy

#print(kivy.__version__)

kivy.require('1.9.2') # this is my current version of kivy

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello World')

if __name__=="__main__":
    MyApp().run()
