file_name = '喜欢编程的原因.txt'

xunhuan=True

while xunhuan:
    ansower = input('你喜欢编程的原因是什么？')
    with open(file_name,'a') as file_object:
        file_object.write(ansower+'\n')
    if ansower == 'q':
        break


        