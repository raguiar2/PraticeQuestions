
def urlify(string,length):
    string = list(string)
    string = string[:length]
    for i in range(len(string)):
        if string[i] == ' ':
            string[i] = '%20'
    return ''.join(string)



print(urlify('a b c', 5))
print(urlify('a b c     ', 5))
print(urlify('abc123', 6))
