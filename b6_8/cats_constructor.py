class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.__sex
    
    def set_sex(self, sex):
        sex = sex.lower()
        if sex in ['мальчик', 'девочка']:
            self.__sex = sex
        else:
            print('Неправильно указан пол (укажите: мальчик или девочка)')
 
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Неправильно указан возраст (укажите: число больше 0)')
    
    def display_info(self):
        print("Имя:", self.name, "\nПол:", self.__sex, '\nВозраст:', self.__age)