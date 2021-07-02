
"""
Implement the AI program on Crpt arithmetic Problem
"""
import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def solve2(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

if __name__ == '__main__':
    #SEND + MORE = MONEY
    solve2(input('Enter Equation: '))

"""
Output: 
Enter Equation: SEND + MORE = MONEY
7531 + 825 = 8356 (mapping: {'o': 8, 'n': 3, 'e': 5, 'd': 1, 'r': 2, 'm': 0, 's': 7, 'y': 6})
6851 + 738 = 7589 (mapping: {'o': 7, 'n': 5, 'e': 8, 'd': 1, 'r': 3, 'm': 0, 's': 6, 'y': 9})
5731 + 647 = 6378 (mapping: {'o': 6, 'n': 3, 'e': 7, 'd': 1, 'r': 4, 'm': 0, 's': 5, 'y': 8})
3821 + 468 = 4289 (mapping: {'o': 4, 'n': 2, 'e': 8, 'd': 1, 'r': 6, 'm': 0, 's': 3, 'y': 9})
8432 + 914 = 9346 (mapping: {'o': 9, 'n': 3, 'e': 4, 'd': 2, 'r': 1, 'm': 0, 's': 8, 'y': 6})
8542 + 915 = 9457 (mapping: {'o': 9, 'n': 4, 'e': 5, 'd': 2, 'r': 1, 'm': 0, 's': 8, 'y': 7})
5732 + 647 = 6379 (mapping: {'o': 6, 'n': 3, 'e': 7, 'd': 2, 'r': 4, 'm': 0, 's': 5, 'y': 9})
3712 + 467 = 4179 (mapping: {'o': 4, 'n': 1, 'e': 7, 'd': 2, 'r': 6, 'm': 0, 's': 3, 'y': 9})
6853 + 728 = 7581 (mapping: {'o': 7, 'n': 5, 'e': 8, 'd': 3, 'r': 2, 'm': 0, 's': 6, 'y': 1})
7643 + 826 = 8469 (mapping: {'o': 8, 'n': 4, 'e': 6, 'd': 3, 'r': 2, 'm': 0, 's': 7, 'y': 9})
8324 + 913 = 9237 (mapping: {'o': 9, 'n': 2, 'e': 3, 'd': 4, 'r': 1, 'm': 0, 's': 8, 'y': 7})
7534 + 825 = 8359 (mapping: {'o': 8, 'n': 3, 'e': 5, 'd': 4, 'r': 2, 'm': 0, 's': 7, 'y': 9})
6524 + 735 = 7259 (mapping: {'o': 7, 'n': 2, 'e': 5, 'd': 4, 'r': 3, 'm': 0, 's': 6, 'y': 9})
6415 + 734 = 7149 (mapping: {'o': 7, 'n': 1, 'e': 4, 'd': 5, 'r': 3, 'm': 0, 's': 6, 'y': 9})
7316 + 823 = 8139 (mapping: {'o': 8, 'n': 1, 'e': 3, 'd': 6, 'r': 2, 'm': 0, 's': 7, 'y': 9})
2817 + 368 = 3185 (mapping: {'o': 3, 'n': 1, 'e': 8, 'd': 7, 'r': 6, 'm': 0, 's': 2, 'y': 5})
9567 + 1085 = 10652 (mapping: {'o': 0, 'n': 6, 'e': 5, 'd': 7, 'r': 8, 'm': 1, 's': 9, 'y': 2})
7429 + 814 = 8243 (mapping: {'o': 8, 'n': 2, 'e': 4, 'd': 9, 'r': 1, 'm': 0, 's': 7, 'y': 3})
7539 + 815 = 8354 (mapping: {'o': 8, 'n': 3, 'e': 5, 'd': 9, 'r': 1, 'm': 0, 's': 7, 'y': 4})
7649 + 816 = 8465 (mapping: {'o': 8, 'n': 4, 'e': 6, 'd': 9, 'r': 1, 'm': 0, 's': 7, 'y': 5})
6419 + 724 = 7143 (mapping: {'o': 7, 'n': 1, 'e': 4, 'd': 9, 'r': 2, 'm': 0, 's': 6, 'y': 3})
5849 + 638 = 6487 (mapping: {'o': 6, 'n': 4, 'e': 8, 'd': 9, 'r': 3, 'm': 0, 's': 5, 'y': 7})
3719 + 457 = 4176 (mapping: {'o': 4, 'n': 1, 'e': 7, 'd': 9, 'r': 5, 'm': 0, 's': 3, 'y': 6})
3829 + 458 = 4287 (mapping: {'o': 4, 'n': 2, 'e': 8, 'd': 9, 'r': 5, 'm': 0, 's': 3, 'y': 7})
2819 + 368 = 3187 (mapping: {'o': 3, 'n': 1, 'e': 8, 'd': 9, 'r': 6, 'm': 0, 's': 2, 'y': 7})
"""
