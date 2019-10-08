import math, re

def task_1_arr_intersection(arr1, arr2):
    return list(set([i for i in max([arr1, arr2], key = len) if i in arr1 and i in arr2]))

def task_2_count_symbol_in_string(string, ch):
    return string.count(ch)

def task_3_check_if_power_of_three(num):
    return True if math.log(num, 3) % 1 == 0 else False

def task_4_sum_digits(num):
    while len(str(num)) > 1:
        num = sum([int(i) for i in str(num)])
    return num

def task_5_push_zeros(arr):
    for i in arr:
        if i == 0:
            arr.remove(0)
            arr.append(0)
    return arr

def task_6_is_arith_progression(arr):
    step = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] == step:
            continue
        else:
            return False
    return True

def task_7_single_number(arr):
    return [i for i in arr if arr.count(i) == 1][0]

def task_8_missing(arr):
    example = list(range(arr[0], arr[len(arr)-1] + 1))
    return next((i for i, j in zip(example, arr) if i != j))

def task_9_count_not_tuples(arr):
    result = 0
    for a in arr:
        if isinstance(a, tuple):
            break
        result += 1
    return result

def task_10_reverse_str(string):
    result = []
    for ch in range(len(string)-1, -1, -1):
        result.append(string[ch])
    return "".join(result)

def task_11_hours_minutes(num):
    return "{}:{}".format(num//60, num%60)

def task_12_largest_word(string):
    return max([re.sub("[^a-zA-Z]", "", word) for word in string.split()])

def task_13_reverse_sentence():
    sentence = input("Enter the sentence: ")
    return " ".join(sentence.split()[::-1])
    # print(" ".join(sentence.split()[::-1]))

def task_14_fibonacci():
    num = int(input("How many numbers of Fibonacci sequence do you want? "))
    arr = []
    for i in range(1, num+1):
        if i in [1, 2]:
            arr.append(1)
            continue
        arr.append(arr[i-2] + arr[i-3])
    return arr

def task_15_even_filter(arr):
    return [i for i in arr if i % 2 == 0]

def task_16_sum_numbers():
    num = int(input("Enter a number: "))
    return sum([i for i in range(1, num+1)])

def task_17_factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def task_18_reformat_str(string):
    result = ""
    for i in string:
        if i == 'z':
            i = 'a'
        else:
            i = chr(ord(i)+1)
        result += i.upper() if i in ["a", "e", "i", "o", "u"] else i
    return result

def task_19_alphabetical_order(string):
    return "".join(sorted(string, key = ord))

def task_20_comparing(num1, num2):
    if num1 == num2:
        return -1
    return True if num2 > num1 else False

if __name__ == "__main__":
    print(task_14_fibonacci())
