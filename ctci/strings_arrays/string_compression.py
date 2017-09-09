

def compress_string(string):
    if not string:
        return ''
    compressed = ''
    ch = string[0]
    count = 1
    for i in range(1,len(string)):
        if string[i-1] != string[i]:
            compressed += ch + str(count)
            ch = string[i]
            count = 1
        else:
            count += 1
    compressed += ch + str(count)
    print(compressed)

compress_string('abc')
compress_string('abaacaabb')
compress_string('aaaaacccccbbbaa')

