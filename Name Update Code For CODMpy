#How_COD_Names_Their_Games

class Game:
    name = "Call of Duty"

    @classmethod
    def update_name(cls):
        add = input("Update: ")
        if add == "warzone":
            add = add.upper()
        else:
            add = add.title()
        cls.name = cls.name+": "+add
        return cls.name

    @staticmethod
    def announcements():
        print("Keep An Eye OUT!")

x = Game.update_name()
print(f"{x} Dropping Soon...")
Game.announcements()
