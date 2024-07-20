def compress_string(s):
    if not s:
        return s

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed.append(f'{s[i - 1]}{count}')
            else:
                compressed.append(s[i - 1])
            count = 1

    if count > 1:
        compressed.append(f'{s[-1]}{count}')
    else:
        compressed.append(s[-1])

    return ''.join(compressed)

if __name__ == "__main__":
    import sys
    input_string = sys.stdin.read().strip()
    print(compress_string(input_string))