from cats_constructor import Cat

cats_data = cats = [
    {
     'name': 'Барон',
     'sex': 'мальчик',
     'age': 2
    },
    {
     'name': 'Сэм',
     'sex': 'мальчик',
     'age': 2
    },
]

for cat in cats_data:
    cat_obj = Cat(name=cat.get('name'),
                  sex=cat.get('sex'),
                  age=cat.get('age'))
    print(cat_obj.display_info())