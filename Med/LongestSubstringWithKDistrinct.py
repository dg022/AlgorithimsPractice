def longest_substring_with_k_distinct(str, k):
    # TODO: Write your code here

    dict = {}
    start = 0
    length = float('-inf')
    for end in range(len(str)):

        if str[end] in dict:
            dict[str[end]] += 1
        else:
            dict[str[end]] = 0

        while len(dict) > k:
            if dict[str[start]] == 0:
                del dict[str[start]]
            else:
                dict[str[start]] -= 1

            start += 1

        length = max(length, end - start + 1)

    if length == float('-inf'):
        return 0

    return length

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()