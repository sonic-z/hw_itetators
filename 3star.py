class FlatIterator:

    def __init__(self, list_of_list):

        self.list_of_list = list_of_list
        self.cursor = 0
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor >= len(self.list_of_list):
            if self.stack:
                self.list_of_list, self.cursor = self.stack.pop()
                return next(self)
            else:
                raise StopIteration

        item = self.list_of_list[self.cursor]
        self.cursor += 1

        if isinstance(item, list):
            self.stack.append((self.list_of_list, self.cursor))
            self.list_of_list = item
            self.cursor = 0
            return next(self)
        else:
            return item

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
