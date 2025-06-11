def get_user_info(users_data:list) -> None:
    for user in users_data:
        print(f'Twój znjaomy: {user["name"]} z miejscowości: {user["location"]} opubikował: {user["posts"]}')