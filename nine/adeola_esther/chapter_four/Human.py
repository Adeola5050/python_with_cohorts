class Human:
    def __init__(self, name, gender, height, age, nationality, complexion):
        self.name = name
        self.gender = gender
        self.height = 0
        self.age = 0
        self.nationality = nationality
        self.complexion = "Black"

        def set_age(age):
            self.age=age
            def set_height(height):
                self.height= height

