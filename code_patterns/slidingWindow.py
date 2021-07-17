# Application of sliding window 
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    while len(char_frequency) > k:
        left_char = str[window_start]
        window_start += 1
        char_frequency[left_char] -= 1
        if char_frequency[left_char] == 0:
            del char_frequency[left_char]
    max_length = max(max_length,window_end-window_start+1)
  return max_length

# main
print(longest_substring_with_k_distinct("aarai",2))
print(longest_substring_with_k_distinct("sdwwdcv",2))
print(longest_substring_with_k_distinct("sdwwdcv",3))

