"""
Module demonstrates calculating number of anagram substrings in string
"""


def substring_buckets(analyzed_str):
    """
    Generate all substrings grouped by substring len.
    Substrings are sorted.
    """
    buckets = {}
    str_len = len(analyzed_str)
    for substr_sz in range(1, str_len):
        buckets[substr_sz] = [''.join(sorted(analyzed_str[i:(i+substr_sz)]))
                              for i in range(0, str_len-substr_sz+1)]
    return buckets

def number_of_anagrams(analyzed_string):
    "Counts number of anagram substrings"
    total_anagrams = 0
    buckets = substring_buckets(analyzed_string)
    for key in buckets:
        substrings = buckets[key]
        for idx in range(0, len(substrings) - 1):
            total_anagrams += substrings[idx+1:].count(substrings[idx])
    return total_anagrams


def main():
    "Main function"
    print(number_of_anagrams('cdcd')) 

if __name__ == '__main__':
    main()
