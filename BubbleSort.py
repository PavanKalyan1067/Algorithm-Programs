# Bubble sort in Python

def bubble_sort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


if __name__ == '__main__':
    array = [-2, 45, 0, 11, -9]
    bubble_sort(array)
    print('Sorted Array in Ascending Order:')
    print(array)