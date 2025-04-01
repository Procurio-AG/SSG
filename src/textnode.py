from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        return
    
    def __eq__(self,t2):
        if self.text == t2.text:
            if self.text_type == t2.text_type:
                if self.url == t2.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        

'''if TextType.self.text_type == "normal":
            return f"TextNode(**{self.text}**,{self.text_type}**,{self.url})"
        elif TextType.self.text_type == "bold":
            return f"TextNode(**{self.text}**,{self.text_type},{self.url})"
        elif TextType.self.text_type == "italic":
            return f"TextNode(_{self.text}_,{self.text_type},{self.url})"
        elif TextType.self.text_type == "code":
            return f"TextNode(`{self.text}`,{self.text_type},{self.url})"
        elif TextType.self.text_type == "link":
            return f"TextNode([{self.text}],({self.url}))"
        elif TextType.self.text_type == "url":
            return f"TextNode(![{self.text}],({self.url}))"'''