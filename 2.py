def galois_multiply(a, b):
    result = 0
    for i in range(8):
        if b & 1:
            result ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x1B
        b >>= 1
    return result & 0xFF

a = int(input("Введіть перший байт (у шістнадцятковому форматі, наприклад, 0x57): "), 16)
b = int(input("Введіть другий байт (у шістнадцятковому форматі, наприклад, 0x83): "), 16)

result = galois_multiply(a, b)

print("Результат множення {} * {} = {}".format(hex(a), hex(b), hex(result)))
