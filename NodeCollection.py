from TermNode import *

class NodeCollection:

    def __init__(self, filenames: list):

        self.filenames = filenames
        self.nodes = dict()
        self.terms = list()
        self.corpus = str()

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

        for line in xml:

            if ("sentence" and "text" in line):

                curr_quote = line.find("\"") + 1
                next_quote = line.find("\"", curr_quote)

                # kind = line[curr_quote:next_quote] # lol copied code

                curr_quote = line.find("\"", next_quote + 1) + 1
                next_quote = line.find("\"", curr_quote)
                sentence = line[curr_quote:next_quote] + " "

                for term in nodes.keys():
                    if term in sentence and sentence not in nodes[term].get_sentences():
                        nodes[term].add_sentence(sentence)

        return nodes

    def parse(self) -> list:
        '''
        run parse_file() on all files in dataset, to get collection of nodes
        '''

        for file in self.filenames:

            try:
                curr = self.parse_file(self.process_filename(file))

                for k, v in curr.items():
                    if k not in self.terms:
                        self.nodes[k] = v
                        self.terms.append(k)

            except FileNotFoundError:
                continue

    def process_filename(self, filename) -> list:
        '''
        read a file and parse extension, given a filename

        @returns:
            all the text in the file, a list where each entry is a new line
        '''
        
        with open(filename[:-1]) as f:
            text = f.readlines()

        return text

    def get_nodes(self) -> None:
        '''
        get all nodes in the collection
        '''

        return self.nodes

    def get_terms(self) -> None:
        '''
        get every term mentioned in the dataset
        '''

        return self.terms

    def make_corpus(self) -> None:
        '''
        utilize to_string() to get a corpus to train with of all terms, types, sentences
        set it as self attribute
        '''

        corpus = str()

        for term, node in self.nodes.items():
            corpus += node.to_string() + "\n"
        
        self.corpus = corpus

    def get_corpus(self) -> str:

        if self.corpus == str():
            if self.nodes == dict():
                if self.filenames == list():
                    pass
                else:
                    self.parse()
                    self.make_corpus()
                    return self.corpus
            else:
                self.make_corpus()
                return self.corpus
        else:
            return self.corpus