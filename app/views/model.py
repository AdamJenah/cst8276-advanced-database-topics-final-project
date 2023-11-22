from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from collections import OrderedDict
from app.views.utils.datatable import DataTable
from app.models.database import Database


class ModelWindow(BoxLayout, Database):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.database = Database
        content = self.ids.scrn_contents
        games = self.get_games()
        game_table = DataTable(table=games)
        content.add_widget(game_table)

        product_scrn = self.ids.scrn_product_content
        products = self.get_games()
        prod_table = DataTable(table=products)
        product_scrn.add_widget(prod_table)

    def add_game_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_title = TextInput(hint_text='Title')
        crud_genre = TextInput(hint_text='Genre')
        crud_year = TextInput(hint_text='Year Released')
        crud_platform = TextInput(hint_text='Platform')
        crud_esrb = Spinner(text='ESRB Rating', values=['E', 'E10+', 'T', 'M', 'AO'])

        submit_button = Button(text='Submit', background_color=(0, 1, 0, 1))

        def submit_game_handler():
            if not all([crud_title.text, crud_genre.text, crud_year.text, crud_platform.text, crud_esrb.text]):
                print("All fields are mandatory. Please fill in all required fields.")
                return

            self.submit_game(crud_title.text, crud_genre.text, crud_year.text, crud_platform.text, crud_esrb.text)

        submit_button.bind(on_release=lambda btn: submit_game_handler())

        crud_year.input_filter = 'int'
        crud_esrb.input_filter = 'int'

        target.add_widget(crud_title)
        target.add_widget(crud_genre)
        target.add_widget(crud_year)
        target.add_widget(crud_platform)
        target.add_widget(crud_esrb)
        target.add_widget(submit_button)

    def update_game_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_title = TextInput(hint_text='Title')
        crud_genre = TextInput(hint_text='Genre')
        crud_year = TextInput(hint_text='Year Released')
        crud_platform = TextInput(hint_text='Platform')
        crud_esrb = Spinner(text='ESRB Rating', values=['E', 'E10+', 'T', 'M', 'AO'])

        submit_button = Button(text='Update', background_color=(0, 1, 0, 1))

        def perform_update():
            if not all([crud_title.text, crud_genre.text, crud_year.text, crud_platform.text, crud_esrb.text]):
                print("All fields are mandatory. Please fill in all the required fields.")
                return

            self.update_game(crud_title.text, crud_genre.text, crud_year.text, crud_platform.text, crud_esrb.text)

        submit_button.bind(on_release=lambda btn: perform_update())

        crud_year.input_filter = 'int'
        crud_esrb.input_filter = 'int'

        target.add_widget(crud_title)
        target.add_widget(crud_genre)
        target.add_widget(crud_year)
        target.add_widget(crud_platform)
        target.add_widget(crud_esrb)
        target.add_widget(submit_button)

    def update_game(self, title, genre, year, plat, esrb):
        content = self.ids.scrn_contents
        content.clear_widgets()
        self.database.get_database(self).games.update_one({'title': title}, {
            '$set': {'title': title, 'genre': genre, 'year_released': year, 'platform': plat, 'ESRB_rating': esrb}})

        games = self.get_games()
        gamestable = DataTable(table=games)
        content.add_widget(gamestable)

    def remove_game_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        crud_game = TextInput(hint_text='Game title')
        crud_submit = Button(text='Remove', size_hint_x=None, width=100, background_color=(0, 1, 0, 1),
                             on_release=lambda x: self.remove_game(crud_game.text))

        target.add_widget(crud_game)
        target.add_widget(crud_submit)

    def remove_game(self, title):
        content = self.ids.scrn_contents
        content.clear_widgets()

        Database.get_database(self).games.delete_one({'title': title})

        games = self.get_games()
        gamestable = DataTable(table=games)
        content.add_widget(gamestable)

    def submit_game(self, title, genre, year, platform, esrb):

        # Create a dictionary for the new game
        new_game = {
            'title': title,
            'genre': genre,
            'year_released': year,
            'platform': platform,
            'ESRB_rating': esrb
        }

        Database.get_database(self).games.insert_one(new_game)

        self.refresh_displayed_data()

    def refresh_displayed_data(self):
        content = self.ids.scrn_contents
        content.clear_widgets()

        games = self.get_games()

        game_table = DataTable(table=games)
        content.add_widget(game_table)

    def get_games(self):
        _games = OrderedDict()
        _games['titles'] = {}
        _games['genres'] = {}
        _games['years_released'] = {}
        _games['platforms'] = {}
        _games['esrb_ratings'] = {}

        titles = []
        genres = []
        years_released = []
        platforms = []
        esrb_ratings = []

        for game in self.database.get_database(self).games.find():
            titles.append(game['title'])
            genres.append(game['genre'])
            years_released.append(game['year_released'])
            platforms.append(game['platform'])
            esrb_ratings.append(game['ESRB_rating'])

        games_length = len(titles)
        idx = 0
        while idx < games_length:
            _games['titles'][idx] = titles[idx]
            _games['genres'][idx] = genres[idx]
            _games['years_released'][idx] = years_released[idx]
            _games['platforms'][idx] = platforms[idx]
            _games['esrb_ratings'][idx] = esrb_ratings[idx]

            idx += 1

        return _games


class ModelApp(App):
    def build(self):
        return ModelWindow()





if __name__ == '__main__':

    database = Database()
    database.create_database_if_not_exists()
    ModelApp().run()
