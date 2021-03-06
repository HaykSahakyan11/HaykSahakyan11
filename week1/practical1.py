def implication3(a, b, c):
    return not a or (b and c)


def expr_value(*args):
    a_list = [args[0][i] for i in range(len(args[0]))]
    return calculation(a_list)


def calculation(b_list):
    func = ["*", "/", "-", "+"]
    for i in range(len(func)):
        if func[i] == "*":
            while "*" in b_list:
                ind = b_list.index("*")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) * float(b)] + b_list[ind + 2:]
        if func[i] == "/":
            while "/" in b_list:
                ind = b_list.index("/")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) / float(b)] + b_list[ind + 2:]
        if func[i] == "-":
            while "-" in b_list:
                ind = b_list.index("-")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) - float(b)] + b_list[ind + 2:]
        if func[i] == "+":
            while "+" in b_list:
                ind = b_list.index("+")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) + float(b)] + b_list[ind + 2:]

    return round(b_list[0], 2)


def is_polyndrome(a_string):
    d = dict()
    for letter in a_string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] = d[letter] + 1
    odd = 0
    for value in d.values():
        if value % 2 != 0:
            odd += 1
    if odd > 1:
        return False
    return True


print(expr_value("6-5*4/3+3-2*4"))
