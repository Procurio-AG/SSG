import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_different_tag_val(self):
        node = HTMLNode(tag='a',value='link')
        node2 = HTMLNode(tag='p',value='this is not a link')
        self.assertNotEqual(node,node2)

    def test_different_tag(self):
        node = HTMLNode(tag='a',value='link')
        node2 = HTMLNode(tag='p',value='link')
        self.assertNotEqual(node,node2)

    def test_different_val(self):
        node = HTMLNode(tag='a',value='link')
        node2 = HTMLNode(tag='a',value='this is not a link')
        self.assertNotEqual(node,node2)

    def test_equal_props(self):
        node = HTMLNode(tag='a',value='link',props={
                        "href": "https://www.google.com",
                        "target": "_blank",
                                            })
        node2 = HTMLNode(tag='p',value='link',props={
                        "href": "https://www.google.com",
                        "target": "_blank",
                                            })
        self.assertEqual(node,node2)