#printing the frequency of the input string.

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
string = input("enter the string:")
print(most_frequent(string))
