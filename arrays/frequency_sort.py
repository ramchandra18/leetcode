# Question: Given an string, sort the characters based on their frequency in descending order

"""
ex: Input: "tree"
    Output: "eert"
"""

# hash map based solution

from heapq import heappush, heappop
from collections import Counter

def frequency_sort_map(s):
    count_map = {}

    for elem in s:
        if count_map.keys().__contains__(elem):
            count_map[elem] += 1
        else:
            count_map[elem] = 1
    return ''.join([k*v for k, v in sorted(count_map.items(), key=lambda x: x[1], reverse=True)])


def frequency_sort_heap(s):
    h = []
    count_map = {}

    for elem in s:
        if count_map.keys().__contains__(elem):
            count_map[elem] += 1
        else:
            count_map[elem] = 1
    for k, v in count_map.items():
        heappush(h, (v, k))

    sub_string = ''
    while True:
        try:
            i = heappop(h)
            sub_string = i[0]*i[1] + sub_string
        except IndexError:
            break

    return sub_string


def frequency_sort_collections(s):
    a = Counter(s)

    return ''.join(i[0]*i[1] for i in sorted(a.items(), key=lambda x: x[1], reverse=True))


word = "raaeaedere"

print(frequency_sort_collections(word))
print(frequency_sort_heap(word))
print(frequency_sort_map(word))
