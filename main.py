from app.models.database import create_database_if_not_exists
from app.views.game_view_controller import main as run_console_application


def main():
    create_database_if_not_exists()  # Ensure the database exists
    run_console_application()


if __name__ == "__main__":
    main()
