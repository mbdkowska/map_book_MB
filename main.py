

users:list = [
    {'name': 'Maciek', 'location': 'Toruń','posts': '3'},
    {'name': 'Patrycja', 'location': 'Kutno','posts': '100'},
    {'name': 'Dobi', 'location': 'Iława','posts': '700'},
    {'name': 'Maja', 'location': 'Inowrocław','posts': '30'},
]
def get_users_info(users_data:list)->None
    for user in users_data:
    print(f'Twój znjaomy: {user["name"]} z miejscowości: {user["posts"]} opubikował: {user["posts"]}')
    get_users_info(users)
