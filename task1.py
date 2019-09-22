import numpy as np
import random
import time


def nmax_of_lists(*lists, N=1):
    """
    Function takes lists and return N max values of them
    :param lists:
    :param N:
    :return:
    """
    union_list = []
    for l in lists:
        union_list.extend(l)
    union_set = set(union_list)
    union_list = list(union_set)
    union_list.sort(reverse=True)
    return union_list[:N]


def time_count(K, M, N):
    """
    Function takes three int params: K, M, N. K times calls function nmax_of_lists
    with two random 2M length lists and N, then it count time of each call and return its average.

    :param K:
    :param M:
    :param N:
    :return:
    """
    times = []
    for k in range(K):
        l1 = [random.randint(0, 2*M) for _ in range(M)]
        l2 = [random.randint(0, 2*M) for _ in range(M)]
        time0 = time.time()
        nmax_of_lists(l1, l2, N=N)
        times.append(time.time()-time0)
    return np.average(times)


def count_of_unique(l):
    return len(set(l))


def count_of_unique2(l):
    a = set()
    count=0
    for i in l:
        if i not in a:
            a.add(i)
            count += 1
    return count


def count_of_unique3(l):
    return len(np.unique(l))


m_and_n = dict()

m_and_n[1] = (1, 2, 5)
m_and_n[10] = (2, 5, 10)
m_and_n[1000] = (5, 50, 100)
m_and_n[1000000] = (5, 100, 1000)

with open('results_ЕфимовАА.txt', 'w') as f:
    for M, N in m_and_n.items():
        for n in N:
            f.write(f'N = {n}, M = {M}, time = {round(time_count(10, M, n),3)}s\n')