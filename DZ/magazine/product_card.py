class Product:
    """Карточка товара"""

    def __init__(self, name, price, info, locator, image):
        """Атрибуты товара"""
        self.name = name  # Наименование
        self.price = price  # Цена
        self.info = info  # Описание товара
        self.locator = locator  # locator
        self.image = image  # Можно сравнимть картинки. Пока думаю как
        # print('Вы добавили новый товар: ' + name, price)

    # def flight(self):
    #     """"Экземпляр летает"""
    #     print(self.name + ' размножается')


product_1 = Product('Sauce Labs Backpack', 29.00, 'carry.allTheThings() with the sleek, '
                                                  'streamlined Sly Pack that melds uncompromising '
                                                  'style with unequaled laptop and tablet protection.', '', '')

product_2 = Product('Sauce Labs Bolt T-Shirt', 39.00, 'carry.allTheThings() with the sleek, '
                                                      'streamlined Sly Pack that melds uncompromising '
                                                      'style with unequaled laptop and tablet protection.', '', '')
product_3 = Product('Sauce Labs Onesie', 49.00, 'carry.allTheThings() with the sleek, '
                                                'streamlined Sly Pack that melds uncompromising '
                                                'style with unequaled laptop and tablet protection.', '', '')
product_4 = Product('Sauce Labs Bike Light', 59.00, 'carry.allTheThings() with the sleek, '
                                                    'streamlined Sly Pack that melds uncompromising '
                                                    'style with unequaled laptop and tablet protection.', '', '')
product_5 = Product('Sauce Labs Fleece Jacket', 69.00, 'carry.allTheThings() with the sleek, '
                                                       'streamlined Sly Pack that melds uncompromising '
                                                       'style with unequaled laptop and tablet protection.', '', '')
product_6 = Product('Test.allTheThings() T-Shirt (Red)', 29.00, 'carry.allTheThings() with the sleek, '
                                                                'streamlined Sly Pack that melds uncompromising '
                                                                'style with unequaled laptop and tablet protection.',
                    '', '')
