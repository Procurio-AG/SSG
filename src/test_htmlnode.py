import unittest
from htmlnode import *

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

    def test_props_to_html(self):
        node = HTMLNode(tag='a', value='link', props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        
        result = node.props_to_html()
        expected1 = ' href="https://www.google.com" target="_blank"'
        expected2 = ' target="_blank" href="https://www.google.com"'
        self.assertTrue(result == expected1 or result == expected2)

    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )