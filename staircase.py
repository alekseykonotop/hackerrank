def create_stairse():
    n = int(input('Укажите число ступеней: '))
    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)

create_stairse()