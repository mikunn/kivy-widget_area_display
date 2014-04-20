from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import wadisp

Builder.load_string('''

<MyBoxLayout>:
    orientation: 'vertical'
    
    GreenLabel:
        text: 'GreenLabel'
        canvas: self.show_area()
        
    BlueLabel:
        text: 'BlueLabel'
        canvas: self.show_area(color='b')
    
    GridLayout:
        rows: 1
        canvas: self.show_area(color='orange', alpha=1, group='before')
        
        CustomColorLabel:
            size_hint: None, None
            size: 200, 40
            text: 'CustomColorLabel'
            canvas: self.show_area(color=(.2, .7, .8, 1))
        
        CustomColorButton:
            size_hint: None, None
            size: 200, 40
            text: 'CustomColorButton'
        
        AnotherCustomColorButton:
            size_hint: None, None
            size: 200, 40
            text: 'AnotherCustomColorButton'
            
<GreenLabel@Label>:
<BlueLabel@Label>:
<CustomColorLabel@Label>:

''')

class WidgetAreaTestApp(App):
    def build(self):
        return MyBoxLayout()

class MyBoxLayout(BoxLayout):
    pass

class CustomColorButton(Button):
    def __init__(self, **kwargs):
        super(CustomColorButton, self).__init__()
        self.show_area(color=(0,1,1), alpha=0.8)
        
class AnotherCustomColorButton(Button):
    def __init__(self, **kwargs):
        super(AnotherCustomColorButton, self).__init__()
        self.show_area(color=(0.7, 0.7, 0.3), alpha=0.8, group='after')
    
if __name__ == '__main__':
    wadisp.attach()
    WidgetAreaTestApp().run()
    