from sort_algorithms.insertion import InsertionSort
from random import sample
from time import time


def test_steps_insertion_sort(capsys):
    list = [7, 5, 1, 8, 3]
    InsertionSort(list, print_steps=True).order()
    assert capsys.readouterr().out == (
        '[7, 5, 1, 8, 3]\n'
        '[5, 7, 1, 8, 3]\n'
        '[1, 5, 7, 8, 3]\n'
        '[1, 5, 7, 8, 3]\n'
        '[1, 3, 5, 7, 8]\n'
    )


def test_assintotic_unsorted():
    list = [x for x in sample(range(10000), 10000)]
    start_time = time()
    InsertionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')


def test_assintotic_sorted():
    list = [x for x in range(10000)]
    start_time = time()
    InsertionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')


def test_assintotic_reverse_sorted():
    list = [x for x in range(10000, -1, -1)]
    start_time = time()
    InsertionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')

def test_repeated_list():
    list = [1 for _ in range(1000)]
    start_time = time()
    InsertionSort(list).order()
    print(f'Tempo de execução: {time() - start_time}')
