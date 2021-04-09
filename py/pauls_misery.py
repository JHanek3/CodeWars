def paul(x):
    # your code here
    kata = x.count("kata") * 5
    petesKata = x.count('Petes kata') * 10
    eating = x.count('eating')
    total = kata + petesKata + eating
    
    if (total < 40):
        return "Super happy!"
    elif (40 <= total < 70):
        return "Happy!"
    elif (70 <= total < 100):
        return "Sad!"
    else:
        return 'Miserable!'

print(paul(['life', 'eating', 'life']))
print(paul(['life', 'kata', 'life', 'kata', 'eating', 'Petes kata', 'eating', 'life', 'Petes kata', 'life']))