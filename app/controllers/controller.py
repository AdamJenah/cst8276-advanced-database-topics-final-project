from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from app.models.database import get_database
from app.models.game import Game
from app.views.model import ModelWindow


class GameController:
    def __init__(self,model):
            self.model = model

    # def add_game_fields(self):
    #     target = self.ids.ops_fields
    #     target.clear_widgets()
    #     crud_title = TextInput(hint_text='Title')
    #     crud_genre = TextInput(hint_text='Genre')
    #     crud_year = TextInput(hint_text='Year Released')
    #     crud_platform = TextInput(hint_text='Platform')
    #     crud_esrb = Spinner(text='ESRB Rating', values=['E', 'E10+', 'T', 'M', 'AO'])
    #
    #     submit_button = Button(text='Submit', background_color=(0, 1, 0, 1))
    #
    #     def submit_game_handler():
    #         if not all([crud_title.text, crud_genre.text, crud_year.text, crud_platform.text, crud_esrb.text]):
    #             print("All fields are mandatory. Please fill in all required fields.")
    #             return
    #
    #         self.model.submit_game(crud_title.text, crud_genre.text, crud_year.text, crud_platform.text, crud_esrb.text)
    #
    #     submit_button.bind(on_release=lambda btn: submit_game_handler())
    #
    #     crud_year.input_filter = 'int'
    #     crud_esrb.input_filter = 'int'
    #
    #     target.add_widget(crud_title)
    #     target.add_widget(crud_genre)
    #     target.add_widget(crud_year)
    #     target.add_widget(crud_platform)
    #     target.add_widget(crud_esrb)
    #     target.add_widget(submit_button)

