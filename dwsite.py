#!/usr/bin/python
#Required python>=3.5
import sys
import os
import argparse
import requests
from html.parser import HTMLParser

class SiteParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.href_site = list()

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if 'href' in attr:
                self.href_site.append(attr[1])

def create_parser_arg():
    parser = argparse.ArgumentParser(description='Download site.')
    parser.add_argument('-u', '--url', required=True, nargs='?', dest='url', type=str)
    parser.add_argument('-df', '--dest-folder', default=os.getcwd(), nargs='?', dest='destination', type=str)
    return parser

def get_site(url: str) -> str:
    #verification protocol HTTP or HTTPS
    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        protocol = input('Specify the protocol http or https :')
        protocol = ''.join(ci for ci in protocol.lower() if ci.isalnum()) + '://'
        url = protocol + url
        response = requests.get(url)
    data = response.text
    return data

def write_file(name: str, data, path) -> None:
    suffix = '.html'
    dest_path = os.path.join(path, name + suffix)
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(data)

def parse_html(data):
    site_parser = SiteParser()
    site_parser.feed(data)
    site_parser.close()
    return site_parser.href_site


if __name__ == '__main__':
    args = create_parser_arg()
    args = args.parse_args()
    data = get_site(args.url)
    write_file('index', data, args.destination)
    print(parse_html(data))

