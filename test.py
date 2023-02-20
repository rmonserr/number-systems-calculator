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
