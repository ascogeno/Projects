import csv

NAMES_INDEX = 0
PLAYTIME_INDEX = 1
PRIORITY_INDEX = 2
PLAYED_INDEX = 3
BEATEN_INDEX = 4
REPLAYABLE_INDEX = 5
MULTIPLAYER_INDEX = 6

def read_games(filename):
    """Reads the csv file with the game data into a compound list"""
    #create compound list to read the game data into
    game_compound_list = []
    #opens up games.csv 
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            row[PRIORITY_INDEX] = row[PRIORITY_INDEX].upper() == "TRUE"
            row[PLAYED_INDEX] = row[PLAYED_INDEX].upper() == "TRUE"
            row[BEATEN_INDEX] = row[BEATEN_INDEX].upper() == "TRUE"
            row[REPLAYABLE_INDEX] = row[REPLAYABLE_INDEX].upper() == "TRUE"
            row[MULTIPLAYER_INDEX] = row[MULTIPLAYER_INDEX].upper() == "TRUE"
            # Repeat for other boolean columns
            game_compound_list.append(row)
    return game_compound_list

def find_shortest_playtime(game_list, played, beaten, replay, priority, multi):
    """
    Finds the game with the shortest playtime in the list, considering boolean flags for prioritization.
    If multiple games have the same priority, the one with the smallest numerical value is chosen.
    DISCLAIMER: I tried my best for maybe 1-2 hours trying to write this function, and eventually caved and asked ChatGPT for help.
    Rather than simply give a suggestion, it wrote out the whole function. I then did my best Ctrl C Ctrl V.
    I wasn't aware of "Continue", but I think I get the idea
    """
    # Initialize variables to track the best match
    best_game = None
    smallest_playtime = float('inf')

    for game in game_list:
        playtime = game[PLAYTIME_INDEX]

        # Skip games with "N/A" in playtime
        if playtime == "N/A":
            continue

        # Ensure playtime is a number for comparison
        playtime = float(playtime)

        # Skip games that don't match the user's (my) preferences
        if played != game[PLAYED_INDEX]:
            continue
        if beaten != game[BEATEN_INDEX]:
            continue
        if replay != game[REPLAYABLE_INDEX]:
            continue
        if priority != game[PRIORITY_INDEX]:
            continue

        if multi and not game[MULTIPLAYER_INDEX]:  # If multiplayer is required and the game isn't multiplayer
            continue

        # Check for the smallest playtime, prioritizing games with higher priority
        if (
            playtime < smallest_playtime or
            (playtime == smallest_playtime and game[PRIORITY_INDEX])
        ):
            smallest_playtime = playtime
            best_game = game[NAMES_INDEX]

    return best_game

def adjust_list(list, chosen_one, priority):
    """Adjusts the list to change the priority of a given item, the 'Chosen One'. Returns that new list"""

    #loops through the list of lists
    for inner_list in list:
        #checks if chosen_one is in inner_list
        if chosen_one in inner_list:
            #change its priority
            inner_list[PRIORITY_INDEX] = priority 
            break
    #return the adjusted list
    return list

def new_file(list):
    """Takes in a list, and creates a new csv file names 'games_output.csv' with that list's contents. 
    Intended to be used after adjust_list"""
    #opens/creates games_output.csv, in a file mode that basically replaces all the stuff in games_output. very important detail
    with open("games_output.csv","wt") as output_file:
        #prints the header row, for consistency since the read_games function skips the top row. I guess this row could've printed
        #ooga booga, since it's never really meant to be human readable. But whatever, I'll keep it consistent
        print("Games,Playtime (Hours.Minutes),Priority?,Played:,Beaten?,Replayable?,Multiplayer?", file=output_file)
        #recreates the rest of the list
        for inner_list in list:
            print(f"{inner_list[NAMES_INDEX]},{inner_list[PLAYTIME_INDEX]},{inner_list[PRIORITY_INDEX]},{inner_list[PLAYED_INDEX]},{inner_list[BEATEN_INDEX]},{inner_list[REPLAYABLE_INDEX]},{inner_list[MULTIPLAYER_INDEX]}", file=output_file)


def get_yes_no(prompt):
    """Helper function to get a yes/no input from the user."""
    #ensures the response is in the correct case, and also gets ride of spaces. Admittedly wouldn't have thought of that myself
    response = input(prompt).strip().lower()
    #checks if the user's response is in the tuple, which appropriatley returns True or False
    return response in ('y', 'yes')

def main():
    """Runs the main program for game selection.
    You may have noticed that in class this section looked a lot messier. While I was busy stealing code from ChatGPT, I asked it
    if it could help make this main more concise. It did, and pretty well too from what I can tell. The biggest addition it made
    was the seperate 'get_yes_no' function, which is comparatively genius compared to what I was doing before."""
    games_list = read_games('games.csv')
    print("Welcome! I'm here to help you pick you a game to play today. Just got a couple questions to ask first, this won't take too long\n")

    # Collect user preferences
    played = get_yes_no("Would you like a game that you've played already? (Y/N): ")
    if played:
        beaten = get_yes_no("Do you want a game you've beaten already? (Y/N): ")
        replay = get_yes_no("Alright, does this game need to be replayable? (Y/N): ")
    else:
        beaten = replay = False

    priority = get_yes_no("Excellent. Now, would you like one of the games on your 'Priority' list? (Y/N): ")
    multi = get_yes_no("Very cool. Now, does this game *need* to have Multiplayer? (Y/N): ")

    #loops until the user likes the game that is picked
    while True:
        chosen_one = find_shortest_playtime(games_list, played, beaten, replay, priority, multi)
        print(f"Here is a game that meets your criteria: {chosen_one}")
        satisfied = get_yes_no("Are you satisfied with this choice? (Y/N): ")

        if satisfied:
            print("Sweet! Happy gaming 👍")
            break

        print("Very sorry about that, we'll pick another game for you.")
        if priority:
            change_priority = get_yes_no("Is this game no longer a priority? (Y/N): ")
            if change_priority:
                print("Alrighty, we'll get that changed for ya. Just one sec...")
                # Adjust priority and reload the game list
                new_file(adjust_list(games_list, chosen_one, False))
                games_list = read_games('games_output.csv')


if __name__ == "__main__":
    main()