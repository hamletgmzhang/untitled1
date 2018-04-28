
file_name1='cats.txt'
file_name2 = 'dogs.txt'

with open(file_name1,'w') as file_obj1:
    file_obj1.write('kitty，mini，cici')
    '''
with open(file_name2,'w') as file_obj2:
    file_obj2.write('jason,jakcy,keith')
    '''
try:
    with open(file_name1) as file_obj3:
        contents1 = file_obj3.read()
        print(contents1)
    with open(file_name2) as file_obj4:
        contents2 = file_obj4.read()
        print(contents2)
except FileNotFoundError:
    pass
