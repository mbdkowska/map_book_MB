def get_user_info(users_data:list) -> None:
    for user in users_data:
        print(f'Twój znjaomy: {user["name"]} z miejscowości: {user["location"]} opubikował: {user["posts"]}')

def add_user(users_data:list) -> None:
    new_name: str = input('podaj imię nowego użytkownika: ')
    new_location: str = input('podaj lokalizację nowego użytkownika: ')
    new_posts: str = input('podaj liczbę postów nowego użytkownika: ')
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts},)

def remove_user(users_data:list) -> None:
    user_name = input('podaj imię do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)

