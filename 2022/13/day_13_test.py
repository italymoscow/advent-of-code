from unittest import TestCase
from day_13 import *


class Test(TestCase):

    def test_parse_input(self):
        input_strings = read_input("day_13_input_test.txt")
        input_list = parse_input(input_strings)

    def test_find_matching_brackets_1(self):
        input_string = "[1,2,3]"
        actual = find_matching_brackets(input_string)
        expected = {0: 6}
        logging.debug("\nInput: " + input_string
                      + "\nMatching brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_find_matching_brackets_2(self):
        input_string = "[[1],[2,3,4]]"
        actual = find_matching_brackets(input_string)
        expected = {0: 12, 1: 3, 5: 11}
        logging.debug("\nInput: " + input_string
                      + "\nMatching brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_find_matching_brackets_3(self):
        input_string = "[1,[2,[3,[4,[5,6,7]]]],8,9]"
        actual = find_matching_brackets(input_string)
        expected = {0: 26, 3: 21, 6: 20, 9: 19, 12: 18}
        logging.debug("\nInput: " + input_string
                      + "\nMatching brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_find_first_level_brackets_1(self):
        matching_brackets = {0: 6}
        actual = find_first_level_brackets(matching_brackets)
        expected = {}
        logging.debug("\nMatching brackets: " + str(matching_brackets)
                      + "\nFirst level brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_find_first_level_brackets_2(self):
        matching_brackets = {0: 12, 1: 3}
        actual = find_first_level_brackets(matching_brackets)
        expected = {1: 3}
        logging.debug("\nMatching brackets: " + str(matching_brackets)
                      + "\nFirst level brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_find_first_level_brackets_3(self):
        # input_string = "[[1],[2,3,4]]"
        matching_brackets = {0: 12, 1: 3, 5: 11}
        actual = find_first_level_brackets(matching_brackets)
        expected = {1: 3, 5: 11}
        logging.debug("\nMatching brackets: " + str(matching_brackets)
                      + "\nFirst level brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_find_first_level_brackets_4(self):
        # [1,[2,[3,[4,[5,6,7]]]],8,9]
        matching_brackets = {0: 26, 3: 21, 6: 20, 9: 19, 12: 18}
        actual = find_first_level_brackets(matching_brackets)
        expected = {3: 21}
        logging.debug("\nMatching brackets: " + str(matching_brackets)
                      + "\nFirst level brackets: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_1(self):
        input_string = "[1,2,3]"
        actual = parse_string_into_list(input_string)
        expected = list((1, 2, 3))
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_2(self):
        input_string = "[[1],4]"
        actual = parse_string_into_list(input_string)
        expected = [[1], 4]
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_3(self):
        input_string = "[[1],[4,5,6]]"
        actual = parse_string_into_list(input_string)
        expected = list(([1], list((4, 5, 6))))
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_4(self):
        input_string = "[1,2,[3,4],5,6]"
        actual = parse_string_into_list(input_string)
        expected = list((1, 2, list((3, 4)), 5, 6))
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_5(self):
        input_string = "[1,[2,[3,[4,[5,6,7]]]],8,9]"
        actual = parse_string_into_list(input_string)
        expected = [1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_6(self):
        input_string = "[[[]]]"
        actual = parse_string_into_list(input_string)
        expected = [[[]]]
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_7(self):
        input_string = "[[]]"
        actual = parse_string_into_list(input_string)
        expected = [[]]
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_parse_string_into_list_8(self):
        input_string = "[[],[[[]],9,[],1],[1,0]]"
        actual = parse_string_into_list(input_string)
        expected = [[], [[[]], 9, [], 1], [1, 0]]
        logging.debug("\nInput string: " + str(input_string)
                      + "\nList: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_1(self):
        input_list = [[[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'right'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_2(self):
        input_list = [[[[1], [2, 3, 4]], [[1], 4]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'right'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_3(self):
        input_list = [[[[1], [2, 3, 4]], [[1], 4]],
                      [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'right', 2: 'right'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_4(self):
        input_list = [[[9], [8, 7, 6]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'wrong'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_5(self):
        input_list = [[[7, 7, 7, 7], [7, 7, 7]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'wrong'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_6(self):
        input_list = [[[[[]]], [[]]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'wrong'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)

    def test_compare_pairs_in_list_7(self):
        input_list = [[[1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
                       [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]]]
        actual = compare_pairs_in_list(input_list)
        expected = {1: 'wrong'}
        logging.debug("\nInput list: " + str(input_list)
                      + "\nPairs in right order: " + str(actual))
        self.assertEqual(expected, actual)


logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.disable(logging.CRITICAL)
input_strings = read_input("day_13_input_test.txt")
