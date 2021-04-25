CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT);
CREATE TABLE substances(id SERIAL PRIMARY KEY, name TEXT, target TEXT, mechanism TEXT, metabolism TEXT, eff_duration TEXT, notes TEXT, risks TEXT, visible BOOLEAN);
CREATE TABLE interactions(id SERIAL PRIMARY KEY, description TEXT);
CREATE TABLE substanceInteraction(
substance_id INTEGER,
interaction_id INTEGER,
CONSTRAINT fk_substance
FOREIGN KEY(substance_id)
REFERENCES substances(id),
CONSTRAINT fk_interaction
FOREIGN KEY(interaction_id)
REFERENCES interactions(id)
);
CREATE TABLE classes(id SERIAL PRIMARY KEY, name TEXT, risks TEXT);
CREATE TABLE moas(
id SERIAL PRIMARY KEY,
class_id INTEGER,
target TEXT,
effect TEXT,
CONSTRAINT fk_class
FOREIGN KEY(class_id)
REFERENCES classes(id)
);
CREATE TABLE substanceMoa(
substance_id INTEGER,
moa_id INTEGER,
CONSTRAINT fk_substance
FOREIGN KEY(substance_id)
REFERENCES substances(id),
CONSTRAINT fk_moa
FOREIGN KEY(moa_id)
REFERENCES moas(id)
);
CREATE TABLE indications(id SERIAL PRIMARY KEY, name TEXT, type TEXT);
CREATE TABLE substanceIndication(
substance_id INTEGER,
indication_id INTEGER,
route TEXT,
notes TEXT,
CONSTRAINT fk_substance
FOREIGN KEY(substance_id)
REFERENCES substances(id),
CONSTRAINT fk_indication
FOREIGN KEY(indication_id)
REFERENCES indications(id)
);
