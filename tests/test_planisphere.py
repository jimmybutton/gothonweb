import pytest
from gothonweb.planisphere import *

def test_room():
    gold = Room("GoldRoom",
    """This room has gold in it you can grab. There's a door to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

def test_load_room():
    assert load_room("central_corridor") == central_corridor
    with pytest.raises(ValueError):
        load_room("outer_corridor")

def test_name_room():
    my_room = load_room("central_corridor")
    assert name_room(my_room) == "central_corridor"
    with pytest.raises(TypeError):
        name_room("not_a_room")
    start = Room("Start", "You can go west and down a hole.")
    with pytest.raises(ValueError):
        name_room(start)

def test_gothon_game_map():
    start_room = load_room(START)
    assert start_room.go('shoot!') == generic_death
    assert start_room.go('dodge!') == generic_death

    room = start_room.go('tell a joke')
    assert room == laser_weapon_armory
