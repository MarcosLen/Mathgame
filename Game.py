from helper import operation


exit = False

while not exit:
    try:
        name = input('\nWelcome to Mathgame. Please, insert your name: ')
        level = 0
        sel_new_level = True
        while not(level==1 or level==2 or level==3) and sel_new_level is True:
            try:
                level = int(input('\nIngrese el nivel de dificultad: 1-Facil, 2-Medio, 3-Dificil: '))
                continu = 'y'
                _ = input('\nNivel de dificultad {}. Pulse una tecla para comenzar...'.format(level))
                while continu=='y':
                    try:
                        cuenta, r = operation(level=level)
                        u = input('{}= '.format(cuenta))

                        if int(u) == r:
                            print('\033[32m' + 'Congratulations {}, you are correct!!'.format(name) + '\033[0m')
                        else:
                            print('\033[91m' + 'Ups, wrong answer :(' + '\033[0m')

                        continu = input('\nDo you want to continue? [y/n] ')
                    except:
                        print('\nSelected not continue...')

                sel_new_level = bool(input('\nSelect new level? [y/n] ')=='y')
                level = 0
            except:
                print('\033[91m' + '\n\nLevel (1, 2, 3) expected. Try again.' + '\033[0m')

    except:
        print('\033[91m' + '\n\nName expected. Try again!!' + '\033[0m')

    exit = bool(input('\nContinue in Mathgame? [y/n] ')=='n')
print('\n\nThanks for playing, come back soon!')
