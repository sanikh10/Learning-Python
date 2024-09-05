# str1 = 'Md Rabius sani'
#
# print(str1.title())
# print(str1.capitalize())
# print(str1.upper())
# print(str1.lower())
# print(str1.casefold())
# print(str1.swapcase())
from idlelib.squeezer import count_lines_with_wrapping
from queue import PriorityQueue
#
# data = 'python is the most, favourite \n language i have, learned, isn\'t it?'
# subsstring = 'is'
# substring2 = 'i'
#
# print(data.splitlines(True))
# print(data.splitlines(False))
# print(data.split(',', 5))

# str1 = ' Hello World! '
# str2 = '---Hello World!------'
#
# print(str2.strip('-'))
# print(str2.lstrip('-'))
# print(str2.rstrip('-'))


name = 'sani'

print(name.center(20, '*'))
print(name.ljust(20, '*'))
print(name.rjust(20, '*'))



myList = ['my','name','is','sani']

mylist_join = '\t'.join(myList)

print(mylist_join)

print(myList)
