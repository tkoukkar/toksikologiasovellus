CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT);
CREATE TABLE substances(id SERIAL PRIMARY KEY, name TEXT, target TEXT, mechanism TEXT, metabolism TEXT, eff_duration TEXT, notes TEXT, risks TEXT);
CREATE TABLE interactions(id SERIAL PRIMARY KEY, description TEXT)
CREATE TABLE substanceInteraction
(
substance_id INTEGER,
interaction_id INTEGER,
CONSTRAINT fk_substance
FOREIGN KEY(substance_id)
REFERENCES substances(id),
CONSTRAINT fk_interaction
FOREIGN KEY(interaction_id)
REFERENCES interactions(id)
);
