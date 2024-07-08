import os
import sys
import pathlib
from colorama import init, Fore

init(autoreset=True)
FOLDER_ICON = chr(128193)
FILE_ICON = chr(128196)


def directory_tree(path: str, deep=0):
    try:
        attachments = os.listdir(path)
    except FileNotFoundError:
        print(f"Директория {path} не существует.")
        return
    except PermissionError:
        print(f"Нет доступа к {path}.")
        return
    for attachment in attachments:
        full_path = os.path.join(path, attachment)
        if os.path.isdir(full_path):
            print("    " * deep + FOLDER_ICON + Fore.LIGHTYELLOW_EX + f" DIR: {attachment}")
            directory_tree(full_path, deep + 1)
        elif os.path.isfile(full_path):
            print("    " * deep + FILE_ICON + Fore.LIGHTMAGENTA_EX + f" File: {attachment}")
    return


def main():
    if len(sys.argv) != 2:
        print("Пример запуска: python script.py \"путь к директории\"")
        sys.exit()
    input_path = sys.argv[1]
    directory = pathlib.Path(input_path)
    if not directory.is_dir():
        print(f"Директория '{input_path}' указана некорректно.")
        sys.exit()

    directory_tree(input_path)


if __name__ == "__main__":
    main()
