import os
import argparse
from dataclasses import dataclass


@dataclass
class ToDoLine:
    todo_text: str
    line_number: int
    filepath: str


all_todos: list[ToDoLine] = []


def find_code_files(dirpath: str, file_type: str):
    with os.scandir(dirpath) as dir_iterator:
        for entry in dir_iterator:
            if entry.is_file():
                if entry.name.endswith(file_type):
                    find_todos(entry.path)
            elif not entry.name.startswith('.') and entry.is_dir():
                find_code_files(entry.path, file_type)


def find_todos(filepath: str):
    with open(filepath) as fd:
        line_index = 1
        for line in fd:
            if line.find('TODO') >= 0:
                add_new_todo(line_index, line, filepath)
            line_index += 1
    


def add_new_todo(line: int, text: str, file: str):
    new_todo = ToDoLine(line_number=line,
                        todo_text=text,
                        filepath=file)
    all_todos.append(new_todo)


def print_todo(todo_item: ToDoLine):
    print(f"\nIn file: {todo_item.filepath}, line {todo_item.line_number}:")
    print(f"\t{todo_item.line_number}| {todo_item.todo_text}")



arg_parser = argparse.ArgumentParser(description="Find all TODO notes in directory with code")
arg_parser.add_argument('dirpath', type=str, help='A directory with code (project)')
arg_parser.add_argument('ftype', type=str, help='A type of file (.py, .c, .cpp and etc.)')


def main():
    args = arg_parser.parse_args()
    if not os.path.exists(args.dirpath):
        print(f'{args.dirpath}: No such directory')
        return -1
    find_code_files(args.dirpath, args.ftype)
    for todo_line in all_todos:
        print_todo(todo_line)


if __name__ == '__main__':
    main()

