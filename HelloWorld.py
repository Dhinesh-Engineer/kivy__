from kivy.app import App # module to build a application
from kivy.uix.label import Label # module used to create the widgets

class demoApp(App):   #create a class for the app
    def build(self): #it just build the app 
        return Label(text = "Hello World ")   # with this statement u can put the string inside the window screen
    #   pass         # without above return statement use pass statement to create the app


demo=demoApp()    #object for the class
demo.run()   # run the application with the objecct
