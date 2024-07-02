import random


def split(numbers):
    # Initialize pivot & lists
    pivot = numbers[0]
    left = []
    right = []

    # Iterate through list starting from the second element
    for n in numbers[1:]:
        if n <= pivot:
            left.append(n)
        else:
            right.append(n)
    pivotList = []
    pivotList.append(pivot)
    numbers = left + pivotList + right
    #################
    # Do not delete return statement
    return numbers


def main():
    numbers = [3, 2, 0, 5, 4]
    # print (id(numbers))
    numbers = split(numbers)
    # print (id(numbers))
    print(numbers)

    numbers = [random.randint(0, 20) for i in range(10)]
    print(numbers)
    numbers = split(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
