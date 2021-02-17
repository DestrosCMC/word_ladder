#!/bin/python3


import collections


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    word_list = open(dictionary_file, 'r').readlines()

    wordList = [wordd[:5] for wordd in word_list]

    if start_word == end_word:
        return [start_word]
    if len(start_word) != len(end_word):
        return None

    if not end_word or not start_word or not wordList or\
            end_word not in wordList:
        return []

    L = len(start_word)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time.
    all_combo_dict = collections.defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    # Shortest path, BFS
    ans = []
    queue = collections.deque()
    queue.append((start_word, [start_word]))
    visited = set([start_word])

    while queue and not ans:
        length = len(queue)
        localVisited = set()
        for _ in range(length):
            word, path = queue.popleft()
            for i in range(L):
                for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                    if nextWord == end_word:
                        # path.append(endword)
                        ans.append(path+[end_word])
                    if nextWord not in visited:
                        localVisited.add(nextWord)
                        queue.append((nextWord, path+[nextWord]))
        visited = visited.union(localVisited)
    if not ans:
        return None
    else:
        return ans[0]


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    verify = 0
    if not ladder:
        verify = False
    if len(ladder) == 1:
        verify = True
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i+1]):
            return False
        else:
            verify = True
    return verify


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) == len(word2):
        counter = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
        if counter <= 1:
            return True
        else:
            return False
