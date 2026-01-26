'''
Write a function that takes in a nested list and merges it to one list
ex:

'''
nl = [[[[[1]]]]]

#long way
for a in nl:
    for b in a:
        for c in b:
            for d in c:
                for e in d:
                    print (e)

nested_list = [[1,2,3,4],['a','b','c'],[7,8,9]]
#smart way
def flatlist(nl):
    nested_list = []
    for sublist in nl:
        #print(sublist)
        for data in sublist:
            nested_list.append(data)
            #print (data)

    print(nested_list)
    return nested_list


flatlist(nested_list)

#new way with iter tools
nested_list = [[1,2,3,4],['a','b','c'],[7,8,9]]

import itertools
def flatlist_iter(nl):
    iter_unpack = list(itertools.chain(*nl))
    print(iter_unpack)
    return

flatlist_iter(nested_list)

#Lambda Function of iterating
from functools import reduce
nested_list = [[1,2,3,4],['a','b','c'],[7,8,9]]

print(reduce(lambda a, b: a + b, nested_list))

#monoids
print("monoidts")
nested_list = [[1,2,3,4],['a','b','c'],[7,8,9]]
print(sum(nested_list, []))