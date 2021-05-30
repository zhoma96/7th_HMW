def orders(rows, numbers):
    return '\n'.join(['+' * rows for i in range(numbers // rows)]) + '\n' + '+' * (numbers % rows)


print(orders(4, 30))