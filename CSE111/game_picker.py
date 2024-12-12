import csv

NAMES_INDEX = 0
PLAYTIME_INDEX = 1
PRIORITY_INDEX = 2
PLAYED_INDEX = 3
BEATEN_INEDX = 4
REPLAYABLE_INDEX = 5
MULTIPLAYER_INDEX = 6

def read_games():
    """Reads the csv file with the game data into a compound dictionary, with game titles acting as 
    keys and each titles data being put into a complimentary list"""
    #create compound list to read the game data into
    game_compound_list = []
    #opens up games.csv 
    with open('games.csv', "rt") as csv_file:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            game_compound_list.append(row)
    return game_compound_list


def find_shortest_playtime(list, played, priority):
    """Finds the game with the shortest play time in the list. If specified, games that have been played before
    will be excluded and games that have priority will be returned instead of other games (even if they have
    higher play times)
    If there is more than one game that meets the shortest playtime criteria, returns all games with that play-time 
    and matching criteria"""

    smallest = 0
    launched = lambda list: list[PLAYED_INDEX]
    important = lambda list: list[PRIORITY_INDEX]

        



def adjust_list(key, played, priority):
    """Edits the csv file if the user indicates changes need to made to a games data regarding whether or not
    they've played it or if they consider it a priority (flips boolean values)"""

def main():
    """Does literally everything"""
    global beaten
    global replay
    games_list = read_games()
    print("Welcome! I'm here to help you pick you a game to play today. Just got a couple questions to ask first, this won't take too long\n")
    p = input("Would you like a game that you've played already? (Y/N): ")
    p = p.lower()
    played = True if p=='y' or p=='yes' else played = False
    if played == True:
        b = input("Do you care if you've beaten this game already? (Y/N): ")
        b = b.lower()
        beaten = False if b=="y" or b=='yes' else played = True
        r = input("Alright, does this game need to be replayable? (Y/N): ")
        r = r.lower()
        replay = True if r =='y' or r == 'yes' else replay = False
    pr = input("Excellent. Now, would you like on the games on your 'Priority' list? (Y/N): ")
    pr = pr.lower()
    priority = True if pr == 'y' or pr == 'yes' else priority = False
    m = input("Very cool. Now, does this game *need* to have Multiplayer? (Y/N): ")
    m = m.lower()
    multi = True if m == 'y' or m =='yes' else multi = False

    chosen_one = find_shortest_playtime()
    print(f"Here is a game that meets your criteria: {chosen_one}")
    the_choice = input("Are you satisfied with this choice? (Y/N): ")
    the_choice = the_choice.lower()
    if the_choice == 'n' or the_choice =="no":
        print("Very sorry about that, ")



if __name__ == "__main__":
    main()