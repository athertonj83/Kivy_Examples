#this creates an android app

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
import random
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import (ListProperty, NumericProperty, ObjectProperty, StringProperty)



__version__='0.1' #Used later during Android compilation

# class BreakoutApp(App):
#         pass


class Game(FloatLayout): #will contain everything
        blocks=ListProperty([])
        player=ObjectProperty([])
        ball=ObjectProperty([])

class Player(Widget): #the moving paddle
    position=NumericProperty(0.5)
    direction=StringProperty('none')

class Ball(Widget):
    #pos_hints are for proportional positioning
    pos_hint_x=NumericProperty(0.5)
    pos_hint_y=NumericProperty(0.3)
    proper_size=NumericProperty(0.5)
    velocity=ListProperty([0.1,0.5])

class Block(Widget):
    colour=ListProperty([0,1,1])

# class BlockA(Block):
#     def __init__(self,**kwargs):
#         self.colour=random.choice([(0.78,0.28,0),(0.28,0.63,0.28),(0.25,0.28,0.78)])



# class Block(Widget):
#     def _init__(self,**kwargs):
#         super(Block,self).__init__(**kwargs)
#         self.colour=random.choice([(0.78,0.28,0),(0.28,0.63,0.28),(0.25,0.28,0.78)])





class Player(Widget):
    def __init__(self,**kwargs):
        super(Player,self).__init__(**kwargs)
        with self.canvas:
            Color(1,0,0,1)
            Rectangle(pos=self.pos,size=self.size)


class Game(FloatLayout):
    def setup_blocks(self):
        for y_jump in range(5):
            for x_jump in range(10):
                block=Block(pos_hint={'x':0.05+0.09*x_jump,'y':0.05+0.09*y_jump})
                self.add_widget(block)

class BreakoutApp(App):
    def build(self):
        g=Game()
        g.setup_blocks()
        return g

BreakoutApp().run()
