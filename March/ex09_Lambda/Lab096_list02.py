my_list = [1 , 2 , 3]

# indexing
print("element at the index 0 -  " , my_list[0])
print("element at the index 1 -  " , my_list[1])
print("element at the index 2 -  " , my_list[2])


#append() - # append object to the end of the list .
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - append a new list
my_list.extend([7 , 8 , 9])
print(my_list)

#insert()
my_list.insert(1 , "kumar")
print(my_list)
print(len(my_list))


my_list.insert(0 , 0)
print(my_list)

my_list.remove("abhi9")
print(my_list)

print("------")
print("------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("kumar")
my_list.remove("kumar")


my_copy_list.sort()

print(my_list)
print(my_copy_list)