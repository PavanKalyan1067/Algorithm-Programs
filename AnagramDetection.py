
def anagram():
    """

    :return:
    """
    string1 = "abcd"
    string2 = "dbca"

    # convert both the strings into lowercase using this if the strings are uppercase
    # str1 = str1.lower()
    # str2 = str2.lower()

    # check if length is same
    if len(string1) == len(string2):

        # sort the strings
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)

        # if sorted char arrays are same
        if sorted_string1 == sorted_string2:
            print(string1 + " and " + string2 + " are anagram.")
        else:
            print(string1 + " and " + string2 + " are not anagram.")

    else:
        print(string1 + " and " + string2 + " are not anagram.")


if __name__ == '__main__':
    anagram()
