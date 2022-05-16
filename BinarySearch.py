def binary_search(arr, x):
    """

    :param arr: passing array of words
    :param x: finding particular word from array
    :return:
    """
    l = 0
    r = len(arr)
    while l <= r:
        m = l + ((r - l) // 2)
        res = (x == arr[m])
        # Check if x is present at mid
        if res == 0:
            return m - 1
        # If x greater, ignore left half
        if res > 0:
            l = m + 1
        # If x s smaller, ignore right half
        else:
            r = m - 1
    return -1


if __name__ == '__main__':
    arr = ["BridgeLabzs", 'Job', 'Guarantee', 'Program']
    x = 'Job'
    result = binary_search(arr, x)
    if result == -1:
        print('Element is present')
    else:
        print('Element is not present')
