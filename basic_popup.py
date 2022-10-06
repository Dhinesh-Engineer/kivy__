from kivy.app import App # module to build a application

from kivy.uix.label import Label # module used to create the widgets
from kivy.uix.button import Button # module used for  creating buttons

from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

class grid_layout(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.rows=3
        self.cols=1

        self.l1 = Label(text="Enter your Name",font_size=14)
        self.add_widget(self.l1)

        self.txt = TextInput(text="",font_size=14)
        self.add_widget(self.txt)
        
        self.button =Button(text='Submit', font_size=14)
        self.button.bind(on_press = self.call_back)
        self.add_widget(self.button)

        self.pop =  Popup(title="Message",size=(200,200),content=Label(text=""))

    def call_back(self,ele):
        self.pop.content.text = self.txt.text
        self.pop.open()



 
class demo1App(App):   #create a class for the app
    def build(self): #it just build the app 
        return grid_layout()

    #   pass         # without above return statement use pass statement to create the app

demo1App().run()   # run the application with the objecct





