# Вариант с использованием магического метода __repr__ и класса на основе списка

class Volunteer:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
    
    def __repr__(self):
        return f'{self.name}, г. {self.city}, статус "{self.status}"'


class VolunteerList(list):
    def __init__(self, name = "Список волонтёров"):
        super().__init__()
        self.name = name

    def __repr__(self):
        text = f"{self.name}:"
        for index, guest in enumerate(self):
            text += f"\n{index+1}) {guest}"
        return text


guests = VolunteerList("Список волонтёров 1")
guests.append(Volunteer('Петр Иванов', 'Санкт-Петербург', 'Волонтер'))
guests.append(Volunteer('Иван Петров', 'Москва', 'Наставник'))
print(guests)
