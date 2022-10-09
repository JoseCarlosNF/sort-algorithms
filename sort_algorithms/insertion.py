"""
------------------------------- INSERTION SORT -------------------------------
    a. Complexidade:

        | Melhor caso | Caso médio | Pior caso |
        | --          | --         | --        |
        | Ω(n)        | ϴ(n²)      | O(n²)     |

    b. Resumo de funcionamento:

        É caracterizado por sucessivas comparações, entre o valor da interação
        atual, e os demais valores a sua esquerda, até que o valor a sua
        esquerda seja menor.

        Começamos a interação partindo do segundo valor da lista, e comparamos
        com o primeiro, e seguimos dessa forma até o último elemento da lista.

        [5, 3, 2, 1, 4]
         ^--*
        [3, 5, 2, 1, 4] -> [3, 2, 5, 1, 4]
            ^--*            ^--+
        [2, 3, 5, 1, 4] -> [2, 3, 1, 5, 4] -> [2, 1, 3, 5, 4]
               ^--*            ^--+            ^--+
        [1, 2, 3, 5, 4]
                  ^--*
        [1, 2, 3, 4, 5]
"""


from random import sample


class InsertionSort:
    def __init__(self, list: list, print_steps: bool = False):
        self.list = list
        self.print_steps = print_steps

    def order(self):
        size_list = len(self.list)

        for i in range(1, size_list):
            print(self.list) if self.print_steps else ''
            for j in range(i - 1, -1, -1):
                if self.list[i] < self.list[j]:
                    self.list[i], self.list[j] = self.list[j], self.list[i]
                    i = j
        print(self.list) if self.print_steps else ''
        return self.list


if __name__ == '__main__':
    any_numbers = sample(range(100), 10)
    print(f'Lista original: {any_numbers}')
    ordere_list = InsertionSort(any_numbers, print_steps=True).order()
    print(f'Lista ordenada: {ordere_list}')
