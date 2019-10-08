import unittest
import sys
from unittest.mock import patch
from tests_practice.task1 import *

class Test(unittest.TestCase):

    def test_task1_correct_values(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(task_1_arr_intersection(a, b), [1, 2, 3, 5, 8, 13])

    def test_task1_empty_value(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = []
        self.assertEqual(task_1_arr_intersection(a, b), [])

    def test_count_ch(self):
        string = "I am a good developer. I am also a writer"
        expected_result = 5
        self.assertEqual(task_2_count_symbol_in_string(string, "a"), expected_result)

    def test_power3(self):
        for i, j in zip([9, 3, 6, 14], [True, True, False, False]):
            self.assertEqual(task_3_check_if_power_of_three(i), j)

    def test_sum_digits(self):
        for i, j in zip([48, 59, 34, 11, 1111, 897], [3, 5, 7, 2, 4, 6]):
            self.assertEqual(task_4_sum_digits(i), j)

    def test_push_zeros(self):
        expected_result = [2, 3, 4, 6, 7, 10, 0]
        self.assertEqual(task_5_push_zeros([0,2,3,4,6,7,10]), [2, 3, 4, 6, 7, 10, 0])

    def test_is_arith_progression(self):
        test_arr = [5, 7, 9, 11]
        self.assertTrue(task_6_is_arith_progression(test_arr))

    def test_single_number(self):
        test_arr = [5, 3, 4, 6, 3, 4, 5]
        expected_result = 6
        self.assertEqual(task_7_single_number(test_arr), expected_result)

    def test_missing(self):
        test_arr = [1,2,3,4,6,7,8]
        expected_result = 5
        self.assertEqual(task_8_missing(test_arr), expected_result)

    def test_count_not_tuples(self):
        test_arr = [1,2,3,(1,2),3]
        expected_result = 3
        self.assertEqual(task_9_count_not_tuples(test_arr), expected_result)

    def test_reverse_str(self):
        test_str = "Hello World and Coders"
        expected_result = "sredoC dna dlroW olleH"
        self.assertEqual(task_10_reverse_str(test_str), expected_result)

    def test_hours_minutes(self):
        test_num = 76
        expected_result = "1:16"
        self.assertEqual(task_11_hours_minutes(test_num), expected_result)

    def test_largest_word(self):
        for sentence, word in zip(["fun&!! time", "I love dogs"], ["time", "love"]):
            self.assertEqual(task_12_largest_word(sentence), word)

    def test_reverse_sentence(self): #, mock_input, mock_print
        user_input = "My name is Michele"
        expected_result = "Michele is name My"
        with patch('builtins.input', return_value = user_input):
            self.assertEqual(task_13_reverse_sentence(), expected_result)

    def test_fibonacci(self):
        user_input = "7"
        expected_result = [1, 1, 2, 3, 5, 8, 13]
        with patch('builtins.input', return_value = user_input):
            self.assertEqual(task_14_fibonacci(), expected_result)

    def test_even_filter(self):
        test_arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        expected_result = [4, 16, 36, 64, 100]
        self.assertEqual(task_15_even_filter(test_arr), expected_result)

    def test_sum_numbers(self):
        user_input = "4"
        expected_result = 10
        with patch('builtins.input', return_value = user_input):
            self.assertEqual(task_16_sum_numbers(), expected_result)

    def test_factorial(self):
        test_num = 4
        expected_result = 24
        self.assertEqual(task_17_factorial(test_num), expected_result)

    def test_reformat_str(self):
        test_str = "abcd"
        expected_result = "bcdE"
        self.assertEqual(task_18_reformat_str(test_str), expected_result)

    def test_alphabetical_order(self):
        test_str = "hello"
        expected_result = "ehllo"
        self.assertEqual(task_19_alphabetical_order(test_str), expected_result)

    def test_comparing(self):
        for params, expected_result in zip([[1, 5], [5, 1], [3, 3]], [True, False, -1]):
            self.assertEqual(task_20_comparing(params[0], params[1]), expected_result)

if __name__ == "__main__":
    unittest.main()
