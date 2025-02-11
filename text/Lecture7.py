def end(n, d):
    while True:
        last, n = n % 10, n // 10
        print(last)
        if last == d:
            return None
