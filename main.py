from utils.model import users
from utils.controller import get_user_info, add_user, remove_user, update_user, get_mapa


def main():
    print('===========MENU============')
    print('0 - zakończ program')
    print('1 - wyświetl co u znajomych')
    print('2 - dodaj użytkownika')
    print('3 - usuń użytkownika')
    print('4 - zaktualizuj użytkownika')
    print('5 - przygotuj mapę użytkowników')
    print('===========================')

    while True:
        choice:str=input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_mapa(users)


if __name__ == '__main__':
    main()
