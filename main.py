import os
import argparse
from dataclasses import dataclass


@dataclass
class ToDoLine:
    todo_text: str
    line_number: int
    filepath: str


all_todos: list[ToDoLine] = []


def find_todos(dirpath: str):
    pass


def add_new_todo(line: int, text: str, file: str):
    pass


def print_todo(todo_item: ToDoLine):
    pass


arg_parser = argparse.ArgumentParser(description="Find all TODO notes in directory with code")
arg_parser.add_argument('dirpath', type=str, help='A directory with code (project)')
arg_parser.add_argument('file-type', type=str, help='A type of file (.py, .c, .cpp and etc.)')


def main():
    arg_parser.parse_args()

if __name__ == '__main__':
    main()

