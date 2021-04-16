import time
import random


def print_pause(message_to_print, delay=1):
    # Print message with delay. We can pass optional parameter - delay timer.
    # It was set to 1 second by default
    print(message_to_print)
    time.sleep(delay)


def valid_input(prompt, options):
    # We ask user for input till he gives on of the options from the
    # 'options' list
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response


def intro(enemy):
    # We give here background information to a player
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + enemy + " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.")


def combat_update(sword, enemy, health_points):
    # Sword can do much more damage than dagger
    if sword:
        max_damage = 100
    else:
        max_damage = 20
    health_points[0] -= random.randint(1, 50)
    health_points[1] -= random.randint(1, max_damage)
    return health_points[0], health_points[1]


def fight(sword, enemy):
    # Initialize health points
    player_hp = 100
    enemy_hp = 100
    # Fight will start from Round 1
    round_number = 1
    if sword:
        print_pause("As the " + enemy + " moves to attack, you unsheath your "
                    "new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
    else:
        print_pause("You do your best..")

    print_pause("Your start health points: " + str(player_hp))
    print_pause(enemy.title() + "'s start health points: " + str(enemy_hp))

    # Fight until someone (or both) loses
    while player_hp > 0 and enemy_hp > 0:
        print_pause("Round " + str(round_number))
        print_pause("It was a fierce fight...")
        player_hp, enemy_hp = combat_update(sword, enemy,
                                            [player_hp, enemy_hp])
        print_pause("Your health points: " + str(max(player_hp, 0)))
        print_pause(enemy.title() + "'s health points: " +
                    str(max(enemy_hp, 0)))
        round_number += 1

    # Printing the result of the fight
    if player_hp <= 0 and enemy_hp <= 0:
        print_pause("You have rid the town of the " + enemy + ".")
        print_pause("But you also died. You were buried as a hero.")
    elif player_hp <= 0:
        print_pause("But you can't cope with " + enemy + ".")
        print_pause("You have been defeated!")
    elif enemy_hp <= 0:
        print_pause("And you have rid the town of the " + enemy + ". You are "
                    "victorious!")

    # Ask if player wants to play once again
    choice = valid_input("Would you like to play again? (y/n)",
                         ['y', 'n'])
    if choice == 'y':
        print_pause("Excellent! Restarting the game ...")
        adventure_game()
    else:
        print_pause("Thanks for playing! See you next time.")


def cave(sword, enemy):
    # At the first entrance player collects the sword
    print_pause("You peer cautiously into the cave.")
    if not sword:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        sword = True
    else:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    field(sword, enemy)


def house(sword, enemy):
    # Here player decides whether he should fight or run away
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                "out steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    print_pause("The " + enemy + " attacks you!")
    if not sword:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    choice = valid_input("Would you like to (1) fight or (2) run away?",
                         ['1', '2'])
    if choice == '1':
        fight(sword, enemy)
    if choice == '2':
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.")
        field(sword, enemy)


def field(sword, enemy):
    # Here player decides where to go
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = valid_input("(Please enter 1 or 2.)\n", ['1', '2'])
    if choice == '1':
        house(sword, enemy)
    if choice == '2':
        cave(sword, enemy)


def adventure_game():
    # Player doesn't have a sword at the beginning of the game
    sword = False
    # the enemy is chosen randomly from the list
    enemies = ['dragon', 'gorgon', 'wicked fairie', 'pirate']
    enemy = random.choice(enemies)
    # play the scenario of the game
    intro(enemy)
    field(sword, enemy)


adventure_game()
