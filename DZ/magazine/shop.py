from DZ.magazine.product_card import Product


class Birds(Animals):
    """Подкласс птицы"""

    def __init__(self, name, atype, country, deti):
        """Инициализация атрибутов класса Animals"""
        super().__init__(name, atype, country)
        self.deti = deti

    def get_deti(self):
        """Получение потомства"""
        print('Потомство:', self.deti)

    def get_population(self):
        """Переопределение описнаи класса"""
        if self.name == 'аист':
            description = self.name + ' класс ' + self.atype + ', потомство: ' + str(self.deti) + ', особей'
            # print('Популяция', description)
            return description
        else:
            return 'ошибка'


aist_1 = Birds('Курица', 'птица', 'Беларусь', 50)
aist_1.get_deti()
aist_1.update_population(2300)
aist_1.get_population()
print('Наблюдаемый экземпляр: ', aist_1.get_population())

slon = Animals('слон', 'млекопитающее', 'Индия')
slon.get_population()
