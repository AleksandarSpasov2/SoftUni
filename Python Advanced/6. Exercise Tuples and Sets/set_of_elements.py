n, m = input().split()
n = int(n)
m = int(m)

n_set = set()
m_set = set()

for _ in range(n + m):
    number = input()
    n -= 1
    if n > 0:
        n_set.add(number)
    else:
        m_set.add(number)


common_elements = n_set.intersection(m_set)

for element in common_elements:
    print(element)
