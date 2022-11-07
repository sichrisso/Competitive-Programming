def compress(self, chars: List[str]) -> int: 
    s = []
    left, right, count = 0, 0, 0
    while right < len(chars):
        if chars[left] == chars[right]:
            right += 1
            count += 1
        if right == len(chars) or chars[left] != chars[right]:
            s.append(str(chars[left]))
            if 1 < count < 10:
                s.append(str(count))
            elif count >= 10:
                count = str(count)
                n = 0
                while n < len(count):
                    s.append(str(count[n]))
                    n += 1
            count = 0
            left = right
    for i in range(len(s)):
        chars[i] = s[i]
    return len(s)