while True:
    n = int(input())
    if n == 0:
        break

    words = []
    for _ in range(n):
        word = input().strip()
        words.append(word)

    ws = sorted(words, key=lambda x: x.lower())

    print(ws[0])