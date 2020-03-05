from count import *

'''
Source for one test case: https://10fastfingers.com/text/119-A-simple-Paragraph-to-practice-simple-typing
'''

inputs = [
    'HellO, WorLd!',
    'once upon a tiMe, theRe was a boy Called Ian, and Ian loved to pLay with his dog, Carlos - by the way this is just a made up story because IAn Actually never had A pet Dog in His life :(',
    'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy',
    '! %!1 234@D !412a 2%() A?1dSa sdfl d12j- ;lkdfd mc,la4p o42?dz.',
    'this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters I am typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story about the time i went to the zoo and found a monkey and a fox playing together they were so cute and i think that they were not supposed to be in the same cage but they somehow were and i loved watching them horse around forgive the pun well i hope that it has been highly enjoyable typing this paragraph and i wish you the best of luck getting the best score that you possibly can' 
]

outputs1 = [
{'H': 1, 'e': 1, 'l': 2, 'O': 1, ',': 1, ' ': 1, 'W': 1, 'o': 1, 'r': 1, 'L': 1, 'd': 1, '!': 1} ,
{'o': 9, 'n': 8, 'c': 3, 'e': 14, ' ': 41, 'u': 5, 'p': 4, 'a': 15, 't': 10, 'i': 8, 'M': 1, ',': 3, 'h': 6, 'R': 1, 'w': 3, 's': 9, 'b': 3, 'y': 6, 'C': 2, 'l': 7, 'd': 6, 'I': 3, 'v': 2, 'L': 1, 'g': 2, 'r': 3, '-': 1, 'j': 1, 'm': 1, 'A': 3, 'D': 1, 'H': 1, 'f': 1, ':': 1, '(': 1} ,
{'I': 5, ' ': 22, 'f': 2, 'e': 13, 'l': 5, 't': 5, 'h': 7, 'a': 10, 'p': 8, 'y': 5, 'b': 3, 'c': 2, 'u': 4, 's': 6, 'w': 4, 'o': 2,'r': 3, 'n': 3, 'd': 2, 'k': 1, '’': 1} ,
{'!': 3, ' ': 10, '%': 2, '1': 4, '2': 5, '3': 1, '4': 4, '@': 1, 'D': 1, 'a': 3, '(': 1, ')': 1, 'A': 1, '?': 2, 'd': 6, 'S': 1, 's': 1, 'f': 2, 'l': 3, 'j': 1, '-': 1, ';': 1, 'k': 1, 'm': 1, 'c': 1, ',': 1, 'p': 1, 'o': 1, 'z': 1, '.': 1} ,
{'t': 87, 'h': 46, 'i': 59, 's': 48, ' ': 183, 'a': 57, 'm': 20, 'p': 21, 'l': 27, 'e': 76, 'r': 33, 'g': 22, 'n': 46, 'o': 52, 'b': 13, 'c': 16, 'd': 19, 'y': 27, 'w': 13, 'u': 24, 'j': 3, 'f': 12, 'k': 8, 'I': 1, 'q': 1, 'v': 3, 'z': 1, 'x': 1}
]

outputs2 = [
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1} ,
{'o': 9, 'n': 8, 'c': 5, 'e': 14, ' ': 41, 'u': 5, 'p': 4, 'a': 18, 't': 10, 'i': 11, 'm': 2, ',': 3, 'h': 7, 'r': 4, 'w': 3, 's': 9, 'b': 3, 'y': 6, 'l': 8, 'd': 7, 'v': 2, 'g': 2, '-': 1, 'j': 1, 'f': 1, ':': 1, '(': 1} ,
{'i': 5, ' ': 22, 'f': 2, 'e': 13, 'l': 5, 't': 5, 'h': 7, 'a': 10, 'p': 8, 'y': 5, 'b': 3, 'c': 2, 'u': 4, 's': 6, 'w': 4, 'o': 2,'r': 3, 'n': 3, 'd': 2, 'k': 1, '’': 1} ,
{'!': 3, ' ': 10, '%': 2, '1': 4, '2': 5, '3': 1, '4': 4, '@': 1, 'd': 7, 'a': 4, '(': 1, ')': 1, '?': 2, 's': 2, 'f': 2, 'l': 3, 'j': 1, '-': 1, ';': 1, 'k': 1, 'm': 1, 'c': 1, ',': 1, 'p': 1, 'o': 1, 'z': 1, '.': 1} ,
{'t': 87, 'h': 46, 'i': 60, 's': 48, ' ': 183, 'a': 57, 'm': 20, 'p': 21, 'l': 27, 'e': 76, 'r': 33, 'g': 22, 'n': 46, 'o': 52, 'b': 13, 'c': 16, 'd': 19, 'y': 27, 'w': 13, 'u': 24, 'j': 3, 'f': 12, 'k': 8, 'q': 1, 'v': 3, 'z': 1, 'x': 1}
]

outputs3 = [
[('l', 3), ('o', 2), ('h', 1), ('e', 1), (',', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1), ('!', 1)] ,
[(' ', 41), ('a', 18), ('e', 14), ('i', 11), ('t', 10), ('o', 9), ('s', 9), ('n', 8), ('l', 8), ('h', 7), ('d', 7), ('y', 6), ('c',5), ('u', 5), ('p', 4), ('r', 4), (',', 3), ('w', 3), ('b', 3), ('m', 2), ('v', 2), ('g', 2), ('-', 1), ('j', 1), ('f', 1), (':', 1), ('(', 1)] ,
[(' ', 22), ('e', 13), ('a', 10), ('p', 8), ('h', 7), ('s', 6), ('i', 5), ('l', 5), ('t', 5), ('y', 5), ('u', 4), ('w', 4), ('b', 3), ('r', 3), ('n', 3), ('f', 2), ('c', 2), ('o', 2), ('d', 2), ('k', 1), ('’', 1)] ,
[(' ', 10), ('d', 7), ('2', 5), ('1', 4), ('4', 4), ('a', 4), ('!', 3), ('l', 3), ('%', 2), ('?', 2), ('s', 2), ('f', 2), ('3', 1),('@', 1), ('(', 1), (')', 1), ('j', 1), ('-', 1), (';', 1), ('k', 1), ('m', 1), ('c', 1), (',', 1), ('p', 1), ('o', 1), ('z', 1), ('.', 1)] ,
[(' ', 183), ('t', 87), ('e', 76), ('i', 60), ('a', 57), ('o', 52), ('s', 48), ('h', 46), ('n', 46), ('r', 33), ('l', 27), ('y', 27), ('u', 24), ('g', 22), ('p', 21), ('m', 20), ('d', 19), ('c', 16), ('b', 13), ('w', 13), ('f', 12), ('k', 8), ('j', 3), ('v', 3), ('q', 1), ('z', 1), ('x', 1)] ,
]

def test_count_char(mocker):
    checker = Checker()
    mocker.patch('sys.stdout', checker)

    for i in range(len(inputs)):
        count_char(inputs[i])
        checker.check(outputs1[i])
        checker.clear()


def test_count_char_insensitive(mocker):
    checker = Checker()
    mocker.patch('sys.stdout', checker)

    for i in range(len(inputs)):
        count_char_insensitive(inputs[i])
        checker.check(outputs2[i])
        checker.clear()


def test_count_char_ordered(mocker):
    checker = Checker()
    mocker.patch('sys.stdout', checker)

    for i in range(len(inputs)):
        count_char_ordered(inputs[i])
        checker.check_ordered(outputs3[i])
        checker.clear()


class Checker():

    def __init__(self):
        self._buffer = ''

    def write(self, output):
        self._buffer += output

    def clear(self):
        self._buffer = ''

    def check(self, output):
        o_buffer = ''
        for char, count in output.items():
            o_buffer += f'{char} {count}\n'
        
        # not a perfect bulletproof test, 
        # but works most of the time
        l1 = self._buffer.split('\n')
        l2 = o_buffer.split('\n')
        assert len(l1) == len(l2)

        s1 = set(l1)
        s2 = set(l2)

        assert s1 == s2

    def check_ordered(self, output):
        o_buffer = ''
        for char, count in output:
            o_buffer += f'{char} {count}\n'
        
        assert self._buffer == o_buffer
