from sprint_planning_helper import *

def test_collecting_data_from_csv():
    total = collecting_data_from_csv('test.csv')
    assert total[0] == [0, 1, 2, 3, 4, 5]
    assert total[1] == {0: 3, 1: 2, 2: 8, 3: 5, 4: 2, 5: 2}
    assert total[2] == {0: 5, 1: 3, 2: 2, 3: 9, 4: 1, 5: 3}

def test_initialize_result_array():
    total = initialize_result_array([0, 1, 2, 3, 4, 5], 13)
    assert total == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def test_knapsack():
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    data_from_csv = ([0, 1, 2, 3, 4, 5], {0: 3, 1: 2, 2: 8, 3: 5, 4: 2, 5: 2}, {0: 5, 1: 3, 2: 2, 3: 9, 4: 1, 5: 3})

    total = knapsack(array,data_from_csv, 13)
    assert total == [5, 3, 1, 0]

def test_conv_list_to_string():
    total = conv_list_to_string([5, 3, 1, 0])
    assert total == '0, 1, 3, 5'

if __name__ == '__main__':
    test_collecting_data_from_csv()
    test_initialize_result_array()
    test_knapsack()
    test_conv_list_to_string()