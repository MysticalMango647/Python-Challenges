'''
Write a function that takes two lists of names and returns a sorted list of unique names from both
 (order by appearance doesn't matter).

Example:
unique_names(["Ava", "Emma", "Olivia"], ["Olivia", "Sophia", "Emma"]) 
should return ["Ava", "Emma", "Olivia", "Sophia"]
'''

def unique_names(names1, names2):
    unquie_name_list = names1 + names2
    unquie_name_list =(set(unquie_name_list))
    return unquie_name_list 

print(unique_names(["Ava", "Emma", "Olivia"], ["Olivia", "Sophia", "Emma"]))  # Output: ['Ava', 'Emma', 'Olivia', 'Sophia']