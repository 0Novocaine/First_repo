import re


def normalize_phone(phone_number):
    normalize_phone_number = re.sub(r"[^\d+]", "", phone_number)
    if normalize_phone_number.startswith("+380") and len(normalize_phone_number) == 13:
        return normalize_phone_number
    if normalize_phone_number.startswith("380") and len(normalize_phone_number) == 12:
        return "+" + normalize_phone_number
    elif normalize_phone_number.startswith("0") and len(normalize_phone_number) == 10:
        return "+38" + normalize_phone_number

    return None

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "sdfsdf1231"
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
phone = "0559820922"
print(sanitized_numbers)
