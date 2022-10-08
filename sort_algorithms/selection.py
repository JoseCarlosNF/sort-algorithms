"""
-------------------------------- SELECTION SORT -------------------------------
    a. Complexidade:

        | Melhor caso | Caso médio | Pior caso |
        | --          | --         | --        |
        | Ω(n²)       | ϴ(n²)      | O(n²)     |

    b. Resumo de aplicação:

        Itera sobre a lista sempre buscando pelo menor elemento, e move-o para
        a primeira posição. Após mover para a primeira posição, descarta essa
        posição, e analisa apenas o restante da lista.

        1a interação: [7, 5, 1, 8, 3]
                       ^-----+
        2a interação: [1, 5, 7, 8, 3]
                          ^--------+
        3a interação: [1, 3, 7, 8, 5]
                             ^-----+
        4a interação: [1, 3, 5, 8, 7]
                                ^--+
        5a interação: [1, 3, 5, 7, 8]
"""

from random import randint
from pprint import pprint


class SelectionSort:
    def __init__(self, list: list, print_steps: bool = False):
        self.list = list
        self.print_steps = print_steps

    def order(self):
        size_list = len(self.list)

        # Itera sobre a patir de qual posição deve ser iniciada a busca pelo
        # menor elemento.
        for i in range(size_list):

            # identifica que o menor elemento será o primeiro item da lista,
            # sempre que a lista for diminuida.
            min_index = i

            # imprime o estado da lista na iteração atual, caso o atributo
            # print_steps estaja definido como verdadeiro.
            print(self.list) if self.print_steps else ''

            # busca pelo menor elemento da lista que está sendo analisada.
            # Importante ressaltar que a análise acontece sobre a mesma lista
            # inicial, mas a partir de um index definido pelo laço anterior.
            for j in range(i+1, size_list):

                # compara o valor atual da iteração, com o menor valor
                # identificado na iteração.
                if self.list[j] < self.list[min_index]:
                    min_index = j

            # coloca o menor valor na primeira posição do vetor que esta sendo
            # avaliado.
            self.list[i], self.list[min_index] = (
                self.list[min_index],
                self.list[i],
            )

        # é de suma importância entender que cada iteração gera
        # resultados particulares para o menor elemento da lista. E isso
        # acontece devido a diminuição do intervalo de análise da lista.
        return self.list


if __name__ == '__main__':
    qdt_item_list = 10
    any_numbers = [randint(1, 10) for _ in range(qdt_item_list)]
    pprint(f'Lista original: {any_numbers}')

    ordered_list = SelectionSort(any_numbers, print_steps=True).order()
    pprint(f'Lista ordenada: {ordered_list}')
