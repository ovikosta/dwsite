#!/usr/bin/python
#Required python>=3.5
import sys
import os
import re
import argparse
import requests
from html.parser import HTMLParser

root_path = ''
all_path = set()

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

def get_page(url):
    #verification protocol HTTP or HTTPS
    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        url = add_protocol_site(url)
        response = requests.get(url)
    data = response.text
    return data

def add_protocol_site(url):
    global root_path
    protocol = input('Specify the protocol http or https :')
    protocol = ''.join(ci for ci in protocol.lower() if ci.isalnum()) + '://'
    url = protocol + url
    root_path = url
    return url

def write_file(name, path, data):
    suffix = '.html'
    dest_path = os.path.join(path, name + suffix)
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(data)

def parse_html(data):
    global all_path
    site_parser = SiteParser()
    site_parser.feed(data)
    site_parser.close()
    #add all path from html page except root path
    all_path = {m for m in site_parser.href_site if root_path in m and m != root_path}
    return all_path

if __name__ == '__main__':
    html_pattern = re.compile(r'(http|https):\/\/([\w-]+\.)+[\w-]+(\/[\w\-.\/?%&=]*)?')
    args = create_parser_arg()
    args = args.parse_args()
    path = args.url
    name = 'index'
    html_page = get_page(path)
    flag = 1
    while flag:
        all_path = set([html_pattern.match(m) for m in parse_html(html_page)])
        for path in all_path:
            
    write_file(name, args.destination, html_page)
    print(set([ html_pattern.match(m) for m in parse_html(html_page)]))


