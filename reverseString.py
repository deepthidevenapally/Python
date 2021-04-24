
def reverse(string):
    for i in range(len(string)):
        string[i],string[i-1]=string[i-1],string[i]
    return string
