# DZ 5 - 2


N = 8
x, y = [0] * N, [0] * N


for i in range(N):
    enter = input(f'Введите координаты ферзя {i + 1} через пробел: ')
    x[i], y[i] = map(int, enter.split())

for i in range(N):
    for j in range(i + 1, N):
        if x[i] == x[j] or y[i] == y[j] or \
                abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = False
        else:
            result = True
