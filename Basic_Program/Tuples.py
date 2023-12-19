# My_tuples=(1,2,3,4.5,(5,6,8))
# print(My_tuples)

# Method:- 1

# Existing tuple
original_tuple = (1, 2, 3, 4)
# Element to append
new_element = 5
# Creating a new tuple by concatenating the original tuple and the new element as a single-element tuple
new_tuple = original_tuple + (new_element,)
print(new_tuple)

# Method:- 2

# # Existing tuple
# original_tuple = (1, 2, 3, 4)
# # Element to append
# new_element = 5
# # Convert the tuple to a list
# tuple_list = list(original_tuple)
# # Append the new element to the list
# tuple_list.append(new_element)
# # Convert the list back to a tuple
# new_tuple = tuple(tuple_list)
# print(new_tuple)
