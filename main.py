def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factor(num - 1)


if __name__ == '__main__':
    print(factorial(7))
