from s02p1.MENU import read_cmd, welcome_print, menu
from s02p1.UI import f_run

def app_start():
    welcome_print()
    w = read_cmd()
    menu_choice(w)

def menu_choice(w):
    if w == '1':
        f_run()
    if w == '2':
        menu()

app_start()