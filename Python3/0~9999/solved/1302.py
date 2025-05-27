from collections import Counter

n = int(input())

books = [input() for _ in range(n)]

book_counts = Counter(books)

max_count = max(book_counts.values())

most_sold_book = min(
    [book for book, count in book_counts.items() if count == max_count]
)

print(most_sold_book)