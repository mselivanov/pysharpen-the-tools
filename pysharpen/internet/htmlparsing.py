"""
Module demonstrates working with a HTMLParser class
"""
from html.parser import HTMLParser
import os
from typing import List, Optional, Tuple

from helpers.helpers import print_header


class MyHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool=True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self._metacount = 0

    def handle_comment(self, data: str) -> None:
        super().handle_comment(data) 
        pos = self.getpos()
        print(f'Encountered comment {data} at line {pos[0]} position {pos[1]}')

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        super().handle_starttag(tag, attrs)
        if tag == 'meta':
            self._metacount += 1
        if attrs:
            for attr in attrs:
                print(f'Encountered attribute {attr[0]} with a value {attr[1]}')

    def handle_endtag(self, tag: str) -> None:
        super().handle_endtag(tag)
        pos = self.getpos()
        print(f'Encountered data {tag} at line {pos[0]} position {pos[1]}')

    def handle_data(self, data: str) -> None:
        super().handle_data(data)
        if data.isspace:
            return
        pos = self.getpos()
        print(f'Encountered data {data} at line {pos[0]} position {pos[1]}')


def html_parsing_examples():
    print_header('HTML parsing examples')
    cwd = os.getcwd() 
    filepath = f'{cwd}{os.sep}pysharpen{os.sep}internet{os.sep}samplehtml.html'
    with open(filepath, 'r') as f:
        if f.mode == 'r':
            contents = f.read()
            my_parser = MyHTMLParser()
            my_parser.feed(contents)


def main():
    html_parsing_examples()


if __name__ == '__main__':
    main()