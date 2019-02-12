# A complete text game, the program will let users move through rooms based on user input and 
# get descriptions of each room. To create this, you’ll need to establish the directions in which 
# the user can move, a way to track how far the user has moved (and therefore which room he/she is in), 
# and to print out a description. You’ll also need to set limits for how far the user can move. 
# In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.” 


rooms = {'sitting': {'name': 'in the sitting room of the abadoned house',     'east':'bedroom', 'north': 'chamber',
        'text': 'The dusty floors and walls are cold and damp.'},
    'bedroom': {'name': 'a small bedroom', 'west': 'sitting', 'north': 'chamber', 'text': 'This seems to be a haven for long lost souls. The deceased clothes are in the closet and the souls reflect on you in the mirror. The windows refuse to open.', 
        },
    'chamber': {'name': 'a torture chamber', 'north': 'sitting', 'west': 'underground',     
        'text': 'There is an executioner with an axe is ready to chain and murder you.'},
    'underground': {'name': 'the house basement', 'east': 'chamber', 'north': 'bedroom', 
        'text': 'This place smells of rot and dead bodies. You must retrieve the knife to survive.'}}
directions = ['north', 'south', 'east', 'west','left']
current_room = rooms['sitting']
while True:
    print()
    print('You are in {}.'.format(current_room['name']))
    print(current_room['text'])
    command = input('\nWhich direction do you move? ').strip()
    if command == '':
        print("I don't understand that command.")
        print("Enter other direction to proceed or 'q' to quit")
    elif command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            print("Wall!! You can't move further in that direction.")
            print("Enter other direction to proceed or 'q' to quit")
    elif command.lower() in ('q', 'quit'):
        break
    else:
        print("I don't understand that command.")
        print("Enter other direction to proceed or 'q' to quit")