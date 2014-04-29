'''
This module extends the Kivy library's Widget class with a method
that can be used to quickly draw rectangles around widgets to
see the space they are using. This is helpful for debugging
layout design errors

'''

__author__ = 'Mika Kunnas'
__version__ = '1.0.4'

from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class InvalidColorError(Exception):
    pass

def show_area(self, color='green', alpha=0.5, group=None):
    '''
    Draws a rectangle on the widget's canvas 
    to display its position and proportions.
    '''
    
    max_ = 255.0
    
    color_names = {'blue': [0, 0, 1],
                   'cyan': [0, 1, 1],
                   'fuchsia': [1, 0, 1],
                   'green': [0, 1, 0],
                   'orange': [1, 165/max_, 0],
                   'pink': [1, 192/max_, 203/max_],
                   'red': [1, 0, 0],
                   'yellow': [1, 1, 0],
                   }
    rgba = None
    
    if type(color) == str:
        
        for name in color_names:
            if name.startswith(color):
                rgba = color_names[name]
                break
        
        try:
            rgba += [alpha]
        
        except TypeError:
            raise InvalidColorError('No color match for color string "' + color + '"')
    
    elif isinstance(color, (list, tuple)):
        if len(color) == 4:
            rgba = color
        
        else:
            rgba = list(color) + [alpha]
    
    attr = self.canvas
    
    if group == 'after':
        attr = self.canvas.after
    
    elif group == 'before':
        attr = self.canvas.before
        
    with attr:
        Color(*rgba)
        self.area = Rectangle(pos=self.pos, size=self.size)
    
    self.bind(pos=self.update_area)
    self.bind(size=self.update_area)

def update_area(self, *args):
    self.area.pos = self.pos
    self.area.size = self.size

def attach():
    Widget.update_area = update_area
    Widget.show_area = show_area
