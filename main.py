import unittest


class Node:

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data


class TestNode(unittest.TestCase):

    def test_should_be_able_to_get_data(self):
        node = Node(93)
        self.assertEqual(93, node.data)


if __name__ == '__main__':
    unittest.main()


