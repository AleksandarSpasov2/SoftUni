import re


def is_valid_barcode(barcode):
    pattern = r'@#+[A-Z][a-zA-Z0-9]+[A-Z]@#+'
    match = re.fullmatch(pattern, barcode)
    return match is not None


def get_product_group(barcode):
    digits = ''.join(filter(str.isdigit, barcode))
    return digits if digits else '00'


def process_barcodes(n, barcodes):
    for barcode in barcodes:
        if is_valid_barcode(barcode):
            product_group = get_product_group(barcode)
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")


n = int(input())
barcodes = [input().strip() for _ in range(n)]

process_barcodes(n, barcodes)
