def sort_insert(A):
    """ сортировка вставками"""
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k] < A[k-1]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
def chise_sort(A):
    """ сортировка выбором """
    for pos in range(0, len(A) - 1):
        for k in range(pos + 1, len(A)):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """ сортировка пузырьком"""
    for bypass in range(1, len(A)):
        for k in range(0, len(A) - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k+1] = A[k + 1], A[k]



def sort_test(sort_algorithm):
    print('Алгоритм:', sort_algorithm.__doc__)
    print('Тест 1:', end='')
    A = [2, 4, 5, 3, 1]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Not Ok')

    print('Тест 2:', end='')
    A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    A_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Not Ok')

if __name__ == "__main__":
    sort_test(sort_insert)
    sort_test(chise_sort)
    sort_test(bubble_sort)