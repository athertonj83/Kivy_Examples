from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import (ListProperty,NumericProperty)
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout

	
class TicTacToeGrid(GridLayout):
	def __init__(self,*args,**kwargs):
		super(TicTacToeGrid,self).__init__(*args,**kwargs)
		for row in range(3):
			for column in range(3):
				#grid_entry=GridEntry(coords=(row,column))
				grid_entry=GridEntry(size_hint_x=None,width=100)
				grid_entry.bind(on_press=self.button_pressed)
				self.add_widget(grid_entry)
	status=ListProperty([0,0,0,
		 	     0,0,0,
			     0,0,0])
	current_player=NumericProperty(1)


	def button_pressed(self,button):
		player={1:'O', -1: 'X'}
		colours={1: (1,0,0,1), -1: (0,1,0,1)} #rgba
		
		row,column=button.coords

		status_index=3*row + column
		already_played=self.status[status_index]
		
		# if nobody has aleady played here, make a new move
		if not already_played:
			self.status[status_index]=self.current_player
			button.text={1: 'O', -1: 'X'}[self.current_player]
			button.background_color=colours[self.current_player]
			self.current_player*= -1 # switch current player



	def reset(self,*args):
		self.status=[0 for _ in range(9)]
		
		#self.children is a list containing all child widgets
		for child in self.children:
			child.text=''
			child.background_color=(1,1,1,1)
		self.current_player=1




	def on_status(self, instance,status):
		status=self.status

		#sum each row, column and diagonal
		sums=[sum(status[0:3]),sum(status[3:6]),sum(status[6:9]), #rows
		      sum(status[0::3]),sum(status[1::3]),sum(status[2::3]), #cols
		      sum(status[0::4]),sum(status[2:-2:2])] # diagonals
		
		winner=None

		if 3 in sums:
			print(self.status)
			winner='Player 1 (O) wins!\n Would you like to play again?'
		elif -3 in sums:
			print(self.status)
			winner='Player 2 (X) wins!\n Would you like to play again?'
		elif 0 not in self.status: #grid full
			print(self.status)
			winner='Draw! \n Would you like to play again?'

		if winner:
			

			# create a button
			float=FloatLayout(size_hint=(0.5,0.5))
			y_button=Button(text="Y",font_size=20,pos_hint={'x':0.4, 'center_y': 0.5},size_hint=(None,None))
			n_button=Button(text="N",font_size=20,pos_hint={'x':0.6, 'center_y': 0.5},size_hint=(None,None))
			float.add_widget(y_button)
			float.add_widget(n_button)

			popup=ModalView(size_hint=(0.5,0.5))
			victory_label=Label(text=winner,pos_hint={'x': 0.3, 'center_y':0.7},size_hint=(None,None))
			float.add_widget(victory_label)

			popup.add_widget(float)			
			
			popup.bind(on_dismiss=self.reset)
			popup.open()
		
			
class GridEntry(Button):
	coords=ListProperty([0,0])


class TicTacToeApp(App):
	def build(self):
		return TicTacToeGrid()

if __name__=='__main__':
	TicTacToeApp().run()



