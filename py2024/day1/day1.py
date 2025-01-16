def compute(integers):
    left = []
    right = []

    # left = integers[0::2]
    # right = integers[1::2]
    for index, x in enumerate(integers):
        if index % 2 == 0:
            left.append(x)
        else:
            right.append(x)
    
    left.sort()
    right.sort()

    difference = 0
#    for num in range(0, len(left)):
#        n1 = left[num]
#        n2 = right[num]
    for n1, n2 in zip(left, right):
        difference = difference + abs(n1 - n2)
    
    return difference

print(compute([3, 4, 4, 3, 2, 5, 1, 3, 3, 9, 3, 3]))
