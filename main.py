from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def search_img(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text

        # Download the wikipedia image
        self.download_img(query)

        # Pass retrieved image to the app
        self.manager.current_screen.ids.showed_img.source = 'files/image.jpg'

    def download_img(self, name):
        pass

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()