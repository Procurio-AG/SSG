from textnode import TextNode,TextType
from htmlnode import *

def text_node_to_html_node(textnode):
    match(textnode.text_type):
        case TextType.TEXT:
            return LeafNode(None,value=textnode.text)
        case TextType.BOLD:
            return LeafNode('b',value=textnode.text)        
        case TextType.ITALIC:
            return LeafNode('i',value=textnode.text)
        case TextType.CODE:
            return LeafNode('code',value=textnode.text)
        case TextType.LINK:
            return LeafNode('a',value=textnode.text,props={"href":textnode.url})
        case TextType.IMAGE:
            return LeafNode('img',None,props={"src":textnode.url, "alt":textnode.text})
        case _:
            raise Exception("Invalid texttype")

def main():
    t1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(t1)

main()
