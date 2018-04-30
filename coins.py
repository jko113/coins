def do_coinage():

    user_input = ''
    coins = 0

    while user_input != 'no':
        user_input = input('You have %s coins.\n\
Do you want another coin? yes/no ' % coins)
        user_input = user_input.lower()
        
        if user_input == 'yes':
            coins += 1
            
        elif user_input != 'no':
            print ('Invalid input. Type \'yes\' or \'no\'')
            continue
    else:
        print("You've exited the game. You amassed", str(coins), "coins.")