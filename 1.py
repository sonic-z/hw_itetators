class FlatIterator:

    def __init__(self, list_of_list):

        self.list_of_list = list_of_list
        self.all_cursor = 0
        self.cursor = 0
        self.list = []
        self.flag = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.flag:
            if self.cursor >= len(self.list):
                self.flag = False
                return next(self)
            item = self.list[self.cursor]
            self.cursor += 1
            return item
        else:
            if self.all_cursor >= len(self.list_of_list):
                raise StopIteration
            item = self.list_of_list[self.all_cursor]
            self.all_cursor += 1
            self.flag = isinstance(item, list)
            if self.flag:
                self.list = item
                self.cursor = 0
                return next(self)
            else:
                return item
                

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
