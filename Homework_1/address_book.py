from collections import UserDict
from record import Record


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name, None)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())