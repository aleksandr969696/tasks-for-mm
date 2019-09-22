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
    times = []
    for k in range(K):
        l1 = [random.randint(0, 2*M) for _ in range(M)]
        l2 = [random.randint(0, 2*M) for _ in range(M)]
        time0 = time.time()
        nmax_of_lists(l1, l2, N=N)
        times.append(round(time.time()-time0, 10))
    print(times)
    return np.average(times)


print(time_count(10, 10000, 5))
#
# print(nmax_of_lists.__doc__)
# l1 = [i for i in range(20) if i%2 == 0]
# l1.append(18)
# l2 = [i for i in range(20) if i%2 != 0]
# l1.append(18)
# print(nmax_of_lists(l1, l2, N = 7, numpy_=True))