class Animals:
    """Классификация животных"""

    def __init__(self, name, atype, country):
        """Атрибуты, описывающие животных"""
        self.name = name  # название животного
        self.atype = atype  # тип (млекопитающие, птица и т.п.)
        self.country = country  # страна обитания
        self.population = 998
        print('Вы добавили новый экземпляр')

    def flight(self):
        """"Экземпляр летает"""
        print(self.name + ' летает')

    def sweem(self):
        """"Экземпляр плавает"""
        print(self.name + ' плавает')

    def breeds(self):
        """"Экземпляр размножается"""
        print(self.name + ' размножается')

    def get_population(self):
        """Получение численности популяции"""
        description = self.name + ' класс ' + self.atype + ' обитают в ' + self.country + ', не первышают ' \
            + str(self.population) + ' особей'
        print('Наблюдаемый экземпляр:', description)

    def update_population(self, quant):
        """Обновление численности популяции"""
        self.population = quant
