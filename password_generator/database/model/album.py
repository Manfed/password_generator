from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

from password_generator.database.database import Base


class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    artist = Column(String(50))
    albums = Column(String(1000))

    def __init__(self, artist, albums):
        self.artist = artist
        self.albums = albums

    def __repr__(self):
        return '<Album %r>' % self.artist
