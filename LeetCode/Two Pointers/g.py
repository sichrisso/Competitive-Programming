def compress(chars):
    left, right, count = 0, 0, 0
    if len(chars) == 1:
        return 1
    while right < len(chars):
        if chars[left] == chars[right]:
            right += 1
            count += 1
        if right == len(chars) or chars[left] != chars[right]:
            s = str(count)
            k = 0
            while k < len(s):
                if len(s) == 1 and s[k] == "1":
                    pass
                else:
                    left += 1
                    chars[left] = s[k]
                k += 1
            left += 1
            if right == left:
                count = 0
            else:
                count = -1
            if right < len(chars):
                chars[left] = chars[right]
                right = left
    return left


def main():
    chars = ["a","a","b","b","c","c","c"]
    compress(chars)

main()