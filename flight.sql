CREATE TABLE flight(
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);



INSERT INTO flight (id, origin, destination, duration) VALUES (1,'new york','london', 415);
INSERT INTO flight (id, origin, destination, duration) VALUES (2,'shanghai','paris', 760);
INSERT INTO flight(id, origin, destination, duration) VALUES (3,'istanbul','tokyo', 700);
INSERT INTO flight(id, origin, destination, duration) VALUES (4,'new york','paris', 435);
INSERT INTO flight(id, origin, destination, duration) VALUES (5,'moscow','paris',245);
INSERT INTO flight(id, origin, destination, duration) VALUES (6,'shanghai','new york', 455);
