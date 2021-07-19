"""
Module demonstrates working with XML files
"""

from helpers.helpers import print_header
import os
import xml.dom.minidom


def xml_parsing_examples():
    print_header('XML parsing examples') 
    filepath = f'{os.getcwd()}{os.sep}pysharpen{os.sep}internet{os.sep}samplexml.xml'
    doc = xml.dom.minidom.parse(filepath)
    print(f'First node name: {doc.nodeName}')
    print(f'First child tag name: {doc.firstChild.tagName}')
    skills = doc.getElementsByTagName('skill')
    for skill in skills:
        print(f'Has skill: {skill.getAttribute("name")}')
    new_skill = doc.createElement('skill')
    new_skill.setAttribute('name', 'Microsoft Azure')
    doc.firstChild.appendChild(new_skill)


def main():
    xml_parsing_examples()


if __name__ == '__main__':
    main()