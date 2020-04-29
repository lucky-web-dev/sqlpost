import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine("postgres://postgres:happy!@#123@localhost:5432/postgres", echo=True)
db = scoped_session(sessionmaker(bind=engine))
def main():
    flights = db.execute("SELECT origin, destination, duration FROM flight").fetchall()
    for fli in flights:
        print(f"{fli.origin} to {fli.destination}, {fli.duration} minutes.")
if __name__ == "__main__":
    main()
