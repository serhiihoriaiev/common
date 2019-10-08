import math, re

def task_1_arr_intersection(arr1, arr2):
    '''
    Take two lists and write a program that returns a list that contains
    only the elements that are common between the lists (without duplicates).
    '''
    return list(set([i for i in max([arr1, arr2], key = len) if i in arr1 and i in arr2]))

def task_2_count_symbol_in_string(string, ch):
    '''
    Return the number of times that the letter “a” appears anywhere in the given string
    '''
    return string.count(ch)

def task_3_check_if_power_of_three(num):
    '''
    Write a Python program to check if a given positive integer is a power of three
    '''
    return True if math.log(num, 3) % 1 == 0 else False

def task_4_sum_digits(num):
    '''
    Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit
    '''
    while len(str(num)) > 1:
        num = sum([int(i) for i in str(num)])
    return num

def task_5_push_zeros(arr):
    '''
    Write a Python program to push all zeros to the end of a list.
    '''
    for i in arr:
        if i == 0:
            arr.remove(0)
            arr.append(0)
    return arr

def task_6_is_arith_progression(arr):
    '''
    Write a Python program to check a sequence of numbers is an arithmetic progression or not
    '''
    step = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] == step:
            continue
        else:
            return False
    return True

def task_7_single_number(arr):
    '''
    Write a Python program to find the number in a list that doesn't occur twice.
    '''
    return [i for i in arr if arr.count(i) == 1][0]

def task_8_missing(arr):
    '''
    Write a Python program to find a missing number from a list.
    '''
    example = list(range(arr[0], arr[len(arr)-1] + 1))
    return next((i for i, j in zip(example, arr) if i != j))

def task_9_count_not_tuples(arr):
    '''
    Write a Python program to count the elements in a list until an element is a tuple.
    '''
    result = 0
    for a in arr:
        if isinstance(a, tuple):
            break
        result += 1
    return result

def task_10_reverse_str(string):
    '''
    Write a program that will take the str parameter being passed and return the string in reversed order.
    '''
    result = []
    for ch in range(len(string)-1, -1, -1):
        result.append(string[ch])
    return "".join(result)

def task_11_hours_minutes(num):
    '''
    Write a program that will take the num parameter being passed and return the number of hours and minutes the parameter converts to
    '''
    return "{}:{}".format(num//60, num%60)

def task_12_largest_word(string):
    '''
    Write a program that will take the parameter being passed and return the largest word in the string
    '''
    return max([re.sub("[^a-zA-Z]", "", word) for word in string.split()])

def task_13_reverse_sentence():
    '''
    Write a program that asks the user for a long string containing multiple words.
    Return the same string, except with the words in backwards order.
    '''
    sentence = input("Enter the sentence: ")
    return " ".join(sentence.split()[::-1])

def task_14_fibonacci():
    '''
    Write a program that asks the user how many Fibonnaci numbers to generate and then generates them
    '''
    num = int(input("How many numbers of Fibonacci sequence do you want? "))
    arr = []
    for i in range(1, num+1):
        if i in [1, 2]:
            arr.append(1)
            continue
        arr.append(arr[i-2] + arr[i-3])
    return arr

def task_15_even_filter(arr):
    '''
    Write one line of Python that takes list and makes a new list that has only the even elements of this list in it
    '''
    return [i for i in arr if i % 2 == 0]

def task_16_sum_numbers():
    '''
    Write a program that will add up all the numbers from 1 to input number
    '''
    num = int(input("Enter a number: "))
    return sum([i for i in range(1, num+1)])

def task_17_factorial(num):
    '''
    Write a program that will take the parameter being passed and return the factorial of it
    '''
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def task_18_reformat_str(string):
    '''
    Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
    '''
    result = ""
    for i in string:
        if i == 'z':
            i = 'a'
        else:
            i = chr(ord(i)+1)
        result += i.upper() if i in ["a", "e", "i", "o", "u"] else i
    return result

def task_19_alphabetical_order(string):
    '''
    Write a program that will take the str string parameter being passed and return the string with
    the letters in alphabetical order (ie. hello becomes ehllo)
    '''
    return "".join(sorted(string, key = ord))

def task_20_comparing(num1, num2):
    '''
    Write a program that will take both parameters being passed and return the true if num2 is greater than num1,
    otherwise return the false. If the parameter values are equal to each other then return the string -1
    '''
    if num1 == num2:
        return -1
    return True if num2 > num1 else False

if __name__ == "__main__":
    print(task_14_fibonacci())
