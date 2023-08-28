#!/usr/bin/python3
def subtraction_num(ln):
    sub = 0
    ml = max(ln)

    for n in ln:
        if ml > n:
            sub += n

    return (ml - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listofkey = list(rom_num.keys())
    num = 0
    last_rom = 0
    ln = [0]

    for c in roman_string:
        for r_num in listofkey:
            if r_num == c:
                if rom_num.get(c) <= last_rom:
                    num += subtraction_num(ln)
                    ln = [rom_num.get(c)]
                else:
                    ln.append(rom_num.get(c))

                last_rom = rom_num.get(ch)

    num += subtraction_num(ln)
    return (num)
