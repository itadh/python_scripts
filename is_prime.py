#!/usr/bin/python3
#user_input = int(input('Bitte geben Sie eine Zahl ein: '))

test_numbers = [-4, 0, 1, 2, 3, 4, 9, 13, 99991]
for user_input in test_numbers:
    if user_input <= 0:
        print(f'Für {user_input} lässt sich keine Aussage treffen.')
        continue
#        exit()

    is_prime = False
    counter = 0
    stop_number = int(user_input ** 0.5) + 1
    for number in range(2, stop_number):
        counter += 1
        intermediate_result = user_input % number
        if intermediate_result == 0:
            print(f'Nein, die Zahl {user_input} ist keine Primzahl, sie lässt sich durch {number} teilen.')
            is_prime = False
            break
        else:
            is_prime = True
    
    if is_prime is True or user_input < 4:
        print(f'Ja, die Zahl {user_input} ist eine Primzahl.')
    

