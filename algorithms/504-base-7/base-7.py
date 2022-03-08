def convert_to_base7(num: int) -> str:
    if num == 0:
        return '0'
    negative = num < 0
    num = abs(num)
    digits = []
    while num:
        digits.append(str(num % 7))
        num //= 7
    if negative:
        digits.append('-')
    return ''.join(reversed(digits))
