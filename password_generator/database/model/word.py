from sqlalchemy import Column, Integer, String
from password_generator.database.database import Base


class Word(Base):
    __tablename__ = 'words'
    word = Column(String(50), unique=True, primary_key=True)
    length = Column(Integer)

    def __init__(self, word):
        self.word = word
        self.length = len(word)

    def __repr__(self):
        return '<Word %r>' % self.word
