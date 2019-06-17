#!/usr/bin/python
#Required python>=3.5
import sys
import os
import argparse
import requests
#from html.parser import HTMLParser

def create_parser_arg():
    parser = argparse.ArgumentParser(description='Download site.')
    parser.add_argument('-u', '--url', required=True, nargs='?', dest='url with protocol "http:// or https://"', type=str)
    parser.add_argument('-df', '--dest-folder', default=os.getcwd(), nargs='?', dest='destination folder', type=str)
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


if __name__ == '__main__':
    args = create_parser_arg()
    args = args.parse_args()
    data = get_site(args.url)
    write_file('index', data, args.destination)


