
def calc(operations, num):
    for op in operations:
        if op == '++' or op == '+':
            num += 1
        elif op == '--' or op == '-':
            num -= 1
    return num

#     5    6    7    8    9             
OPE=['++','++','++','++','++','--']

print(calc(OPE,4))