import unittest


class Node:

    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class TestNode(unittest.TestCase):

    def test_should_be_able_to_get_data(self):
        node = Node(93)
        self.assertEqual(93, node.data)

    def test_should_be_able_to_set_data(self):
        node = Node(93)
        node.data = 39
        self.assertEqual(39, node.data)

    def test_should_be_able_to_get_next_when_init(self):
        node = Node(93)
        self.assertEqual(None, node.next)

    def test_should_be_able_to_set_next(self):
        node = Node(93)
        next_node = Node(7)
        node.next = next_node
        self.assertEqual(next_node, node.next)


if __name__ == '__main__':
    unittest.main()


