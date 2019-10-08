#! usr/bin/env python3

def mathmath():
    x = None
    y = None
    z = None
    for key,value in locals():
        value = int(input("Input a value: "))
   
   # x = int(input("Input a value: "))
   # y = int(input("Input a value: "))
   # z = int(input("Input a value: "))
    total = (x + y)/z

    print(total)
    return
   
mathmath()
