def star_pattern(n):
    for i in range(1, 2 * n):
        for j in range(1, 2 * n):
            if j == i or j == 2 * n - i or i == n or j == n:
                print("*", end=" ")
            else:
                print("*", end= " ")
        print()


n = int(input('Please enter the value of n (star size): '))
star_pattern(n)