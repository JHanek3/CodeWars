# Task
# rotate("Hello") => ["elloH", "lloHe", "loHel", "oHell", "Hello"]

def rotate(str_):
    fin_array = []
    for x in range(len(str_)):
        fin_array.append(str_[x+1:] + str_[:x + 1])
    return fin_array

print(rotate("Hello"))