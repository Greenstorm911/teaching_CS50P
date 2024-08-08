

player = input('enter players name: ')


# if player == 'beyranvand':
#     print('team meli iran')
# elif player == 'ronaldo':
#     print('al nasr')
# elif player == 'messi':
#     print('enter maiami')
# else:
#     print('player is not saved in program')



# in match case you should use | insted of "or"
match player:
    case 'beyranvand' | "karim" | 'saman':
        print('team meli iran')
    case 'messi':
        print('enter maiami')
    case _:
        print('player is not saved in program')
