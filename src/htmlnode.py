
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        props = ""
        for key, value in self.props.items():
            if value is not None:
                props += f' {key}="{value}"'
        return props
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    def __eq__(self,node):
        if self.tag == node.tag:
            if self.value == node.value:
                if self.children == node.children:
                    if self.props == node.props:
                        return True
        return False
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if (self.tag==None):
            return f'{self.value}'
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag missing")
        if self.children == None:
            raise ValueError("No children")
        
        children_html = ''
        for child in self.children:
            children_html+=child.to_html()
            
        if self.props==None:
            return f'<{self.tag}>{children_html}</{self.tag}>'
        else :
            return f'<{self.tag}>{self.props_to_html}</{self.tag}>' 
