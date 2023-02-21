from collections import defaultdict

def has_concatenation(s):
    prefixes = defaultdict(bool)
    for i in range(len(s)):
        if i > 0:
            prefixes[s[:i]] = True
        if prefixes[s[i:]]:
            return True
    return False

t = int(input())

for _ in range(t):
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input().strip())

    result = ""
    for s in strings:
        if has_concatenation(s):
            result += "1"
        else:
            result += "0"
    print(result)
