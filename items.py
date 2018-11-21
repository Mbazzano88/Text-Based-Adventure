class Item():
	##The base class for all items##
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
            return "{}\n=====\n{}\nValue: {}\n"\
                       .format(self.name, self.description, self.value)
##Creating gold as a superclass of item
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="Me want shiny round!!".format(str(self.amt)), 
                         value = self.amt)

##Creating a superclass called weapons in Item
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str(self):
        return "{}n=====\n{}Value: {}\nDamage: {}"\
               .format(self.name, self.description, self.value, \
                       self.damage)

##Extending Weapon to include specific weapons
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                       description="Good for bludgeoning,\
bad for Halloween treats.",
                       value = 0,
                       damage = 5)

class Dagger(Weapon):
    def __init__(self):
        super().__init(name="Dagger",
                       description="Useful for the slyest of flourishes.",
                       value = 10,
                       damage = 10)

class Shuruken(Weapon):
    def __init__(self):
        super().__init(name="Shuruken",
                       description="Are you sure that's how it's pronounced?",
                       value = 8,
                       damage = 8)
class Hammer(Weapon):
    def __init__(self):
        super().__init(name="Hammer",
                       description="Aludra SMASH.",
                       value = 25,
                       damage = 15)
        
                       
