
file_name = 'Alice in wonderland.txt'

with open(file_name) as file_obj1:
    names = file_obj1.read()
    words = names.split()
    num_words = len(words)
    print('The file '+file_name+' has about '+ str(num_words)+' words.')
    print('出现the这个单词的次数'+str(names.lower().count('the')))