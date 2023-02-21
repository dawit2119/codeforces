t = int(input())

for _ in range(t):
    s = input().strip()
    freq = [0] * 26
    
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    res = ''
    for i in range(26):
        if freq[i] % 2 == 0:
            res += chr(i + ord('a'))
    
    print(res)
