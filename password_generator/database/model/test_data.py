from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from password_generator.database.database import Base


class TestData(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    uuid = Column(String(20))
    random_characters_password = Column(String(100))
    random_words_password = Column(String(100))
    song_password = Column(String(100))

    def __init__(self, uuid, random_characters_password, random_words_password, song_password):
        self.uuid = uuid
        self.random_characters_password = random_characters_password
        self.random_words_password = random_words_password
        self.song_password = song_password

    def __repr__(self):
        return '<UUID: %s>' % self.uuid
