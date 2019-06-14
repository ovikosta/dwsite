#!/usr/bin/python
import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser(description='Download site.')
    parser.add_argument('url', required=True)
    parser.add_argument('dest_folder', default='./')
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

