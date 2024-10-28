def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)


def main():
    n = int(input("Номер числа фібоначі: "))
    print(f"Число фібоначі з номером {n}: {fibo(n)}")


if __name__ == "__main__":
    main()
