from sort_algorithms.selection import SelectionSort

def test_selection_sort(capsys):
    list = [9, 3, 6, 2, 9, 9, 5, 6, 10, 7]
    SelectionSort(list, print_steps=True).order()
    assert capsys.readouterr().out == (
        '[9, 3, 6, 2, 9, 9, 5, 6, 10, 7]\n'
        '[2, 3, 6, 9, 9, 9, 5, 6, 10, 7]\n'
        '[2, 3, 6, 9, 9, 9, 5, 6, 10, 7]\n'
        '[2, 3, 5, 9, 9, 9, 6, 6, 10, 7]\n'
        '[2, 3, 5, 6, 9, 9, 9, 6, 10, 7]\n'
        '[2, 3, 5, 6, 6, 9, 9, 9, 10, 7]\n'
        '[2, 3, 5, 6, 6, 7, 9, 9, 10, 9]\n'
        '[2, 3, 5, 6, 6, 7, 9, 9, 10, 9]\n'
        '[2, 3, 5, 6, 6, 7, 9, 9, 10, 9]\n'
        '[2, 3, 5, 6, 6, 7, 9, 9, 9, 10]\n'
    )
