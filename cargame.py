user_input = ''
car_start = False
while True:
    user_input = input('>')
    if user_input == 'help':
        print('''
start: to start the car
stop: to stop the car
quit: to quit the game''')
    elif user_input == 'start':
        if car_start:
            print('car already started!')
        else:
            car_start = True
            print('car started')
    elif user_input == 'stop':
        if not car_start:
            print('car already stopped')
        else:
            car_start = False
            print('car stopped')
    elif user_input == 'quit':
        break
    else:
        print('Invalid input')
