def binary_search(list, search, start, end):

    print("function called!")
    mid = start + end // 2
    if mid == 0:
        if list[mid] == search:
            return mid
        else:
            return None

    if mid > len(list) - 1:
        return None

    guess = list[mid]


    if guess == search:
        return mid

    if guess < search:
        return binary_search(list, search, mid, end)

    else:
        return binary_search(list, search, start , mid)



my_list = []

for i in range(100):
    my_list.append(i + 1)

print("your target is at the index:" , binary_search(my_list, 3, 0, len(my_list) - 1))
