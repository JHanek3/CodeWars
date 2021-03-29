# Task
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3


def zero(func=""):
    if len(func) > 0:
        eval_str = "0 {}".format(func)
        return eval(eval_str)
    else:
        return 0

def one(func=""):
    if len(func) > 0:
        eval_str = "1 {}".format(func)
        return eval(eval_str)
    else:
        return 1

def two(func=""):
    if len(func) > 0:
        eval_str = "2 {}".format(func)
        return eval(eval_str)
    else:
        return 2

def three(func=""):
    if len(func) > 0:
        eval_str = "3 {}".format(func)
        return eval(eval_str)
    else:
        return 3

def four(func=""):
    if len(func) > 0:
        eval_str = "4 {}".format(func)
        return eval(eval_str)
    else:
        return 4

def five(func=""):
    if len(func) > 0:
        eval_str = "5 {}".format(func)
        return eval(eval_str)
    else:
        return 5

def six(func=""):
    if len(func) > 0:
        eval_str = "6 {}".format(func)
        return eval(eval_str)
    else:
        return 6

def seven(func=""):
    if len(func) > 0:
        eval_str = "7 {}".format(func)
        return eval(eval_str)
    else:
        return 7

def eight(func=""):
    if len(func) > 0:
        eval_str = "8 {}".format(func)
        return eval(eval_str)
    else:
        return 8

def nine(func=""):
    if len(func) > 0:
        eval_str = "9 {}".format(func)
        return eval(eval_str)
    else:
        return 9

def plus(right):
    return "+ {}".format(right)

def minus(right):
    return "- {}".format(right)

def times(right):
    return "* {}".format(right)

def divided_by(right):
    return "// {}".format(right)


print(seven(times(five())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))
print(eight(divided_by(three())))

# def zero(f = None): return 0 if not f else f(0)
# def one(f = None): return 1 if not f else f(1)
# def two(f = None): return 2 if not f else f(2)
# def three(f = None): return 3 if not f else f(3)
# def four(f = None): return 4 if not f else f(4)
# def five(f = None): return 5 if not f else f(5)
# def six(f = None): return 6 if not f else f(6)
# def seven(f = None): return 7 if not f else f(7)
# def eight(f = None): return 8 if not f else f(8)
# def nine(f = None): return 9 if not f else f(9)

# def plus(y): return lambda x: x+y
# def minus(y): return lambda x: x-y
# def times(y): return lambda  x: x*y
# def divided_by(y): return lambda  x: x/y