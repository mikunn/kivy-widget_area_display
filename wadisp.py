from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color

class InvalidColor(Exception):
    pass

def display_widget_area(self, color='green', alpha=0.5, group=None):
    '''
    Draws a rectangle on the widget's canvas 
    to display its position and proportions.
    '''
    
    max_ = 255.0
    
    color_names = {'blue': [0, 0, 1],
                   'cyan': [0, 1, 1],
                   'green': [0, 1, 0],
                   'fuchsia': [1, 0, 1],
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
        
        try:
            rgba += [alpha]
        
        except TypeError:
            raise InvalidColor('No color match for color string "' + color + '"')
    
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
    
    self.bind(pos=self.update_rect)
    self.bind(size=self.update_rect)

def update_area(self, *args):
    self.area.pos = self.pos
    self.area.size = self.size

def attach():
    Widget.update_rect = update_area
    Widget.display_widget_area = display_widget_area