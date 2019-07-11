# Как передать копию списка или словаря в функцию?
def list_in_func(array_x):
    array_x.reverse()
    return array_x


def wordbook_in_func(wordbook_x):
    return wordbook_x


if __name__ == '__main__':
    array = [1, 2, 3]
    copy_of_array = array.copy()
    list_in_func(copy_of_array)
    print(array, copy_of_array)
    wordbook = {'a': 1, 'b': 2, 'c': 3}
    copy_of_wordbook = wordbook_in_func(wordbook.copy())
    print(wordbook, copy_of_wordbook)
