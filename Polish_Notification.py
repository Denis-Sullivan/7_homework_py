def user_input():
    user = input('\nВведите знак операции и два числа через пробел: \n(например: + 2 2) \n')
    return user


def calculation(f):
    function_length = len(f.split())
    sign = f.split()[0]

    if function_length != 3:
        print('неверные данные, прочитайте условия ввода')
        print(len(f.split()))
        main()

    try:
        first_num = int(f.split()[1])
        second_num = int(f.split()[2])

        assert int(f.split()[1]) >= 0 and int(f.split()[2]) >= 0, 'одно из значений меньше нуля'

        assert sign in ['+', '-', '/', '*'], 'не верный знак операции'

        if sign == '+':
            return first_num + second_num
        elif sign == '-':
            return first_num - second_num
        elif sign == '/':
            return round((first_num / second_num), 2)
        elif sign == '*':
            return first_num * second_num
        elif function_length != 3:
            return 'введено не верное кол-во операндов'
    except ZeroDivisionError:
        return '[ОШИБКА] деление на ноль'
    except ValueError:
        return '[ОШИБКА1] операция со строками'
    except Exception as e:
        return f'[ОШИБКА2] {e}'


def main():
    print(calculation(user_input()))


if __name__ == '__main__':
    while True:
        main()