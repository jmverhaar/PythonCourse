#! /usr/bin/env python3

text = 'THis is good coffee'
print(text)
print(text[0:4])
print(text[-6:])
print(text[-1:-7:-1])

words = text.split()
print(words)

low = text.lower()
print(low)

title = text.title()
print(title)

rep = text.replace('coffee', 'tea')
print(rep)

g = "{} {} {} {} {}!".format('a', 'b', 'c', 'd', 'e')
print(g)

