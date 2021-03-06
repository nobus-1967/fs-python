# Вариант с использованием магического метода __repr__ (основан на варианте 1)

class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    def __repr__(self):
        return f'{self.name}, г. {self.city}'


class StatusVolunteer(Volunteer):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status
        
    def __repr__(self):
        return f'{self.name}, г. {self.city}, статус "{self.status}"'
        
petr_ivanov = Volunteer('Петр Иванов', 'Санкт-Петербург')
ivan_petrov = StatusVolunteer('Иван Петров', 'Москва', 'Наставник')

guests = [petr_ivanov, ivan_petrov]
print('Список волонтеров:')
for index, guest in enumerate(guests):
    print(f'{index + 1}) {guest}')
