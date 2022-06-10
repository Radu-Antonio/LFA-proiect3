def prod_cart(x, y, Gramatica):
    return Gramatica in [i + j for i in x.split(',') for j in y.split(',')]

def CYK(w, Gramatica, S):
    if w == '#':
        return '#' in Gramatica[S]
    n = len(w)
    dp = [[''] * n for _ in range(n)]

    for i in range(n):
        for stanga in Gramatica.keys():
            for dreapta in Gramatica[stanga]:
                if w[i] == dreapta:
                    dp[i][i] = stanga if not dp[i][i] else dp[i][i] + ',' + stanga

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for stanga in Gramatica.keys():
                    for dreapta in Gramatica[stanga]:
                        if len(dreapta) == 2 and prod_cart(dp[i][k], dp[k + 1][j], dreapta) and not stanga in dp[i][j]:
                            dp[i][j] = stanga if not dp[i][j] else dp[i][j] + ',' + stanga
    return S in dp[0][n - 1]

f = open("input.txt")
Gramatica = {}
S = f.readline().strip()

for linie in f:
    stanga, dreapta = linie.split('->')
    stanga = stanga.strip()
    if stanga in Gramatica:
        Gramatica[stanga].extend(x.strip() for x in dreapta.split('|'))
    else:
        Gramatica[stanga] = [x.strip() for x in dreapta.split('|')]

w = input("w = ")
print("apartine gramaticii" if CYK(w, Gramatica, S) else "nu apartine gramaticii")