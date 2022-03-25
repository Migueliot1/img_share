from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def search_img(self):
        self.manager.current_screen.ids.showed_img.source = 'files/tomb.png'


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()