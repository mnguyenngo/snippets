def permutations(n, k):
    return math.factorial(n)/math.factorial(n-k)

def combinations(n, k):
    return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))
