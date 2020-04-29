import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine=create_engine("postgres://postgres:happy!@#123@localhost:5432/postgres", echo=True)
db=scoped_session(sessionmaker(bind=engine))
def main():
    flights= db.execute("SELECT id, origin, destination, duration FROM flight").fetchall()
    for fli in flights:
        print(f"Flight {fli.id}:{fli.origin} to {fli.destination}, {fli.duration} minutes.")
    flight_id= int(input("\nFlight ID:"))
    flight=db.execute("SELECT origin, destination, duration FROM flight WHERE id=:id", {"id":flight_id}).fetchone()
    if flight is None:
        print("Error:No such flight.")
        return
    passengers=db.execute("SELECT name,id  FROM passenger WHERE flight_id=:flight_id", {"flight_id":flight_id}).fetchall()
    print("\nPASSENGERS:")
    for passenger in passengers:
        print(passenger.name, passenger.id)
    if len(passenger.name)==0:
        print("No passenger.")

if __name__=='__main__':
    main()
