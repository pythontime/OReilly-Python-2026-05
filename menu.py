def menu(options):
    while True:
        user_choice = input('Choose one: ').strip()
    
        if user_choice in options:
            return user_choice
    
        print(f'Choose a valid option from {options}')    

if __name__ ==         
