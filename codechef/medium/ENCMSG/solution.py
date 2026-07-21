t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    l = []
    for i in range(0, n - 1, 2):
        l.append(s[i + 1])
        l.append(s[i])
        
    if n % 2 != 0:
        l.append(s[-1])
        
    encoded_chars = []
    for char in l:
        new_char = chr(122 - (ord(char) - 97))
        encoded_chars.append(new_char)
        

    ans = "".join(encoded_chars)
    print(ans)