def readintegers(filename):

    with open(filename, 'r') as file:
        file_content = file.read()

    file_items = file_content.split()  
    
    integers = []

    for x in file_items:
        integers.append(int(x))
    return integers
    




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

# print(readintegers('py2024/day1/sample.txt'))
print(compute(readintegers('py2024/day1/data.txt')))
# "https://adventofcode.com/2024/day/1/input"