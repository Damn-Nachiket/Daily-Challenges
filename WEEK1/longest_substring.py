#day-1 - python
def longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index_map:
            left = max(left, char_index_map[s[right]] + 1)

        char_index_map[s[right]] = right
        max_length = max(max_len, right - left + 1)

    return max_len

#test cases

assert longest_substring("abcabcbb") == 3
assert longest_substring("bbbbb") == 1
assert longest_substring("pwwkew") == 3
assert longest_substring(" ") == 1
assert longest_substring("dvdf") == 3
assert longest_substring(" ") == 1

print("100% PASS")