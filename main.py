from modules import Application
from os import system, name

if __name__ == '__main__':
    app = Application()
    while True:
        app.show_menu()
        while True:
            goto_menu = input('go back to menu [y/n] :=> ').strip()
            if goto_menu.lower() == 'n':
                print('#dirumahaja !')
                exit()
            elif goto_menu.lower() == 'y':
                system('cls' if name == 'nt' else 'clear')
                break
            else:
                print('[ERROR] wrong input please try again')