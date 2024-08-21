 #Task 1

place = input ("choose a place: forest or cave?")

if place =="forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("you found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action.")

#task 2
elif place == "cave":
    cave_action = input("light a torch or proceed in the dark? ")
    if cave_action == "light a torch":
        print("You light the torch and see beautiful cave paintings on the walls!")
    elif cave_action == "proceed in the dark":
        print("You proceed in the dark and stumble upon a hidden passage!")
    else:
        print("Invalid action.")
else:
    print("Invalid place.")