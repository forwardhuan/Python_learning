def lengthOfLongestSubstring(s: str) -> int:
    max_count = cur_count = 0
    cur_str = []
    for i in s:
        try:
            index = cur_str.index(i)
            if index != -1:
                cur_str = cur_str[index + 1:]
        except:
            pass
        cur_str.append(i)
    return len(cur_str)
te

print(lengthOfLongestSubstring('adcdcs'))
print('fds'.index('d'))
print('fds'[2:])