from TermNode import *

class NodeCollection:

    def __init__(self, filenames: list):

        self.filenames = filenames
        self.nodes = dict()
        self.terms = list()

    def parse_file(self, xml: list) -> dict:
        '''
        parse xml files in dataset to find names and types of drugs
        does not account for links, but isolates the named entities

        @params:
            xml: the current file being passed in

        @returns:
            a dictionary of nodes in format {node name : node}'''

        nodes = dict()

        for line in xml:
            if ("type" and "text" in line) and ("sentence" not in line):
                
                curr_quote = line.find("\"") + 1
                next_quote = line.find("\"", curr_quote)

                kind = line[curr_quote:next_quote]

                curr_quote = line.find("\"", next_quote + 1) + 1
                next_quote = line.find("\"", curr_quote)

                name = line[curr_quote:next_quote].lower()

                if name not in nodes:
                    nodes[name] = TermNode(name = name, kind = kind)

        return nodes

    def parse(self) -> list:

        for file in self.filenames:

            try:
                curr = self.parse_file(self.process_filename(file))

                for k, v in curr.items():
                    if k not in self.terms:
                        self.nodes[k] = v
                        self.terms.append(k)

            except FileNotFoundError:
                continue

    def process_filename(self, filename):
        
        with open(filename[:-1]) as f:
            text = f.readlines()

        return text

    def get_nodes(self):

        return self.nodes

    def get_terms(self):

        return self.terms
    