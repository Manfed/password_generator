from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from password_generator.utils.constants import DATABASE_INIT_FILE_PATH, MINIMAL_RANDOM_WORD_LENGTH

engine = create_engine('sqlite:///../generator.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from password_generator.database.model.word import Word
    import password_generator.database.model
    Base.metadata.create_all(bind=engine)

    if Word.query.first() == None:
        __init_db_from_file()


def __init_db_from_file():
    from password_generator.database.model.word import Word
    with open(DATABASE_INIT_FILE_PATH) as file:
        for line in file:
            word = line.strip()
            if len(word) >= MINIMAL_RANDOM_WORD_LENGTH:
                db_session.add(Word(word))
        db_session.commit()
