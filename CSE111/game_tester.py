from game_picker import find_shortest_playtime, adjust_list, read_games
import csv #if I need it
from pytest import approx
import pytest

#indexes for needed values
NAMES_INDEX = 0
PLAYTIME_INDEX = 1
PRIORITY_INDEX = 2
PLAYED_INDEX = 3
BEATEN_INDEX = 4
REPLAYABLE_INDEX = 5
MULTIPLAYER_INDEX = 6

#contains a sampling from games.csv, for easier edge-case testing
small_games_list = [
    ["A Hat in Time",9.5,False,True,True,True,True],
    ["Baldur's Gate 3",68.5,True,True,False,True,True],
    ["Chrono Trigger",23,True,True,False,True,False],
    ["The Great Ace Attorney Chronicles",67,True,True,True,True,False],
    ["Yooka Laylee and the Impossible Lair",13,False,True,False,True,False],
    ["Tyrion Cuthbert: Attorney of the Arcane",15.5,False,True,True,True,False],
    ["NIER Automata",21,True,True,False,True,False],
    ["Octopath Traveler ",60.5,True,True,False,True,False]
]

def test_read_games():
    """Ensures that read_games produces a compound list"""
    #Call read_games to make the list
    games_list = read_games('games.csv')
    #check if games_list is a list
    assert isinstance(games_list, list)
    #check if each item in games_list is also a list
    for inner_list in games_list:
        assert isinstance(inner_list, list)

def test_find_shortest_playtime():
    """Ensures that find_shortest_playtime works properly, by checking known test-cases"""
    assert find_shortest_playtime(small_games_list,False,True,True,False,False) == None
    assert find_shortest_playtime(small_games_list,False,False,True,True,True) == None
    assert find_shortest_playtime(small_games_list,True,True,True,True,False) == "The Great Ace Attorney Chronicles"
    assert find_shortest_playtime(small_games_list,True,False,True,True,False) == "NIER Automata"
    assert find_shortest_playtime(small_games_list,True,False,True,True,True) == "Baldur's Gate 3"
    assert find_shortest_playtime(small_games_list,False,False,True,False,False) == None

def test_adjust_list():
    """Ensures that adjust_list adjusts the list properly"""
    #calls in the list
    games_list = read_games('games.csv')
    #checks to make sure the known value is still True
    for inner_list in games_list:
        if "NIER Automata" in inner_list:
            assert inner_list[PRIORITY_INDEX] == True
    #adjusts the list
    adjust_list(games_list,"NIER Automata",False)
    #now it checks if the known value has changed, just like the function should do
    for inner_list in games_list:
        if "NIER Automata" in inner_list:
            assert inner_list[PRIORITY_INDEX] == False

pytest.main(["-v", "--tb=line", "-rN", __file__])
