def longest(wl):
    wlen = []
    for n in wl:
        wlen.append((len(n),n))
    wlen.sort()
    return wlen[-1][1]
print(longest(["lol","exercises","backend"]))