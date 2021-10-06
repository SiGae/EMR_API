from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import text, create_engine
from env import db_auth

engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(db_auth.get("account_id"),
                                                            db_auth.get("account_pw"),
                                                            db_auth.get("address"),
                                                            db_auth.get("port"),
                                                            db_auth.get("db")))

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
session = Session()

