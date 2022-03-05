def abbrev_name(name):
    result = ""
    result2 = ""
    space = " "
    i = 0
    while i < len(name):
        if name[i] == space:
            result2 += name[i + 1]
        elif i == 0:
            result += name[i]
        i += 1


    return f'{result.upper()}.{result2.upper()}'


print(abbrev_name("Max Malkhazov"))


def digitize(n):
    reversed = str(n)[::-1]
    result = []
    for n in reversed:
        result += int(n)

    return result

print(digitize(35231))
