chemicals = set()
n = int(input())

for _ in range(n):
    chemical_compounds = input().split()
    for element in chemical_compounds:
        chemicals.add(element)

print(*chemicals, sep='\n')
