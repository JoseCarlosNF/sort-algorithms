from sort_algorithms.selection import SelectionSort
from random import sample
from time import time

def test_steps_selection_sort(capsys):
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

def test_assintotic_unsorted():
    list = [x for x in sample(range(10000), 10000)]
    start_time = time()
    SelectionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')

def test_assintotic_sorted():
    list = [x for x in range(10000)]
    start_time = time()
    SelectionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')

def test_assintotic_reverse_sorted():
    list = [x for x in range(10000, -1, -1)]
    start_time = time()
    SelectionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')
