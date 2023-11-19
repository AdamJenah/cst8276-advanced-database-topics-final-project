from app.controllers.controller import GameController


def display_menu():
    print("\nVideo Game Catalog")
    print("1. Add New Game")
    print("2. View All Games")
    print("3. Search Game by Title")
    print("4. Update Game")
    print("5. Delete Game")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice


def add_game(controller):
    print("\nAdd New Game")
    title = input("Enter title: ")
    genre = input("Enter genre (comma-separated): ").split(',')
    year_released = int(input("Enter year released: "))
    platform = input("Enter platform (comma-separated): ").split(',')
    ESRB_rating = input("Enter ESRB rating: ")

    while True:
        try:
            admin_id = int(input("Enter admin ID: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric admin ID.")

    admin = {
        "admin_id": admin_id,
        "username": input("Enter admin username: "),
        "password": input("Enter admin password: ")
    }

    controller.add_game(title, genre, year_released, platform, ESRB_rating, admin)
    print("Game added successfully.")


def view_all_games(controller):
    print("\nAll Games:")
    games = controller.get_all_games()
    for game in games:
        print(game)


def search_game(controller):
    title = input("Enter the title of the game to search: ")
    game = controller.get_game_by_title(title)
    if game:
        print(game)
    else:
        print("Game not found.")


def update_game(controller):
    title = input("Enter the title of the game to update: ")
    update_data = {}
    update_field = input("Enter the field to update (genre/year_released/platform/ESRB_rating): ")
    update_value = input("Enter the new value: ")
    update_data[update_field] = update_value
    controller.update_game(title, update_data)
    print("Game updated successfully.")


def delete_game(controller):
    title = input("Enter the title of the game to delete: ")
    controller.delete_game(title)
    print("Game deleted successfully.")


def main():
    controller = GameController()
    while True:
        choice = display_menu()
        if choice == '1':
            add_game(controller)
        elif choice == '2':
            view_all_games(controller)
        elif choice == '3':
            search_game(controller)
        elif choice == '4':
            update_game(controller)
        elif choice == '5':
            delete_game(controller)
        elif choice == '6':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
