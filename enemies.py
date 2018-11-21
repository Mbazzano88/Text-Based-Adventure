##creating a base class called Enemy

class Enemy:
    def __init__(self, name, hp, damage, description):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.description = description

    def is_alive(self):
        return self.hp >0

##creating sublcasses of Enemy to define specific types of enemies

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp = 10, damage = 2, \
                         description="KILL IT WITH FIRE")

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp = 30, damage = 8, \
                         description="Strong, but not very smart.")

class FrenchCastle(Enemy):
    def __init__(self):
        super().__init__(name="French Castle", hp = 100, damage = 10, \
                         description="RUN AWAAAYYYYYY")

class Kobold(Enemy):
    def __init__(self):
        super().__init__(name="Kobold", hp = 5, damage = 1, \
                         description="You no take candle!")


    
