# Salau Adeiza round 2 (1)
def PatGen(n):
    x = 1
    while x <= n:
        l = []
        for i in range(n):
            l.append('*')
            print(l)
            x += 1

PatGen(4)
