class Cat:
    def __init__(self, nickname='', gender='', age=0):
        self.nickname = nickname
        self.gender = gender
        self.age = age

    def init_from_dict(self, cats_dict):
        self.nickname = cats_dict.get("nickname")
        self.gender = cats_dict.get("gender")
        self.age = cats_dict.get("age")
