def cls():
    print('\n' * 80)


def dead(reason):
    cls()
    print('           *****')
    print('        **********')
    print('       ***  **   **')
    print('       ************')
    print('         *******')
    print('         * * * *')
    print('\n' * 5)
    print(reason)


def two_doors():
    cls()
    print('   *******    *******')
    print('   *     *    *     *')
    print('   *  *  *    *  *  *')
    print('   *     *    *     *')
    print('   *     *    *     *')
    print('**************************')
    print('')
    print('')
    print('')
    print('')
    print('You are facing two giant doors, one on the left and one on the\n'
          'right. Which path will you choose?')


def tower():
    two_doors()
    choice = input("> ")
    words = choice.split()

    good_words = ['left', 'right', 'open']

    if any(gword in words for gword in good_words):
        cls()
        print('\n' * 9)
        print('Congratulations you have found the legendary treasure!\n'
              'You are a hero!\n'
              'Your fame will surely spread, and you will become the new king.')
    else:
        dead("You are overrun by monsters. You are never heard from again.")


def left_of_tower():
    dead("You are overrun by monsters. You are never heard from again.")


def right_of_tower():
    dead("You are overrun by monsters. You are never heard from again.")


def courtyard():
    cls()
    print('   *     ******       *')
    print('   *     *    *       *')
    print('   * * * *    * * * * *')
    print('  *      * ** *        *')
    print(' *                      *')
    print('**************************')
    print('')
    print('')
    print('You enter into a large enclosed courtyard with a single tower in\n'
          'the center. Its dark and you cant see very well, but it looks like\n'
          'There are doors on the tower, and there are large empty spaces to\n'
          'the left and the right of the tower.')

    choice = input("> ")
    words = choice.split()

    if 'left' in words:
        left_of_tower()
    elif 'right' in words:
        right_of_tower()
    elif 'tower' in words:
        tower()
    else:
        dead('A giant Golem attacks you from behind. You are dead.')

def doors_to_courtyard(from_room):
    two_doors()
    choice = input("> ")
    words = choice.split()

    good_words = ['left', 'right', 'open']

    if any(gword in words for gword in good_words):
        courtyard()
    elif from_room == 'golem_room':
        dead('The Golem rips out your spine.')
    else:
        dead("You stumble around the room until you starve.")


def golem_room():
    cls()
    print('        *  ***  *         ')
    print('         * * * *          ')
    print('          *****           ')
    print('           ***        *** ')
    print('           * *        *** ')
    print('**************************')
    print('')
    print("It's a trap!")
    print('A giant spiked ball falls from the ceiling and prevents you from\n'
          'leaving the room through the door you just walked through.\n'
          'A Golem stands in the middle of the room.\n'
          'You can see two doors on the far wall.')

    choice = input("> ")
    words = choice.split()

    if "run" in words:
        doors_to_courtyard('golem_room')
    elif "fight" in words:
        dead("You punch and claw at the Golem, then he smashes you dead.")
    else:
        dead("The Golem smashes your head like a grape.")


def treasure_room():
    cls()
    print('')
    print('')
    print('         *******')
    print('        *   $   *')
    print('        *       *')
    print('**************************')
    print('')
    print('You found a treasure room!')

    input("> ")
    doors_to_courtyard('treasure_room')


def start():
    two_doors()
    choice = input("> ")
    words = choice.split()

    if "left" in words:
        golem_room()
    elif "right" in words:
        treasure_room()
    else:
        dead("You stumble around until you starve.")


start()
