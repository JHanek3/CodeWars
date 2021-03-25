def rot(strng):
    strng_fin = strng[::-1]
    return strng_fin

def selfie_and_rot(strng):
    length = 0
    len_list = strng.split("\n")
    length = len(len_list[0]) * "."

    strng_n = strng.replace("\n", "{}\n".format(length))
    strng_rev = strng[::-1]
    strng_rev = strng_rev.replace("\n", "\n{}".format(length))
    strng_full = strng_n + "{}\n{}".format(length, length) + strng_rev
    return strng_full

def oper(fct, s):
    return fct(s)

        
# testing(oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"), "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif")
# testing(oper(rot, "rkKv\ncofM\nzXkh\nflCB"), "BClf\nhkXz\nMfoc\nvKkr")

print(oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"))
print(oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP"))