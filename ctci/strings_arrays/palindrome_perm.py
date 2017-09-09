from collections import defaultdict


def palindrome_perm(string):
    counts = defaultdict(int)
    for ch in string:
        counts[ch] += 1
    seenodd = False
    for val in counts.values():
        if val%2 !=0:
            if seenodd:
                return False
            else:
                seenodd = True
    return True

print(palindrome_perm('tact coa'.replace(' ','')))
print(palindrome_perm('hotdog'.replace(' ','')))
print(palindrome_perm('mommommom'.replace(' ','')))



    
