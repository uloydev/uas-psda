from .tree import Tree
from .fetch import Fetch
from os import system, name

class Core:
    def __init__(self):
        self.tree = Tree('Indonesia')
        self.input_data()
        self.data_provinsi = self.tree.get_data_by_level(2)

    def input_data(self):
        print('get data...')
        data = Fetch.all_data()
        print('get data success')
        # add level 2 data
        for item in data:
            self.tree.add_children(item['attributes']['Provinsi'], self.tree.root)
        # add level 3 data
        for x in range(len(self.tree.root.children)):
            for (key, _) in item['attributes'].items():
                if 'Kasus' in key:
                    self.tree.add_children(data[x]['attributes'][key], self.tree.root.children[x])

    def show_menu(self):
        print('========| data covid19 |=========')
        print('1. data covid 19 indonesia')
        print('2. list provinsi')
        print('3. data by provinsi')
        print('4. credit')
        print('=================================')
        try:
            pilih = int(input('pilih menu :=> '))
            self.process_menu(pilih)
        except:
            system('cls' if name == 'nt' else 'clear')
            print('input yg anda masukkan salah !')
            self.show_menu()

    def process_menu(self, pilih):
        if pilih == 1:
            try:
                data = self.tree.get_leaf(self.tree.root)
                for x in range(len(data)):
                    print(f'=====| KASUS DI {self.data_provinsi[x]} |=====')
                    print('total kasus     :=>', data[x].total)
                    print('kasus aktif     :=>', data[x].aktif)
                    print('kasus sembuh    :=>', data[x].sembuh)
                    print('kasus meninggal :=>', data[x].meninggal)
            except Exception as e:
                print("[ERROR] ", e)
        elif pilih == 2:
            self.data_provinsi = self.tree.get_data_by_level(2)
            # print(d)
            for x in range(len(self.data_provinsi)):
                print(f'{x+1}. {self.data_provinsi[x]}')
        elif pilih == 3:
            provinsi = int(input("masukkan nomor provinsi :=> "))
            try:
                node = self.tree.search_by_value(self.data_provinsi[provinsi-1])
                data = self.tree.get_leaf(node)
                for x in range(len(data)):
                    print(f'=====| KASUS DI {node.value} |=====')
                    print('total kasus     :=>', data[x].total)
                    print('kasus aktif     :=>', data[x].aktif)
                    print('kasus sembuh    :=>', data[x].sembuh)
                    print('kasus meninggal :=>', data[x].meninggal)
            except Exception as e:
                print("[ERROR] ", e)
        elif pilih == 4:
            text = """ __________________________________
<   Albani Kautsar (1910511047)    >
<   Alfian Pratama (1910511050)    >
<   Jamie Saviola  (1910511051)    >
<   M.Fathurrahman (1910511058)    >
<   Wahyu Miftahul (1910511060)    >
<   Abril Muhammad (1910511061)    >
< from developer for developer <3  >
 ----------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||"""
            print(text)
        else:
            print('menu yang anda masukkan salah')
