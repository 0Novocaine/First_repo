import pathlib
from typing import Any


def get_cats_info(path: pathlib) -> list[dict[str, int | Any]] | None:
    try:
        with open(path, "r", ) as file:
            cats = file.readlines()
            result = []
            for cat in cats:
                cat_id, cat_name, cat_age = cat.split(",")
                cat_age = int(cat_age)
                cat_dict = {
                    "Идентификатор котэ": cat_id,
                    "Имя котэ": cat_name,
                    "Возраст котэ": cat_age
                }
                result.append(cat_dict)
            return result
    except FileNotFoundError:
        print(f"There is no such file at this path: {path}")
        return None


current_dir = pathlib.Path(__file__).parent / "cats.txt"
print(get_cats_info(current_dir))
