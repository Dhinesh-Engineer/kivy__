from kivy.app import App # module to build a application

from kivy.uix.label import Label # module used to create the widgets
from kivy.uix.button import Button # module used for  creating buttons

from kivy.uix.anchorlayout import AnchorLayout  # modules used for layout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout


class anchor_layout(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anchor_x ='right'   # we can change the buttonn position by anchor_x and anchor_y
        self.anchor_y = 'bottom'

        self.button =Button(text='Hello world', size_hint=(.1,.1),font_size=14)
        self.add_widget(self.button)



class grid_layout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows=2
        self.cols=1

        self.l1 = Label(text="click me")
        self.add_widget(self.l1)

        self.button =Button(text='Hello world', font_size=14)
        self.add_widget(self.button)

class float_layout(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.button =Button(text='Hello world', size_hint=(.1,.1),font_size=14)
        self.add_widget(self.button)
        
        self.button1 =Button(text='Hello world', size_hint=(.1,.1),font_size=14,pos_hint={"x":.6,"y":.5})
        self.add_widget(self.button1)

class page_layout(PageLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        self.button1 =Button(text='page 1', font_size=14)
        self.add_widget(self.button1)
        self.button2 =Button(text='page 2', font_size=14)
        self.add_widget(self.button2)
        self.button3 =Button(text='page 3', font_size=14)
        self.add_widget(self.button3)
        




 
class demo1App(App):   #create a class for the app
    def build(self): #it just build the app 
        # return anchor_layout()
        # return grid_layout()
        # return float_layout()
        return page_layout()


    #   pass         # without above return statement use pass statement to create the app

demo1App().run()   # run the application with the objecct





