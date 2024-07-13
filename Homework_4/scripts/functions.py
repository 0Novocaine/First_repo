import re


def normalize_phone(phone_number: str) -> str:
    normalize_phone_number = re.sub(r"[^\d+]", "", phone_number)
    if normalize_phone_number.startswith("+380") and len(normalize_phone_number) == 13:
        return normalize_phone_number
    if normalize_phone_number.startswith("380") and len(normalize_phone_number) == 12:
        return "+" + normalize_phone_number
    elif normalize_phone_number.startswith("0") and len(normalize_phone_number) == 10:
        return "+38" + normalize_phone_number
    else:
        return "Неверный номер телефона"


def to_lowercase(strings: str) -> list:
    return [s.lower() for s in strings]
