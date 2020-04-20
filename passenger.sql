CREATE TABLE passenger(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flight
);


INSERT INTO passenger(id, name, flight_id) VALUES (1,'alice',1);
INSERT INTO passenger(id, name, flight_id) VALUES (2,'bob',1);
INSERT INTO passenger(id, name, flight_id) VALUES (3,'charlie',2);
INSERT INTO passenger(id, name, flight_id) VALUES (4,'dave',2);
INSERT INTO passenger(id, name, flight_id) VALUES (5,'erin',4);
INSERT INTO passenger(id, name, flight_id) VALUES (6,'frank',6);
INSERT INTO passenger(id, name, flight_id) VALUES (7,'grace',6);
