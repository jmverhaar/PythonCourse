#!usr/bin/env python3

pets = ['Max', 'Garfeild', 'Spot']
fish = ['Goldy', 'Finny']

pets.append(fish)

print("I have 3 pets name {0}, {1}, and {2}, as well as 2 fish named {3[0]} and {3[1]}.".format(*pets))
