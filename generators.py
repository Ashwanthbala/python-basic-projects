import memory_profiler
import random


names = ["John","Jack","Tim","Dave"]

print("Using a Normal iterator")
print('Memory (Before): {}Mb'.format(memory_profiler.memory_usage()))

#Normal iterator
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {"id": i,"name": random.choice(names)}
        result.append(person)
    return result

#generator
def people_generator(num_people):
    for i in range(num_people):
        person = {'id' : i,"name": random.choice(names)}
        yield person


people = people_list(1000000)

print('Memory (After): {}Mb'.format(memory_profiler.memory_usage()))

people1 = people_generator(100000)
print("Using Generator")
print('Memory (After): {}Mb'.format(memory_profiler.memory_usage()))



