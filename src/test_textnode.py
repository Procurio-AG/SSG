import unittest
from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
    def test_different_text(self):
        node = TextNode("This is a text node",TextType.BOLD)
        node2 = TextNode("This is a different text node",TextType.BOLD)
        self.assertNotEqual(node,node2)
    
    def test_different_type(self):
        node = TextNode("This is a text node",TextType.BOLD)
        node2 = TextNode("This is a text node",TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_different_url(self):
        node = TextNode("This is a text node",TextType.BOLD,url='abc.abc')
        node2 = TextNode("This is a text node",TextType.BOLD,url = 'xyz.xyz')
        self.assertNotEqual(node,node2)

    def test_eq(self):
        node = TextNode("This is a text node",TextType.BOLD)
        node2 = TextNode("This is a different text node",TextType.BOLD)
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()
