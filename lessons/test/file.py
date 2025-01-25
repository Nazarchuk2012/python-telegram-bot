# робота з файлами

import random
# варіант 1
#file_name = 'f4.txt'
#file = open(file_name, mode='w')


#   file.close()


# варіант 2
#file_name = 'f2.txt'
#with open(file_name, 'w') as file:
 #   for n in range(0, 100):
 #       file.write(str(random. randint(1, 10000)) + '\n')

# зчитування з файла
#with open('f2.txt', 'r') as file:
    #content = file.read()
   # print(content)


with open('f2.txt', 'r') as file:
    line =file.readline()
    while line:
        print(line)
        # ...   
        line = file.readline()












