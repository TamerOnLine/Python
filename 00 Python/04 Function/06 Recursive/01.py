def info(n):
    if n <= 1:
        return 1
    else:
        return n * info(n - 1)

print(info(365))

