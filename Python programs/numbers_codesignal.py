def numbers_check(numbers):

    if numbers[0] % 2 == 0:
        return helper(numbers, "even_first",1)
    else:
        return helper(numbers, "odd_first",1)


def helper(numbers, str,i):
    num_len = len(numbers)
    if str == "even_first" and i < num_len:
        for i in (i, num_len-1):
            if numbers[i] % 2 != 0:
                return helper(numbers,"odd_first",i+1)
            else:
                return i
    elif str == "odd_first" and i < num_len:
        for i in (i, num_len-1):
            if numbers[i] % 2 == 0:
                return helper(numbers,"even_first",i+1)
            else:
                return i
    else:
        return -1


d = numbers_check([1,2,3,4,5,6])
print(d)
