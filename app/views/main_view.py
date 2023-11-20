from kivy.app import App
from kivy.properties import BooleanProperty, ColorProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from app.controllers.controller import GameController



class GameListItem(RecycleDataViewBehavior, Label):
    """ Basic list item for games. """
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    bg_color_normal = ColorProperty([0, 0, 0, 0])  # Default color
    bg_color_selected = ColorProperty([0.9, 0.9, 0.9, 1])  # Color when selected

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.text = data['text']
        return super(GameListItem, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        """ Add selection on touch down """
        if super(GameListItem, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        """ Respond to the selection of items in the view. """
        self.selected = is_selected
        self.background_color = self.bg_color_selected if is_selected else self.bg_color_normal


class GameListView(RecycleView):
    def __init__(self, **kwargs):
        super(GameListView, self).__init__(**kwargs)
        self.data = [{'text': 'Sample Game 1'}, {'text': 'Sample Game 2'}]

# Screen for adding games
class AddGameScreen(Screen):
    def __init__(self, **kwargs):
        super(AddGameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Create and add your widgets for game details to layout
        self.title_input = TextInput(hint_text='Title')
        self.genre_input = TextInput(hint_text='Genre (comma-separated)')
        self.year_released_input = TextInput(hint_text='Year Released')
        self.platform_input = TextInput(hint_text='Platform (comma-separated)')
        self.ESRB_rating_input = TextInput(hint_text='ESRB Rating')
        self.admin_id_input = TextInput(hint_text='Admin ID')
        self.admin_username_input = TextInput(hint_text='Admin Username')
        self.admin_password_input = TextInput(hint_text='Admin Password')

        # Add the input fields to the layout
        layout.add_widget(self.title_input)
        layout.add_widget(self.genre_input)
        layout.add_widget(self.year_released_input)
        layout.add_widget(self.platform_input)
        layout.add_widget(self.ESRB_rating_input)
        layout.add_widget(self.admin_id_input)
        layout.add_widget(self.admin_username_input)
        layout.add_widget(self.admin_password_input)

        # Add Game button
        add_game_btn = Button(text='Add Game')
        add_game_btn.bind(on_press=self.on_add_game)
        layout.add_widget(add_game_btn)

        # View Game List button
        view_game_list_btn = Button(text='View Game List')
        view_game_list_btn.bind(on_press=self.on_view_game_list)
        layout.add_widget(view_game_list_btn)

        self.add_widget(layout)

    def on_add_game(self, instance):
        # Access the controller from the running app
        app = App.get_running_app()
        controller = app.controller
        # Extract information from the input fields
        title = self.title_input.text.strip()
        genre = self.genre_input.text.strip().split(',')
        year_released_text = self.year_released_input.text.strip()
        platform = self.platform_input.text.strip().split(',')
        ESRB_rating = self.ESRB_rating_input.text.strip()
        admin_id_text = self.admin_id_input.text.strip()
        admin_username = self.admin_username_input.text.strip()
        admin_password = self.admin_password_input.text.strip()

        # Validate fields
        if not title or not genre or not year_released_text or not platform or not ESRB_rating or not admin_id_text or not admin_username or not admin_password:
            popup = Popup(title='Error', content=Label(text='All fields are required!'), size_hint=(None, None),
                          size=(400, 400))
            popup.open()
            return

        try:
            year_released = int(year_released_text)
            admin_id = int(admin_id_text)
        except ValueError:
            popup = Popup(title='Error', content=Label(text='Year released and Admin ID must be integers!'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            return

        admin = {"admin_id": admin_id, "username": admin_username, "password": admin_password}

        # Call the controller's method to add the game
        controller.add_game(title, genre, year_released, platform, ESRB_rating, admin)  # Use 'controller' here

        # Clear the input fields after adding the game
        self.title_input.text = ''
        self.genre_input.text = ''
        self.year_released_input.text = ''
        self.platform_input.text = ''
        self.ESRB_rating_input.text = ''
        self.admin_id_input.text = ''
        self.admin_username_input.text = ''
        self.admin_password_input.text = ''

        # Display success message
        popup = Popup(title='Success', content=Label(text='Game added successfully!'), size_hint=(None, None),
                      size=(400, 400))
        popup.open()

        self.manager.current = 'game_list'

    def on_view_game_list(self, instance):
        # Change to the game list screen
        self.manager.current = 'game_list'

# Screen for viewing the list of games
class GameListScreen(Screen):
    def __init__(self, **kwargs):
        super(GameListScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Add labels for each game (you can replace this with your game data)
        game_names = ["Sample Game 1", "Sample Game 2", "Sample Game 3"]
        for game_name in game_names:
            label = Label(text=game_name)
            layout.add_widget(label)

        self.add_widget(layout)

# ScreenManager to manage the two screens
class MainView(ScreenManager):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.add_widget(AddGameScreen(name='add_game'))
        self.add_widget(GameListScreen(name='game_list'))


    def on_view_games(self, instance):
        try:
            # Fetch games from the database through the controller
            games = self.controller.get_all_games()
            # Convert each game document to a dictionary that the RecycleView can understand
            # Here, we're just using the title to display
            self.games_list_view.data = [{'text': game['title'], 'size_hint_y': None, 'height': 44} for game in games]
        except Exception as e:
            print(f"An error occurred: {e}")


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.controller = GameController()  # Initialize the controller within __init__

    def build(self):
        return MainView()



if __name__ == '__main__':
    MyApp().run()
