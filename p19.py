def pythagorean_triplets(N):
    triplets = []
    for a in range(1, N+1):
        for b in range(a, N+1):
            c_square = a**2 + b**2
            c = int(c_square ** 0.5)
            if c <= N and c_square == c**2:
                triplets.append((a, b, c))
    return triplets

# Example usage:
N = 340
result = pythagorean_triplets(N)
print("Pythagorean Triplets with sides up to", N, ":")
print(result)
