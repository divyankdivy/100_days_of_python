from Art import treasure
print(treasure)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Which direction would you like to go? left or right\n")

if direction == 'left':
    swim = input("Your boat is on the way, would you like to wait or swim? \n")
    if swim == 'wait':
        door = input("Choose a door between 'yellow' 'blue' and 'red'.\n")
        if door == 'yellow':
            print("You Won")
        elif door == 'blue':
            print("eaten by beast\nGame Over")
        elif door == 'red':
            print("Burned by fire\nGame Over")
    elif swim == 'swim':
        print('You were attacked by trout\nGame Over')
elif direction == 'right':
    print("You fall into a hole.\nGame Over")