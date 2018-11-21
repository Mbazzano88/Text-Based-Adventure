##Give Tiles module access to modueles Items, Enemies

import items, enemies, actions, world
##Create template for all tiles to expand upon
##Called abstract base class, never created directly, only expanded upon
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("I work")
        print(self.x)
        print(self.y)
    def adjacent_moves(self):
        ##returns all move actions for adjacent tiles
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
            print ("East")
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
            print ("West")
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
            print ("North")
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
            print ("South")
        return moves

    def available_actions(self):
        ##Returns all of the available actions in this room
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

    def intro_text(self):
        raise NotImplementedError()
    ##NotImplementedError warns us if MapTile is created directly

    ##player parameter serving as a placeholder
    def modify_player(self, player):
        raise NotImplementedError()

##Create tile subclass
class StartingRoom(MapTile):
    def intro_text(self):
        return "You find yourself in a cave with a flickering torch\
on the wall. You can make out four paths, \
each as dark and forboding as the next."

    def modify_player(self, the_player):
        ##Starting room has no action on player
        pass

##Create tile where item is found
    ##no item called Player yet, but it will happen
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)

##Create tile where enemy is encountered

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp - the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining."\
                  .format(self.enemy.damage, the_player.hp))
    ##overrides default mapTile behavior based on status of Enemy
    def available_actions(self):
        if self.enemy.is_alive():
            return[actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


##Other types of tiles
##Another MapTile (no action)
class EmptyCavePath(MapTile):
    def intro_text(self):
        return"A long, dimly lit corridor.  \
You hear water dripping from somewhere nearby and feel compelled to move on."
    def modify_player(self, the_player):
        #Room has no action on player
        pass

##Two-way intersection room
class TwoWayIntersection(MapTile):
    def intro_text(self):
        return"You face a solid stone wall.  The path continues to the east \
and to the west."
    def modify_player(self, the_player):
        #Room has no action on player
        pass

##Four-way intersection room
class FourWayIntersection(MapTile):
    def intro_text(self):
        return"The path opens up into a large intersection.  You can continue, \
go east, west, or back. You feel eyes on you."
    def modify_player(self, the_player):
        #Room has no action on player
        pass

##Exit to the cave room.  VICTORY
class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return"A bright light shines in the distance.  You are filled with \
hope as you feel a cool breeze on your face.  You run towards it, leaving\
the stench of death and decay behind.\n \n YOU WIN!"
    def modify_player(self, the_player):
        player.victory = True
    
#A room where a spider attacks
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
    def intro_text(self):
        if self.enemy.is_alive():
            return"An eight-legged monstrosity leaps down from the ceiling!"
        else:
            return"Spider icor and severd legs are strewn about the floor."

##A room where a kobold attacks
class KoboldRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Kobold())
    def intro_text(self):
        if self.enemy.is_alive():
            return"A gnarled, ugly creature approaches with a club raised!"
        else:
            return"The smell of dead kobold hangs thick in the room."

##A room where you find a French-occupied castle
class FrenchCastleRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.FrenchCastle())
    def intro_text(self):
        if self.enemy.is_alive():
            return"The French soldiers taunt you relentlessly. \
cows, sheep, and other livestock rain down upon you."
        else:
            return"Polka-dotted officers lay massacred. The castle is yours!"

##A room where an ogre attacks
class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())
    def intro_text(self):
        if self.enemy.is_alive():
            return"A hulking ogre looms out of the darkness."
        else:
            return"A large, lifeless body slumps in a corner."

##A room where you find a dagger
class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
    def intro_text(self):
        return"Something small glints in the corner of the room.\
 You pick up a dagger!"

##A room where you find a hammer
class FindHammerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Hammer())
    def intro_text(self):
        return"A skeletal corpse of a Dwarf holds a large ornate hammer. \
you pry the weapon from the boney hands."

##A room where you find (x) gold
class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))
    def intro_text(self):
        return"Shiny, round, and precious.  You collect gold that some \
unfortunate adventurer left behind."

class Find25GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(25))
    def intro_text(self):
        return"Shiny, round, and precious.  You collect gold that some \
unfortunate adventurer left behind."

class Find50GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(50))
    def intro_text(self):
        return"Shiny, round, and precious.  You collect gold that some \
unfortunate adventurer left behind."



