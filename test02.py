file_name='gest_book.txt'

while True:
    name = input('Pleas write your name:')
    with open(file_name,'w') as file_object:
        file_object.write(name+'\n')
    print('Thank you '+ name)
    break