class ValueTooLow(Exception):
    pass


amount_to_send = float(input())

if 0 <= amount_to_send < 1:
    raise ValueTooLow('Value is too low')