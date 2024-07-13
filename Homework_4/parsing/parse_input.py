from typing import Any
from scripts import to_lowercase


def parse_input(user_input: str) -> tuple[Any, list[Any]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = to_lowercase(args)
    return cmd, args
