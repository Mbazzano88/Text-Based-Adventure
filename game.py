##THE GAME LOOP

import world
from player import Player

def play():
    print("Loading Tiles...")
    world.load_tiles()
    print("Loading Player...")  ####CODE STOPS HERE
    player = Player()
    ##load starting room and display text
    print("Loading Room")
    room = world.tile_exists(player.location_x, player.location_y)
    print(room)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        ##THE LOOP BEGINS HERE
        room=world.tile_exists(player.location_x, player.location_y)
        print (player.location_x, player.location_y)
        room.modify_player(player)
        ##check again since the romo could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input=input("Action: ")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

if __name__ =="__main__":
    play()
