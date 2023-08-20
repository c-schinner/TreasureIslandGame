print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("\n")

print("You wake up in an empty room, you remember a storm and a waved crashed into your boat and you blacked out.")
print("There are two doors in front of you that look like it will lead outside.")
print("\n")

answer1 = input('Do you choose the door on the left or right? Type "left" or "right"  ').lower()
if answer1 == "left":
    print("You walk outside and notice there is a path that leads into the palm tree forest. You walk down the path.")
    answer2 = input('You come across a fork in the road, to the left leads down deeper into the forest, the right takes you over a bridge crossing a river. Type "left" or "right" ').lower()
    print("\n")
    if answer2 == "right":
        answer3 = input('You have made it across the bridge safely, and see two paths, straight leads to a mountain, and right leads into a clearing. Type "straight" or "right" ').lower()
        if answer3 == "straight":
            print("\n")
            answer4 = input('Into the mountain you go inside a cave and inside the cave has three doors to pick, left, straight and right. Type "left" "straight" or "right" ').lower()
            if answer4 == "right":
                print("\n")
                print("You find the lost treasure! Congratulations, hurry back and find a way off the island.")
            else:
                print("The natives lock you in their dungeons and feast on you... YOU LOSE")
        else:
            print("The clearing gave you no protection from wild animals which decided to eat you... YOU LOSE")
    else:
        print("A tribe of natives have been hunting you since you left the cabin, and capture you for food....YOU LOSE")
else:
    print("You fall into a dungeon made by natives, they want you for food... YOU LOSE")


