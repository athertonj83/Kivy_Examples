from kivy.app import App
from kivy.uix.label import Label

# Some pre-tic tac toe testing
class TicTacToeApp(App):
    def build(self):
	return Label(text="Hello World!", font_size=50, color=(1,0,0,1)) #r,g,b,a	

if __name__=="__main__":
    TicTacToeApp().run()




