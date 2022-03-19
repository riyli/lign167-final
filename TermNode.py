class TermNode:
    '''
    the purpose of this is class is to store words, their type, and a dictionary of every word linked to it
    attributes:
        name: a string of what it is named
        kind: the type of the object (drug, group, etc)
        links: a list containing objects (name, kind, links) that this object is linked to
    '''

    def __init__(self, name: str, kind: str, links: list = list()):
        '''
        initialize the class with name, type, and empty dictionary
        '''

        self.name = name
        self.kind = kind
        self.links = links

    def get_name(self) -> str:
        '''
        gets the name of the term
            returns: self.name, the name of the term
        '''

        return self.name

    def set_name(self, name) -> None:
        '''
        sets name to new input
        '''

        self.name = name

    def get_type(self) -> str:
        '''
        get the type of the term
            returns: self.kind, the type of the term
        '''

        return self.kind

    def set_type(self, kind) -> None:
        '''
        sets type to new input
        '''

        self.kind = kind

    def get_links(self) -> list:
        '''
        get the list of every term this term is linked to
            returns: self.links, a list of ddistrucs which are linked to this term
        '''

        return self.links

    def get_link_names(self) -> list:
        '''
        get a list of names (in str type) of terms that this term is linked to
            returns: names, a list of .getName() for every term in self.links
        '''

        names = [ node.get_name() for node in self.links ]

        return names

    def get_link_dict(self) -> dict:
        '''
        get a dict of {name:obj} of terms that this term is linked to
        
            returns: names, a dict wherein the keys are names of terms and the value is the term 
                        object itself for every term in self.links
        '''

        names = { node.get_name() : node for node in self.links }

        return names

    def add_link(self, name, kind) -> None:
        '''
        add a link, such that the two terms are linked
        '''

        self.links.append(TermNode(name, kind))