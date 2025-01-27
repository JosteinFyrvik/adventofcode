def count(integers, x):
    
    count = 0

    for n in integers:

        if n == x:
            count += 1
    
    return count

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

    similarity_score = 0

    for x in left:
        similarity_score += count(right, x) * x

    return similarity_score

def readintegers(filename):

    with open(filename, 'r') as file:
        file_content = file.read()

    file_items = file_content.split()  
    
    integers = []

    for x in file_items:
        integers.append(int(x))
    return integers
    
print(compute(readintegers('py2024/day1/data.txt')))