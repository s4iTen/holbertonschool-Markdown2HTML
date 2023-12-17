#!/usr/bin/python3
'''
    Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], 'r') as readme:
        # Read the content of the file
        file_content = readme.read()

        # Check if the content is empty or contains only whitespace
        if not file_content.strip():
            print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
            exit(1)

    # Continue with the rest of your code, e.g., markdown to HTML conversion
    # ...
