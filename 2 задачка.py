def math(a, b):
    res = ''
    for i in range(len(a)):
        if a[i] == '+' and b[i] == '+':
            res += '+-'
        if a[i] == '-' and b[i] == '-':
            res += '-+'
        if a[i] == '0' and b[i] == '0':
            res += '0'
        if (a[i] == '+' and b[i] == '0') or (a[i] == '0' and b[i] == '+'):
            res += '+'
        if (a[i] == '-' and b[i] == '0') or (a[i] == '0' and b[i] == '-'):
            res += '-'
        if (a[i] == '+' and b[i] == '-') or (a[i] == '-' and b[i] == '+'):
            res += '0'
    return res


def check(x, y):
    if len(x) < len(y):
        for i in range(len(y) - len(x)):
            x = '0' + x
    elif len(x) > len(y):
        for i in range(len(x) - len(y)):
            y = '0' + y
    return x, y


def main():
    user = input().split('(')
    if user == ['']:
        return
    user[1] = user[1].split(')')
    if user[1][0] == '+':
        user[0], user[1][1] = check(user[0], user[1][1])
        print(math(user[0], user[1][1]))
    elif user[1][0] == '-':
        user[1][0], user[1][1] = check(user[1][0], user[1][1])
        user[1][1] = math(user[1][0], user[1][1])
        user[0], user[1][1] = check(user[0], user[1][1])
        print(math(user[0], user[1][1]))


main()
