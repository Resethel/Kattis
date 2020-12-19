#!/usr/bin/env python3
"""
Archive all the problems found in the "Problems" folder.

Also create a JSONinformation file.
"""
import os
import re

PROBLEM_FOLDER = "Problems"

EXTENSION = {
    'c':        'C',
    'c++':      'C++',
    'cc':       'C++',
    'c#':       'C#',
    'cpp':      'C++',
    'cs':       'C#',
    'cxx':      'C++',
    'cbl':      'COBOL',
    'cob':      'COBOL',
    'cpy':      'COBOL',
    'fs':       'F#',
    'go':       'Go',
    'h':        'C++',
    'hs':       'Haskell',
    'java':     'Java',
    'js':       'JavaScript',
    'kt':       'Kotlin',
    'lisp':     'Common Lisp',
    'cl':       'Common Lisp',
    'm':        'Objective-C',
    'ml':       'OCaml',
    'pas':      'Pascal',
    'php':      'PHP',
    'pl':       'Prolog',
    'py':       'Python3',  # Python is assumed as I'm never gonna use Python 2
    'rb':       'Ruby',
    'rs':       'Rust',
    'scala':    'Scala',
}

FILES_TO_IGNORE = [
    ".DS_Store"
]


def is_python2(file):
    """Determine if a python file a Python2 file or Python 3."""
    python2 = re.compile(r'^\s*\bprint\b *[^ \(\),\]]|\braw_input\b')
    try:
        with open(file) as f:
            for index, line in enumerate(f):
                if index == 0 and line.startswith('#!'):
                    if 'python2' in line:
                        return True
                    if 'python3' in line:
                        return False
                if python2.search(line.split('#')[0]):
                    return True
    except IOError:
        return False
    return False
# def is_python2


if __name__ == "__main__":
    origin_dir = os.getcwd()
    try:
        os.chdir(os.path.join(origin_dir, PROBLEM_FOLDER))
        cwd = os.getcwd()
        # List all the files in the problems folder
        orphan_problems = []
        existing_problems = []
        for item in os.listdir(cwd):
            if item in FILES_TO_IGNORE:
                continue
            if os.path.isfile(os.path.join(cwd, item)):
                orphan_problems.append(item)
            else:
                existing_problems.append(item)

        # Check if there is an already a problem folder for the item, otherwise
        # create a folder with the extension for the problem
        for problem in orphan_problems:
            pb_wo_ext, pb_ext = problem.split(".")
            if pb_wo_ext not in existing_problems:
                os.mkdir(pb_wo_ext)
                print("Creating folder for problem \"{}\"".format(pb_wo_ext))

            if pb_ext in EXTENSION:
                if os.path.exists(os.path.join(pb_wo_ext, EXTENSION[pb_ext])):
                    print("A {} solution for {} already exists")
                    continue
                else:
                    os.mkdir(os.path.join(pb_wo_ext, EXTENSION[pb_ext]))
                    os.rename(problem, os.path.join(pb_wo_ext, EXTENSION[pb_ext], problem))
                    print("Moving \"{}\" to folder \"{}\"".format(problem, EXTENSION[pb_ext], pb_wo_ext))
            else:
                print("Unknow extension \".{}\" for {}".format(pb_ext, problem))

    finally:
        os.chdir(origin_dir)
