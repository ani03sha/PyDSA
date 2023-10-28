from algorithms.searching.binary_search import binary_search


def test_binary_search_found_at_beginning():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0


def test_binary_search_found_at_end():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4


def test_binary_search_found_in_middle():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2


def test_binary_search_not_found_lower():
    assert binary_search([1, 2, 3, 4, 5], 0) is None


def test_binary_search_not_found_higher():
    assert binary_search([1, 2, 3, 4, 5], 6) is None


def test_binary_search_not_found_in_empty_list():
    assert binary_search([], 42) is None


def test_binary_search_found_in_single_element_list():
    assert binary_search([42], 42) == 0


def test_binary_search_found_in_duplicate_elements():
    assert binary_search([1, 2, 2, 3, 4, 4, 5], 2) == 1


def test_binary_search_found_in_large_sorted_list():
    assert binary_search(list(range(1, 1001)), 750) == 749


def test_binary_search_found_with_float_numbers():
    assert binary_search([1.1, 2.2, 3.3, 4.4, 5.5], 3.3) == 2
