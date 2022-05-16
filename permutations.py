# Iterative function to generate all permutations of a string in Python
def permutations(string):
    """

    :param string: string to get permutations
    :return:
    """
    # base case
    if not string:
        return []

    # create a list to store (partial) permutations
    partial = [string[0]]

    # initialize the list with the first character of the string

    # do for every character of the specified string
    for i in range(1, len(string)):

        # consider previously constructed partial permutation one by one

        # iterate backward
        for j in reversed(range(len(partial))):

            # remove the current partial permutation from the list
            curr = partial.pop(j)

            # Insert the next character of the specified string into all
            # possible positions of current partial permutation.
            # Then insert each of these newly constructed strings into the list

            for k in range(len(curr) + 1):
                partial.append(curr[:k] + string[i] + curr[k:])

    print(partial, end='')


# Using Recursion
def get_permutation(string, i=0):
    """

    :param string: string to get permutations
    :param i:
    :return:
    """
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]

        get_permutation(words, i + 1)


def checkig_array_equal():
    arr1 = ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']  # Taking result from recursion
    arr2 = ['cab', 'acb', 'abc', 'cba', 'bca', 'bac']  # Taking result from Iteration
    if len(arr1) == len(arr2):
        print("array is equal")
    else:
        print("array is not equal")


if __name__ == '__main__':
    string = 'abc'
    print("permutations using recursion: ")
    get_permutation(string)  # Using recursion
    print('permutations using Iteration: ')
    permutations(string)  # using Iteration
    print("\nChecking arrays are equal or not:")
    checkig_array_equal()
