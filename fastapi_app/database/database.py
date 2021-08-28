from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlmodel import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:superrootPassword987@localhost:5432/unite"

# Create the SQLAlchemy engine.
# echo=True --> To show all DB sentences in the console.
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
