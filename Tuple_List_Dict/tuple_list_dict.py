'''
Write a program that accepts  a list of num or str
seperated by commas
generate teh input into a tuple, list and dict
ex:
1,2,3 -> (1,2,3) [1,2,3] {0:1, 1:2, 2:3}
'''

values = input("Enter new items(seperated by commas): ")
new_values = values.split(',')
c_tuples = tuple(new_values)
key = range(0, len(new_values))
dict12 = {}
for i in key:
    dict12[i] = new_values[i]
print("List: ", new_values)
print("Tuples: ", c_tuples)
print("Dict: ", dict)

# alternative way for dict
c_dict = {i: new_values[i] for i in range(0, len(new_values))}
print("New Dict: ", c_dict)

#enumerate method
x = dict(list(enumerate(new_values)))
print("Dict enumerate", x)