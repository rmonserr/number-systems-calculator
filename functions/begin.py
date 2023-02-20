from .scale import to_decimal
from .scale import to_binary
from .scale import to_ternaty

def     check_decimal(str):
    count = 0
    tmp = ""

    while(count <= len(str) - 1):
        if (str[count] == " " or str[count] == "\t"):
            count +=1
        else:
            if (str[count] >= chr(48) and str[count] <= chr(49)):
                tmp += str[count]
                count +=1
            else:
                str = "Это не двоичное число!"
                return (str)
    str = tmp
    str = to_decimal(str)
    return(str)

def     check(flag, str):
    count = 0
    tmp = ""

    while(count <= len(str) - 1):
        if (str[count] == " " or str[count] == "\t"):
            count +=1
        else:
            if (str[count] >= chr(48) and str[count] <= chr(57)):
                tmp += str[count]
                count +=1
            else:
                str = "Неправильное значение!"
                return (str)
    str = tmp
    if(flag == 2):
        str = to_binary(str)
    if(flag == 3):
        str = to_ternaty(str)
    else:
        str = check_decimal(str)
    return(str)

def     begin():
    flag = input("Выбери систему счисления, в которую необходимо перевести число:\n    1 - перевести двоичное в десятичное.\
        \n    2 - перевести десятичное в двоичное.\n    3 - перевести в десятичное в троичное.\n")
    flag = int(flag)
    data = input("Введи число, которое будем переводить: ")
    data = check(flag, data)
    print(data) # тестовый принт
    return 
