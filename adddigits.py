
def add_digits(ansexp, expression, i):
    if i == 9:
        if eval(ansexp) == 99:
            print(ansexp)
        return 
    add_digits(ansexp +  expression[i], expression, i + 1)
    if i != 0:
        add_digits(ansexp + '+' +  expression[i], expression, i + 1)
        add_digits(ansexp, expression, i + 1)

add_digits('','123456789',0)
