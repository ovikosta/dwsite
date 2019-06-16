#!/usr/bin/python
#Required python>=3.5
import sys
import argparse
import http.client
import ssl
from html.parser import HTMLParser

def create_parser_arg():
    parser = argparse.ArgumentParser(description='Download site.')
    parser.add_argument('-u', '--url', required=True, nargs='?', type=str)
    parser.add_argument('-df', '--dest-folder', default='./', nargs='?', type=str)
    return parser

def download_site(url: str) -> None:
    #verification protocol HTTP or HTTPS
    try:
        conn = http.client.HTTPSConnection(url) 
        conn.request('GET', '/')
    except ssl.SSLCertVerificationError:
        conn = http.client.HTTPConnection(url)
        conn.request('GET', '/')
    resp = conn.getresponse()
    raw_data = resp.read()
    data = raw_data.decode('utf-8')



def write_file(name: str, data) -> None:
    with open(name, 'w') as file:
        file.write(data)


if __name__ == '__main__':
    parser = create_parser_arg()
    namespace = parser.parse_args()


