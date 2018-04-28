
print('以下当输入q时，退出程序！')
try:

    while True:

        first_number = input('请输入第一个数字：')
        if first_number == 'q':
            break

        second_number = input('请输入第二个数字：')
        if first_number == 'q':
            break
        '''
        print('你输入的第一个数字是：' + first_number)
        print('你输入的第二个数字是：' + second_number)
        '''
        number = int(first_number + second_number)
        print(number )

except ValueError:
    print('请输入数字类型的！')




