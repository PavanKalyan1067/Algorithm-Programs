# Python program to display all the prime numbers within an interval
def prime_numbers():
    lower = 1
    upper = 1000

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, 'is prime number')
    for num in range(1001):
        reverse = int(str(num)[::-1])
        # all prime numbers are greater than 1
        if num == reverse:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num, 'is palindrome prime number')
    for num in range(1000):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num, 'is Armstrong prime number')


if __name__ == '__main__':
    prime_numbers()
