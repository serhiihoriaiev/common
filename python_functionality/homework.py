from typing import List, Dict, Union, Generator
import sympy

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for _dict in data:
        if "name" in _dict.keys():
            _dict["name"] = _dict["name"].capitalize()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for _dict in data:
        for rkey in redundant_keys:
            if rkey in _dict.keys():
                del _dict[rkey]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    result = []
    for _dict in data:
        if value in _dict.values():
            result.append(_dict)
    return result


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data) if len(data) > 0 else None


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the shortest string
    """
    if len(data) > 0:
        sh = data[0]
        for word in data:
            if len(str(word)) < len(sh):
                sh = str(word)
        return sh 
    else:
        return None   


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    if len(data) > 0:
        mini = data[0]
        for _dict in data:
            if key in _dict.keys():
                if _dict[key] < mini[key]:
                    mini = _dict
        return mini


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    arr = (a for a in data)
    res_arr = []
    for a in arr:
        if len(a) > 0:
            res_arr.append(max(a))
    return max(res_arr)


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data) if len(data) > 0 else 0


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    result = 0
    for ch in text:
        result += ord(ch)
    return result

def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    return (x for x in range(201) if sympy.isprime(x))
        
