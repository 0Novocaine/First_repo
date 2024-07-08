from scripts import normalize_phone


def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Ведите два аргумента: пользователь и номер телефона."
    name, phone = args
    contacts[name] = normalize_phone(phone)
    return "Контакт добавлен."


def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Ведите два аргумента: пользователь и номер телефона."
    name, phone = args
    if name in contacts:
        contacts[name] = normalize_phone(phone)
        return "Контакт обновлен."
    else:
        return "Такой контакт отсутствует."


def show_phone(args: list, contacts: dict) -> str:
    if len(args) != 1:
        return "Введите имя пользователя, чей телефон вы хотите узнать."
    name = args[0]
    if name in contacts:
        return f"У {name.capitalize()} следующий номер телефона: {contacts[name]}."
    else:
        return "Error: Contact not found."


def show_all(contacts: dict) -> str:
    if not contacts:
        return "Контакты отсутствуют."
    contact_list = [f"{name.capitalize()}: {phone}" for name, phone in contacts.items()]
    return "\n".join(contact_list)
