#! usr/bin/env python3

def showInstructions():
    print('''
    RPG Game
    ========
    Commands:
        go [direction]
        get [item]
    ''')

def showStatus():
    print('----------------------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory: ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You See a ' + rooms[currentRoom]['item'])
    print("----------------------------------------")

inventory = []

rooms = {
            'Hall': {
                    'south': 'Kitchen',
                    'east': 'Dinning Room',
                    'item': 'key'
                },
            'Kitchen': {
                    'north': 'Hall',
                    'item': 'Monster',
                },
            'Dinning Room': {
                    'west': 'Hall',
                    'south': 'Garden',
                    'item': 'potion'
                },
            'Garden': {
                    'north': 'Dinning Room'
                }
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    move = ''

    while move == '':
        move = input('>')

    move = move.lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]

        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print('Picked up ' + move[1])
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + [move[1]] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster got you... GAME OVER.')
        break
    
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You Win!')
        break
