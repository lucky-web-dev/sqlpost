import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine("postgres://postgres:happy!@#123@localhost:5432/postgres", echo=True)
db=scoped_session(sessionmaker(bind=engine))
def main():
    f=open("flights.csv")
    reader=csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flightS (origin, destination, duration) VALUES (:origin,:destination,:duration)",{"origin":origin,"destination":destination,"duration":duration})
        print(f"Added flight from {origin} to {destiantion} during {duration} ")
    db.commit()

if __name__=="__name__":
    main()
