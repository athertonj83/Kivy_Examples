#this creates an android app

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
import random
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import (ListProperty, NumericProperty, ObjectProperty, StringProperty)
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform

__version__='0.1' #Used later during Android compilation


class Player(Widget): #the moving paddle
    position=NumericProperty(0.5)
    direction=StringProperty('none')

    def __init__(self,**kwargs):
        super(Player,self).__init__(**kwargs)
        with self.canvas:
            Color(1,0,0,1)
            Rectangle(pos=self.pos,size=self.size)

    def on_touch_down(self,touch):
        self.direction=('right' if touch.x>self.parent.center_x else 'left')

    def on_touch_up(self,touch):
        self.direction='none'

    def on_key_down(self,keypress,scancode,*args):
        if scancode==275:
            self.direction='right'
        elif scancode==276:
            self.direction='left'
        else:
            self.direction='none'

    def on_key_up(self,*args):
        self.direction='none'

    def update(self,dt):
        dir_dict={'right':1, 'left':-1, 'none':0}
        self.position+=(0.5*dt*dir_dict[self.direction])



class Ball(Widget):
    #pos_hints are for proportional positioning
    pos_hint_x=NumericProperty(0.5)
    pos_hint_y=NumericProperty(0.3)
    proper_size=NumericProperty(0.5)
    velocity=ListProperty([0.1,0.5])

    def update(self,dt):
        self.pos_hint_x+=self.velocity[0]*dt
        self.pos_hint_y+=self.velocity[1]*dt
        if self.right>self.parent.right: #bounce from right
            self.velocity[0]=-1*abs(self.velocity[0])
        if self.x<self.parent.x: # bounce from left
            self.velocity[0]=abs(self.velocity[1])
        if self.top>self.parent.top: #bounce from top
            self.velocity[1]=-1*abs(self.velocity[1])
        if self.y<self.parent.y: #lose at bottom
            self.parent.lose()
        self.bounce_from_player(self.parent.player)

    def bounce_from_player(self,player):
        if self.collide_widget(player):
            self.velocity[1]=abs(self.velocity[1])
            self.velocity[0]+=(0.1*((self.center_x - player.center_x)/player.width))


class GameEndPopup(ModalView):
    message=StringProperty()
    game=ObjectProperty()

    class Game(Widget):
        def lose(self):
            self.stop()
            GameEndPopup(message='[color=#ff0000]You lose![/color]', game=self).open()

        def win(self):
            self.stop()
            GameEndPopup(message='[color=#00ff00]You win![/color]',game=self).open()



class Block(Widget):
    colour=ListProperty([0,1,1])

    def _init__(self,**kwargs):
        super(Block,self).__init__(**kwargs)
        self.colour=random.choice([(0.78,0.28,0),(0.28,0.63,0.28),(0.25,0.28,0.78)])





class Game(FloatLayout):
    blocks=ListProperty([])
    player=ObjectProperty([])
    ball=ObjectProperty([])

    def setup_blocks(self):
        for y_jump in range(5):
            for x_jump in range(10):
                block=Block(pos_hint={'x':0.05+0.09*x_jump,'y':0.05+0.09*y_jump})
                self.add_widget(block)

    # def update(self,dt):
    #     self.ball.update(dt)
    #     self.player.update(dt)
    #
    # def start(self,*args):
    #     Clock.schedule_interval(self.update,1./60.)
    #
    # def stop(self):
    #     Clock.unschedule(self.update)
    #
    # def reset(self):
    #     for block in self.blocks:
    #         self.remove_widget(block)
    #     self.blocks=[]
    #     self.setup_blocks=[]
    #     self.ball.velocity=[random.random(),0.5]
    #     self.player.position=0.5



class BreakoutApp(App):
    def build(self):
        g=Game()
        g.setup_blocks
        # if platform!='android':
        #     Window.bind(on_key_down=g.player.on_key_down)
        #     Window.bind(on_key_up=g.player.on_key_up)
        # g.reset()
        # Clock.schedule_once(g.start,0)
        return g

BreakoutApp().run()
