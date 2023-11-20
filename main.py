from app.models.database import create_database_if_not_exists

# Import your Kivy App class, assuming it's named MyApp and located in main_view.py
from app.views.main_view import MyApp


def main():
    create_database_if_not_exists()  # Ensure the database exists
    MyApp().run()  # Run the Kivy App


if __name__ == "__main__":
    main()
