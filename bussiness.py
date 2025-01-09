import uuid
from datetime import datetime

DATE_FORMAT = "%y/%m/%d %H:%M:%S"

class NotesEntity:
    def __init__(self, id: str, date: str, header: str, text: str):
        self.id = id
        self.date = date
        self.header = header
        self.text = text

    def to_db_dto(self) -> dict:
        return {
            "_id": self.id,
            "header": self.header,
            "date": self.date,
            "text": self.text
        }

    def to_web_dto(self) -> dict:
        return {
            "id": self.id,
            "header": self.header,
            "date": self.date,
            "text": self.text
        }

def note_from_web_dto(note_dto: dict) -> NotesEntity:
    if "id" in note_dto and "header" in note_dto and "date" in note_dto and "text" in note_dto:
        return NotesEntity(note_dto.get('id'), note_dto.get('date'), note_dto.get('header'), note_dto.get('text'))
    else:
        raise Exception("Note parsing failed")

def new_note_from_web_dto(note_dto: dict) -> NotesEntity:
    if "header" in note_dto and "text" in note_dto:
        return NotesEntity(str(uuid.uuid1()), datetime.now().strftime(DATE_FORMAT), note_dto.get('header'), note_dto.get('text'))
    else:
        raise Exception("Note parsing failed")

def note_from_db_dto(note_dto: dict) -> NotesEntity:
    if "_id" in note_dto and "header" in note_dto and "date" in note_dto and "text" in note_dto:
        return NotesEntity(note_dto.get('_id'), note_dto.get('date'), note_dto.get('header'), note_dto.get('text'))
    else:
        raise Exception("Note parsing failed")
