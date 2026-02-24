class Shop:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def open(self):
        print('Dokon ochildi')


class OnlineShop(Shop):
    def __init__(self, name, adress, website):
        super().__init__(name, adress)
        self.website = website

    def open(self):
        super().open()
        print(f'Sayt manzili: {self.adress}')


shoop = OnlineShop('Uzum market', 'Tashkent', 'uzuum.com')
# shoop.open()
