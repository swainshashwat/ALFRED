from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Container(GridLayout):
    pass

class MainApp(App):
    def build(self):
        self.title = "DOMINO"
        return Container()

if __name__=="__main__":
    app = MainApp()
    app.run()