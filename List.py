my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = list(range(10, 17))
my_list3 = list(range(1, 100, 10))

print(my_list1)
print(my_list2)
print(my_list3)

print(type(my_list1))

print(my_list1[5])  # This returns the sixth element in the list, the first element is 0.
print(my_list1[-1])  # This returns the last element on the list
print(my_list1[1:4])
print(len(my_list1))
print(max(my_list1))
print(min(my_list1))

# Add an element onto our list
my_list1.append(120) # Append adds an element at the end of the list
print(my_list1)

# Reverse a list
my_list1.reverse()
print(my_list1)

# Add two list together
print(my_list1 + my_list2)

