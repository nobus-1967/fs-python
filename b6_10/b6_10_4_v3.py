# Вариант с использованием магического метода __repr__ и переменных класса

class Volunteer:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
    
    def __repr__(self):
        return f'{self.name}, г. {self.city}, статус "{self.status}"'


class VolunteerList(Volunteer):
    people = []
    
    def __init__(self, name, city, status):
        super().__init__(name, city, status)
        self.people.append(f'{self.name}, г. {self.city}, статус "{self.status}"')
       

petr_ivanov = VolunteerList('Петр Иванов', 'Санкт-Петербург', 'Волонтер')
ivan_petrov = VolunteerList('Иван Петров', 'Москва', 'Наставник')

guests = VolunteerList.people
for guest in guests:
    print(guest)
        
