def menu(options):
    while True:
        user_choice = input('Choose one: ').strip()
    
        if user_choice in options:
            return user_choice
    
        print(f'Choose a valid option from {options}')    

if __name__ == '__main__':   # __name__ is a variable, but '__main__' is a string!
    choice = menu(['x', 'y', 'z'])
    print(f'You chose {choice}')
    
