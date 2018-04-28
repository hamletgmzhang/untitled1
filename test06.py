
try:
    first_number = input('请输入第一个数字：')

    second_number = input('请输入第二个数字：')
    '''
    print('你输入的第一个数字是：' + first_number)
    print('你输入的第二个数字是：' + second_number)
    '''
    print('相加的结果是：' + int(first_number + second_number))

except ValueError:
    print('请输入数字类型的！')


