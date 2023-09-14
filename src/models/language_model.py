from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict = {}):
        super().__init__(data)

    # Req. 2
    def to_dict(self):
        language_name = self.data["name"]
        language_acronym = self.data["acronym"]
        return {"name": language_name, "acronym": language_acronym}

    # Req. 3
    @classmethod
    def list_dicts(cls):
        return [language.to_dict() for language in cls.find()]
