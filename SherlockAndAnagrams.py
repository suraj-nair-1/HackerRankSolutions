
def countChars(s):
    chars = {}
    for ch in s:
        if chars.has_key(ch):
            chars[ch] = chars[ch] + 1
        else:
            chars[ch] = 1
    return chars

num_tests = int(raw_input())
for tests in range(0, num_tests):
    s = raw_input()
    subs = {}
    for i in range(0, len(s)+1):
        for j in range(0, i):
            sub = s[j:i]
            if subs.has_key(len(sub)):
                subs[len(sub)] = subs[len(sub)] + [( countChars(sub))]
            else:
                subs[len(sub)] = [(countChars(sub))]
    total = 0
    for a in range(1, len(s)+1):
        substrs = subs[a]
        for i in range(0, len(substrs)):
            for j in range(0, i):
                if cmp(substrs[i], substrs[j]) == 0:
                    total += 1
    print total
