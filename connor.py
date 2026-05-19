count = {'vowels':0, 'digits':0, 'others':0}
word = input('Enter a string')

for one_char in word:
    if one_char in 'aeiou':
        count['vowels'] += 1
        print(f'counts = {count}')
    elif one_char.isdigit():
        count['digits'] += 1
        print(f'counts = {count}')
    else:
        count['others'] += 1
