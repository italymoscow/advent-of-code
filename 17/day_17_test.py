from unittest import TestCase
from day_17 import *


class Test(TestCase):

    def test_move_stone_horizontally_right_1(self):
        rocks = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        rock = rocks[1]
        rock_starting_pos = set_starting_pos(rock, bottom)
        bottom[4] = [[4, 4]]
        if not rock.get_pos_cur():
            rock.set_pos_cur(copy.deepcopy(rock.get_pos_init()))
        move_rock_horizontally(rock, ">", bottom)
        actual = rock.get_pos_cur()
        expected = [[3, 4], [2, 5], [3, 5], [4, 5], [3, 6]]
        self.assertEqual(expected, actual)

    def test_move_stone_horizontally_right_1_return(self):
        rocks = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        rock = rocks[1]
        rock_starting_pos = set_starting_pos(rock, bottom)
        bottom[4] = [[5, 4]]
        if not rock.get_pos_cur():
            rock.set_pos_cur(copy.deepcopy(rock.get_pos_init()))
        move_rock_horizontally(rock, ">", bottom)
        actual = rock.get_pos_cur()
        expected = [[4, 4], [3, 5], [4, 5], [5, 5], [4, 6]]
        self.assertEqual(expected, actual)

    def test_move_rock_down_1(self):
        rocks = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        rock = rocks[1]
        set_starting_pos(rock, bottom)
        bottom[4] = [[3, 3]]
        actual = move_rock_down(rock, bottom)
        expected = True
        self.assertEqual(expected, actual)

    def test_update_bottom(self):
        rocks = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        rock = rocks[1]
        set_starting_pos(rock, bottom)
        bottom[3] = [[3, 3]]
        update_bottom(rock, bottom)
        print(bottom)


    def test_set_init_stone_pos_0(self):
        rocks = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        actual = set_starting_pos(rocks[0], 1, bottom)
        expected = [[2, 4], [3, 4], [4, 4], [5, 4]]
        self.assertEqual(expected, actual)

    def test_set_init_stone_pos_2(self):
        stones_init = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        actual = set_starting_pos(stones_init, 2, bottom)
        expected = [[3, 4]], [[2, 5], [3, 5], [4, 5]], [[3, 6]]
        self.assertEqual(expected, actual)

    def test_get_rock_min_max_x_0(self):
        stone_pos = [[2, 4], [3, 4], [4, 4], [5, 4]]
        actual = get_rock_min_max_x(stone_pos)
        logging.debug("Actual: " + str(actual))
        expected = (2, 5)
        self.assertEqual(expected, actual)

    def test_get_rock_min_max_y_0(self):
        stone_pos = [[2, 4], [3, 4], [4, 4], [5, 4]]
        actual = get_rock_min_max_y(stone_pos)
        logging.debug("Actual: " + str(actual))
        expected = (4, 4)
        self.assertEqual(expected, actual)

    def test_get_rock_min_max_y_1(self):
        rock_pos = [[3, 4], [2, 5], [3, 5], [4, 5], [3, 6]]
        actual = get_rock_min_max_y(rock_pos)
        logging.debug("Actual: " + str(actual))
        expected = (4, 6)
        self.assertEqual(expected, actual)

    def test_define_stone_obj(self):
        rocks = initialize_rocks()

    def test_rock_0_intersects_with_bottom(self):
        rocks = initialize_rocks()
        rock = rocks[0]
        if not rock.get_pos_cur():
            rock.set_pos_cur(copy.deepcopy(rock.get_pos_init()))
        bottom = {0: [[i, 0] for i in range(7)]}
        actual = rock_intersects_with_bottom(rock, bottom)
        expected = True
        self.assertEqual(expected, actual)

    def test_rock_1_intersects_with_bottom(self):
        rocks = initialize_rocks()
        bottom = {0: [[i, 0] for i in range(7)]}
        rock = rocks[1]
        rock_starting_pos = set_starting_pos(rock, bottom)
        bottom[4] = [[i, 4] for i in range(7)]
        if not rock.get_pos_cur():
            rock.set_pos_cur(copy.deepcopy(rock.get_pos_init()))
        actual = rock_intersects_with_bottom(rock, bottom)
        expected = True
        self.assertEqual(expected, actual)

    def test_part_1(self):
        part_1()


logging.basicConfig(level=logging.DEBUG, format="%(message)s")
# logging.disable(logging.CRITICAL)
input_str = read_input("day_17_input_test.txt")
