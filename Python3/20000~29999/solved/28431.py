def main():
    sock_numbers = [int(input()) for _ in range(5)]

    sock_count = {}
    for num in sock_numbers:
        sock_count[num] = sock_count.get(num, 0) + 1

    odd_sock_number = None
    for num, count in sock_count.items():
        if count % 2 != 0:
            odd_sock_number = num
            break

    print(odd_sock_number)

if __name__ == "__main__":
    main()
