from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings

import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER", "postgres")
password = os.getenv("DB_PASSWORD", "postgres")
server = os.getenv("DB_HOST", "localhost:5432")
db = os.getenv("DB_NAME", "postgres")
connection_string = f"postgresql://{user}:{password}@{server}/{db}"

# if os.environ.get('DATABASE_URL'):
#     connection_string = os.environ.get('DATABASE_URL')

engine = create_engine(connection_string, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
