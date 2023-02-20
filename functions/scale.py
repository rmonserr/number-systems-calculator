def     power(dig, pow):
    tmp = dig
    if(pow == 0):
        return 1
    if(pow < 0):
        dig = 1 / power(dig, pow * -1)
        return dig
    while(pow - 1 > 0):
        dig = dig*tmp
        pow -= 1
    return dig


def     to_decimal(str): # Перевод в деятичную систему счисления
    n = len(str) - 1
    count = 0
    tmp = 0

    while(count <= len(str) - 1):
        tmp += power(2, n) * int(str[count])
        n -= 1
        count += 1
    str = tmp
    return str

def     to_binary(dec_num): # Перевод в двоичную систему счисления
    dec_num = int(dec_num)
    rem = 0
    dig = ""
    while (dec_num != 1):
        rem = dec_num % 2 # сюда пишем остаток от деления
        dec_num = int(dec_num / 2)
        dig += str(rem)
    if (dec_num == 1):
        dig += "1"
    dig = "".join(reversed(dig))
    return(dig)

def     to_ternaty(dec_num): #перевод в троичную систему
    dec_num = int(dec_num)
    rem = 0
    dig = ""
    while (dec_num >= 3):
        rem = dec_num % 3 # сюда пишем остаток от деления
        dec_num = int(dec_num / 3)
        dig += str(rem)
    if (dec_num == 1):
        dig += "1"
    dig = "".join(reversed(dig))
    return(dig)