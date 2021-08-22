from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:superrootPassword987@localhost:5432/unite"

# Create the SQLAlchemy engine.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# Each instance of the SessionLocal class will be a database session. The class itself is not a database session yet.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We will inherit from this class (Base) to create each of the database models or classes (the ORM models).
# SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database.
# SQLAlchemy's "model" and Pydantic's "model" are different things.
Base = declarative_base()