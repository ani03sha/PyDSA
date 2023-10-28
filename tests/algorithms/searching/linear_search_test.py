from algorithms.searching.linear_search import linear_search


def test_linear_search_found():
    assert linear_search([4, 2, 7, 1, 9, 5], 7) == 2


def test_linear_search_not_found():
    assert linear_search([4, 2, 7, 1, 9, 5], 3) is None


def test_linear_search_empty_list():
    assert linear_search([], 5) is None


def test_linear_search_single_element_found():
    assert linear_search([9], 9) == 0


def test_linear_search_single_element_not_found():
    assert linear_search([6], 9) is None


def test_linear_search_duplicate_elements():
    assert linear_search([3, 7, 2, 7, 9], 7) == 1


def test_linear_search_large_list():
    assert linear_search(list(range(1000000)), 999999) == 999999


def test_linear_search_negative_numbers():
    assert linear_search([-1, -5, -3, -8, -10], -8) == 3


def test_linear_search_mixed_data_types():
    assert linear_search(['apple', 3, 'banana', True], 'banana') == 2


def test_linear_search_floats():
    assert linear_search([1.5, 3.7, 2.8, 5.2], 2.8) == 2
