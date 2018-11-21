_world = {}
starting_position = (0, 0)

def load_tiles():
    ##Parses a file that describes the world space into the _world object
    with open('map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t')) #Assumes all rows contain the same number

    for y in range(len(rows)):
        cols = rows[y].split('\t')
        #print("beginning second for loop")
        for x in range (x_max):
            tile_name = cols[x].replace('\r\n', '')
            #print("Tile Name", tile_name)
            #print(cols)
            #print (cols[x])
            if tile_name == "StartingRoom":
                global starting_position
                starting_position = (x, y)
                print(starting_position)
            #_world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
            if tile_name=='':
                _world[(x, y)] = None
            else:
                print(cols[x])
                print("Importing tiles breaks the program.")
                getattr(__import__('tiles'), tile_name)(x, y)
                                        

def tile_exists(x, y):
    return _world.get((x, y))
