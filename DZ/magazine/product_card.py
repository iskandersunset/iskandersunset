class Product:
    """Карточка товара"""

    def __init__(self, name, price, info):
        """Атрибуты товара"""
        self.name = name  # Наименование
        self.price = price  # Цена
        print('Вы добавили новый товар')

    # def flight(self):
    #     """"Экземпляр летает"""
    #     print(self.name + ' размножается')
