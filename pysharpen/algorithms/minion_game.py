VOWELS = ['A', 'E', 'I', 'O', 'U']


def stuart_predicate(letter):
    return letter not in VOWELS


def kevin_predicate(letter):
    return letter in VOWELS


def start_indexes(string, predicate):
    return [idx for idx, letter in enumerate(string) if predicate(letter)]


def calculate_score(string, start_predicate):
    score = 0
    start_idxs = start_indexes(string, start_predicate)
    processed_substrings = {}
    for start_index in start_idxs: 
        max_substring_len = len(string) - start_index
        for substring_len in range(1, max_substring_len + 1):
            _start_index = start_index
            substring = string[_start_index:_start_index + substring_len]
            if substring in processed_substrings:
                continue
            else:
                processed_substrings[substring] = True
            while True:
                _start_index = string.find(substring, _start_index)
                if _start_index >= 0:
                    score += 1
                    _start_index += 1
                else:
                    break
            print(f"Substring: {substring}. Score: {score}")
    return score


def minion_game(string):
    stuart_score = calculate_score(string, stuart_predicate)
    kevin_score = calculate_score(string, kevin_predicate)
    print(f'Stuart: {stuart_score}', f'Kevin: {kevin_score}')
    if stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    elif stuart_score < kevin_score:
        print('Kevin {}'.format(kevin_score))
    else:
        print('Draw')


def main():
    minion_game('BAANANAS')


if __name__ == '__main__':
    main()
