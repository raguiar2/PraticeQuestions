import sys 


args = [arg for arg in sys.argv]

string = args[1]

def unique_chars(string):
    seen = {}
    for ch in string:
        if ch in seen:
            return False
        seen[ch] = 1
    return True

def unique_chars_no_dup(string):
    string.sort()
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            return False
    return True

print(unique_chars(string))
print(unique_chars_no_dup(list(string)))


