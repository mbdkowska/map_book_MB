from cProfile import label
from tkinter import *

import tkintermapview
from geocoder import location

users:list = []

def add_user():
    name=entry_imie.get()
    location=entry_miejscowosc()
    post=entry_liczba_postow.get()
    users.append({'name':name,'location':location,'posts':post})
    print(users)
    show_users()

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_imie.focus()

def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f'{idx+1}{user['name']} {user["location"]} {user["posts"]}')

def remove_user():
    listbox_lista_obiektow.index(ACTIVE)
    print(i)
    users.pop(i)
    show_users()

def edit_user():
    i=listbox_lista_obiektow.delete(ACTIVE)
    print(users[i])
    entry_imie.insert(0,users[i]['name'])
    entry_miejscowosc.insert(0,users[i]['location'])
    entry_liczba_postow.insert(0,users[i]['posts'])
    button_dodaj_obiekt.config(text='Zapisz', command=lambda: update_user(i))

def update_user(i):
    name=entry_imie.get()
    location=entry_miejscowosc.get()
    posts=entry_liczba_postow.get()
    users[i]['name']=name
    users[i]['location']=location
    users[i]['posts']=posts
    show_users()
    button_dodaj_obiekt.config(text='Dodaj', command=add_user)
    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_imie.focus()

def show_user_details()
    i=listbox_lista_obiektow.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=users[i]['name'])
    label_miejscowosc_szczegoly_obiektu_wartosc.config(text=users[i]['location'])
    label_posty_szczegoly_obiektu_wartosc.config(text=users[i]['posts'])




root = Tk()


root.title('map_book_MB')
root.geometry('1200x800')

ramka_lista_obiektów=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)


# ramka_lista_obiektow

label_lista_obiektow=Label(ramka_lista_obiektów, text='Lista użytkownikow')
label_lista_obiektow.grid(row=1, column=0, columnspan=3)

listbox_lista_obiektow=Listbox(ramka_lista_obiektów)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_poka_szczegoly=Button(ramka_szczegoly_obiektow, text = 'Pokaż szczegoly')
button_poka_szczegoly.grid(row=2, column=0)

button_usun_obiekt=Button(ramka_lista_obiektow, text = 'Usuń obiekt')
button_usun_obiekt.grid(row=3, column=2)

button_edytuj_obiekt=Button(ramka_lista_obiektow, text = 'Edytuj obiekt')
button_edytuj_obiekt.grid(row=0, column=2)

# ramka_formularz

label_formularz=Label(ramka_formularz,text='Formularz')
label_formularz.grid(row=0, column=1, columnspan=2)

label_imie=Label(ramka_formularz,text='Imie')
label_imie.grid(row=1, column=0, sticky=W)

label_miejscowosc=Label(ramka_formularz,text='Miejscowość')
label_miejscowosc.grid(row=2, column=0, sticky=W)

label_liczba_postow=Label(ramka_formularz,text='Liczba postow')
label_liczba_postow.grid(row=3, column=0, sticky=W)

entry_imie=Entry(ramka_formularz)
entry_imie.grid(row=1, column=1)
entry_miejscowosc=Entry(ramka_formularz)
entry_miejscowosc.grid(row=2, column=1)
entry_liczba_postow=Entry(ramka_formularz)
entry_liczba_postow.grid(row=3, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text = 'Dodaj')
button_dodaj_obiekt.grid(row=4, column=2)


#ramka szczegoly obiektow

label_szczegoly_obiektow=Label(ramka_formularz,text='Szczegoly')
label_szczegoly_obiektow.grid(row=0, column=0)

label_imie_szczegoly_obiektow=Label(ramka_formularz, text='Imie: ')
label_imie_szczegoly_obiektow.grid(row=1, column=0)

root.mainloop()

