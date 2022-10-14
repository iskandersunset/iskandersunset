class Car:
    """Классификатор легковых автомобилей"""

    def __init__(self, brand, year, volume, price, mileage):
        """"Инициализация атрибутов класса Car"""
        self.brand = brand  # марка авто
        self.year = year  # год выпуска
        self.volume = volume  # объем двигателя
        self.price = price  # цена
        self.mileage = mileage  # пробег
        self.wheels = 4  # кол-во колес
        self.tip = 'легковой'
        print('Новый автомобиль добавлен:', self.brand, self.year, 'г.в.')

    def get_info(self):
        """Вывод информации о экземпляре"""
        car_info = 'Поступил новый ' + self.tip + ' автомобиль: марки ' + self.brand + ' ' + str(self.year) + ' г.в.' + \
            ', двигатель объемомом: ' + str(self.volume) + ' л.' + ', цена: ' + str(self.price) + ' руб., пробег: ' \
            + str(self.mileage) + ' км.'
        return car_info

    def update_price(self, price):
        """Изменение цены авто"""
        self.price = price


class Truck(Car):
    """Классификатор грузовых автомобилей"""

    def __init__(self, brand, year, volume, price, mileage):
        """Инициализация атрибутов класса Truck"""
        super().__init__(brand, year, volume, price, mileage)
        self.tip = 'грузовой'
        self.wheels = 8


car_1 = Car('Audi', 1999, 1.8, 400000, 120000)
car_1.update_price(100)
car_2 = Truck('Man', 2000, 5, 20000, 1000000)
car_2.update_price(5000)
print('У авто ' + str(car_1.brand) + ' ' + str(car_1.wheels) + ' колес(а)')
print(car_1.get_info())
print(car_2.get_info())
