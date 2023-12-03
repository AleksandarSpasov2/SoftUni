import re

n = int(input())

pattern = r'((@)#+)(\b[A-Z][A-Za-z0-9]+[A-Z]\b)(\1)'

for barcode in range(n):
    barcode_input = input()
    match = re.fullmatch(pattern, barcode_input)

    if not match:
        print(f"Invalid barcode")
    else:
        product_group = ''.join(char for char in barcode_input if char.isdigit())
        if not product_group:
            product_group = '00'
        print(f"Product group: {product_group}")
