def mul02(byte):
    result = byte << 1
    if result & 0x100:
        result ^= 0x1B
    return result & 0xFF

def mul03(byte):
    return mul02(byte) ^ byte

# Тестування функцій на прикладах, наданих у завданні
d4 = 0xD4
bf = 0xBF

# Результати множення
result_d4_mul02 = mul02(d4)
result_bf_mul03 = mul03(bf)

# Виведення результатів у шістнадцятковому форматі
print("D4 * 02 =", hex(result_d4_mul02))
print("BF * 03 =", hex(result_bf_mul03))
