a = float(input('Введите длину стороны А '))
b = float(input('Введите длину стороны B '))
c = float(input('Введите сторону длины С '))
if a + b > c and b + c > a and c + a > b:
    print('Это треугольник')
    if a != b and b != c and c != a:
        print('Треугольник разносторонний')
    if a == b or b == c or c == a:
        print('треугольник является равнобедренным')
    if a == b == c:
        print('треугольник является равносторонним')
else:
    print('Это не треугольник')