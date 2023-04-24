from class_cat import Cat
cats = [
    {
    "nickname": "Барон",
    "gender": "мальчик",
    "age": 2,
    },
    {
    "nickname": "Сэм",
    "gender": "мальчик",
    "age": 2,
    }
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(f'\nИмя:{cat_obj.nickname}', f'\nПол:{cat_obj.gender}', f'\nВозраст:{cat_obj.age}')

