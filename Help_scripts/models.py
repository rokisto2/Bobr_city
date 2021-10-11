class Attractions:
    def __init__(self, name, address, contennt, img):
        self.name = name
        self.address = address
        self.contennt = contennt
        self.img = img

    def show(self):
        print("Название", self.name)
        print('адресс',self.address)
        print('Содержимое', self.contennt)
        print('Кортинки', self.img)
        print('-' * 50)
