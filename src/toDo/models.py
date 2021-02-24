from sqlalchemy import (
                        create_engine, 
                        Column, 
                        Integer,
                        String,
                        Sequence,

                    )
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sqlite.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_name = Column(String)


class ToDoItem(Base):
    __tablename__ = 'todoItem'

    item_id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    title = Column(String)
    description = Column(String)
    # due_date = 
    # priority = 

if __name__ == '__main__':
    Base.metadata.create_all(engine)