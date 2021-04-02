# # thetuple=("apple","banana","cacek")
# # print(len(thetuple))


# # To create a tuple with only one item, 
# # you have to add a comma after the item, 
# # otherwise Python will not recognize it as a tuple.

# # thistuple = ("apple",)
# # print(type(thistuple))

# # #NOT a tuple
# # thistuple = ("apple")
# # print(type(thistuple))

# # update tuple
# x =("apple","banana","cacek")
# y= list(x)
# y[1] ="jambu"
# x = tuple(y)
# print(x)



#---------add item in tuple-------------

thistuple = ("apple", "banana", "cherry","orange")
y=list(thistuple)
# y.append("orange")
y.remove("orange")
thistuple = tuple(y)
print(thistuple)

#-------------del not working with tuple----------------

