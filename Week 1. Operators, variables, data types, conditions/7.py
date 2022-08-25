```
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
```

a = float(input())
b = float(input())
operation = input()

if operation == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif operation == 'pow':
    if b == 0:
        print(1)
    else:
        print(a ** b)
elif operation == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)
elif operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a/b)
elif operation == '*':
    print(a * b)

