#map function in functional programming
#it is used for mainly reducing the code complexity
my_list = [2,4,6]
def multiply_2(item):
    return item*2
print(list(map(multiply_2,my_list)))
print(my_list)
#even though we have changed the my_list this map function don't disturb the outside world.
# The above map function will call the multiply function on behalf of us, where the we will pass the parameters as the
#function to be called and the iterable
#--------------------------------------------------------------------------------------------------------
#2.Filter function
list_my = [1,2,3]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,list_my)))
print(my_list)
#this is self explanatory where it will filter based on the instruction that we give in the function
#--------------------------------------------------------------------------------------------------------------
#3. zip function
their_list = [1,2,3]
your_list = [4,5,6]

print(list(zip(their_list,your_list)))

#since the output of the function is clear that it will zip the list by first value of one list to another list and second value of first list to another list

#--------------------------------------------------------------------------------------------------------------
#4.reduce function
from functools import reduce

red_list = [1,2,3,4]
def accumulator(acc,item):
    print(acc,item)
    return acc + item
print(reduce(accumulator,red_list,0))