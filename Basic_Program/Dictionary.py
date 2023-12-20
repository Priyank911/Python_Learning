#Dictionary = A changeable, unordered collection of unique key:value pairs Fast because they use hashing method, allow us to access a value quickly

# dic={1:"Burger",2:"Frankie",3:"Pizza",4:"Pasta"}
# print(dic)
# print(dic.get('Coldcoffee'))
# print(dic.keys())
# print(dic.values())

# dic_upadate = {1:"Burger",2:"Frankie",3:"Pizza",4:{5:"Pasta"}}
# print(dic_upadate.values())
# print(dic_upadate.keys())
# # If you want to print the value of 5
# value_of_5 = dic_upadate[4][5]
# print(value_of_5)
# print(dic_upadate.items())

# Formkeys method to assign same key value to all...

keys = ['apple', 'banana', 'cherry']
default_value = 0
fruit_dict = dict.fromkeys(keys, default_value)
print(fruit_dict)

# # Example 2: Setting all values to None by default
# keys = ['one', 'two', 'three']

# number_dict = dict.fromkeys(keys)

# print(number_dict)
