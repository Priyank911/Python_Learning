# s='django'
# print(s[0])
# print(s[-1])
# print(s[0:4])
# print(s[1:4])
# print(s[4:])
# print(s[::-1])

# Ist = [3,7,[1,4,'hello']]
# Ist[2][2]='goodbye'
# print(Ist)

# d1 = {'simple_key':'hello'}
# d2 = {'k1':{'k2':'hello'}}
# d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# d4 = {'k1':[{'nest_key':10}]}
# print(d1['simple_key'])
# print(d2['k1']['k2'])
# print(d3['k1'][0]['nest_key'][1][0])
# print(d4['k1'][0]['nest_key'])


# print("<-------Program 1--------->")

# if 1<3:
#     print("First Block..!")
#     if 20<3:
#         print("Second Block..!")


# print("<-------Program 2--------->")

# if 1>4:
#     print("In if")
# elif 1<4:
#     print("In elif")
# else:
#     print("In else")

print("<--------Control Flow-------->")
# Sequence = [1,2,3,4,5]
# for i in Sequence:
#     print(i*i)

# # Program 2
# item = {'sam': 1, 'frank':2}
# print("Print Key:- ")
# print()
# for d in item:
#     print(d)
# print()
# print("Print Value:- ")
# print()
# for k in item.values():
#     print(k)

mypairs = [(1,5),(2,6),(3,7)]
for (tup1,tup2) in mypairs:
    print(tup1)