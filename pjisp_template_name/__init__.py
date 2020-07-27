#!/usr/bin/env python2

import os
import click
from distutils.dir_util import copy_tree

ERROR_MESSAGE = 'Repository name not valid. Error on {}'
LENGTH_MESSAGE = 'Repository name length not valid'
PROGRAMS = ('E214', 'E111')
TEMPLATES = ('T12', 'T34', 'SOV')

def check_pjisp(pjisp):
    if pjisp != 'pjisp':
        print(ERROR_MESSAGE.format(pjisp))
        exit(1)

def check_year(year):
    try:
        int(year)
    except ValueError:
        print(ERROR_MESSAGE.format(year))
        exit(1)

def check_program(program):
    if program not in PROGRAMS:
        print(ERROR_MESSAGE.format(program))
        exit(1)

def check_template(template):
    if template not in TEMPLATES:
        print(ERROR_MESSAGE.format(template))
        exit(1)

def check_group(group):
    if not group.startswith('G'):
        print(ERROR_MESSAGE.format(group))
        exit(1)
    try:
        int(group[1:])
    except ValueError:
        print(ERROR_MESSAGE.format(group))
        exit(1)

def check_repo_name(repo_name):
    try:
        pjisp, year, program, template, group = repo_name.split("-")
    except ValueError:
        print(LENGTH_MESSAGE)
        exit(1)

    check_pjisp(pjisp)
    check_year(year)
    check_program(program)
    check_template(template)
    check_group(group)

    return template

@click.command()
@click.argument('repo_name')
def get_name(repo_name):
    template = check_repo_name(repo_name)
    print(template)

if __name__ == '__main__':
    get_name()