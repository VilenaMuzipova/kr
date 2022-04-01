import csv
class Details:
    def __init__(self, height, width, length, weight, color=None):
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight
        self.color = color
    def Height(self):
        print(f'Высота детали{self.height}')
    def Width(self):
        print(f'Ширина детали{self.width}')
    def Lenght(self):
        print(f'Длина детали{self.length}')
    def Weight(self):
        print(f'Масса детали{self.weight}')
    def Color(self):
        print(f'Цвет детали {self.color}')

class Ceh_color_queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def file(self):
        with open('details.txt', 'w')as file:
            file.write(f'В цеху {self.count} деталей')
            for i in range(0, self.count - 1):
                file.write(
                    f'Деталь 1: {self.queue[i].height},{self.queue[i].width},{self.queue[i].lenght},{self.queue[i].weight}'
                    f'{self.queue[i].color}')

detail_1 = Details(150, 50, 40, 30)
detail_2 = Details(100, 20, 60, 30)
detail_3 = Details(180, 40, 30, 50)
detail_4 = Details(170, 50, 30, 20)

detail = Details(19, 10, 3, 5)
detail.Height()
detail.Width()
detail.Lenght()
detail.Weight()



