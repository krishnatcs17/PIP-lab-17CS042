list1 = input("Enter the elements separated with space: ").split(" ")
list2 = list()
for i in list1:
    if (int(i) % 2) is 0:
        list2.append(i)

print("Original list: ", *list1)
print("List with only even numbers: ", *list2)
