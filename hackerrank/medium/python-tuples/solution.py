if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    x = 0x345678
    mult = 1000003
    length = len(integer_list)

    for item in integer_list:
        x = (x ^ item) * mult
        length -= 1
        mult += 82520 + length + length

    x += 97531

    x &= (1 << 64) - 1

    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    print(x)
