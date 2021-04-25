DROP TABLE IF EXISTS substanceInteraction;
DROP TABLE IF EXISTS substanceIndication;
DROP TABLE IF EXISTS substanceMoa;
DROP TABLE IF EXISTS substances;
DROP TABLE IF EXISTS interactions;
DROP TABLE IF EXISTS indications;
DROP TABLE IF EXISTS moas;
DROP TABLE IF EXISTS classes;
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT);
CREATE TABLE classes(id SERIAL PRIMARY KEY, name TEXT, risks TEXT);
CREATE TABLE substances(
id SERIAL PRIMARY KEY,
class_id INTEGER,
name TEXT,
target TEXT,
mechanism TEXT,
metabolism TEXT,
eff_duration TEXT,
notes TEXT,
risks TEXT,
visible BOOLEAN,
CONSTRAINT fk_class
FOREIGN KEY(class_id)
REFERENCES classes(id)
);
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
INSERT INTO classes(
name, risks)
VALUES ('muut lääkeaineet', '');

INSERT INTO classes(
name, risks)
VALUES ('parasympatomimeetit', '');

INSERT INTO classes(
name, risks)
VALUES ('antikolinergit', '');

INSERT INTO classes(
name, risks)
VALUES ('katekoliamiinit', '');

INSERT INTO classes(
name, risks)
VALUES ('sympatomimeetit', '');

INSERT INTO classes(
name, risks)
VALUES ('sympatolyytit', '');

INSERT INTO classes(
name, risks)
VALUES ('triptaanit', '');

INSERT INTO classes(
name, risks)
VALUES ('antihistamiinit', '');

INSERT INTO classes(
name, risks)
VALUES ('kortikosteroidit', '');

INSERT INTO classes(
name, risks)
VALUES ('närästys-, ulkus- ja refluksilääkkeet', '');

INSERT INTO classes(
name, risks)
VALUES ('tulehduskipulääkkeet', '');

INSERT INTO classes(
name, risks)
VALUES ('opioidit', 'pahoinvointi, oksentelu, ummetus; histamiinin vapautuminen, kutina; väsymys, keskittymisvaikeudet; riippuvuus, vieroitusoireet (hikoilu, pahoinvointi, vapina, lihaskivut, dysforia)');

INSERT INTO moas(
class_id, target, effect)
VALUES (2, 'muskariinireseptorit', 'agonismi');

INSERT INTO moas(
class_id, target, effect)
VALUES (2, 'koliiniesteraasit', 'esto');

INSERT INTO moas(
class_id, target, effect)
VALUES (3, 'muskariinireseptorit', 'salpaus');

INSERT INTO moas(
class_id, target, effect)
VALUES (4, 'dopamiinireseptorit', 'agonismi');

INSERT INTO moas(
class_id, target, effect)
VALUES (4, 'adrenergiset reseptorit', 'agonismi');

INSERT INTO moas(
class_id, target, effect)
VALUES (5, 'adrenergiset reseptorit', 'epäsuora agonismi');

INSERT INTO moas(
class_id, target, effect)
VALUES (5, 'β₁', 'agonismi');

INSERT INTO moas(
class_id, target, effect)
VALUES (5, 'β₂', 'agonismi');

INSERT INTO moas(
class_id, target, effect)
VALUES (6, 'α₁', 'salpaus');

INSERT INTO moas(
class_id, target, effect)
VALUES (6, 'α₂', 'salpaus');

INSERT INTO moas(
class_id, target, effect)
VALUES (6, 'β₁', 'salpaus');

INSERT INTO moas(
class_id, target, effect)
VALUES (6, 'β₂', 'salpaus');

INSERT INTO moas(
class_id, target, effect)
VALUES (6, 'β₃', 'salpaus');

INSERT INTO moas(
class_id, target, effect)
VALUES (6, 'β₂', 'osittaisagonismi');

INSERT INTO indications(
name, type)
VALUES ('myasthenia gravis', 'muut');

INSERT INTO indications(
name, type)
VALUES ('myrkytykset', 'muut');

INSERT INTO indications(
name, type)
VALUES ('matkapahoinvointi', 'muut');

INSERT INTO indications(
name, type)
VALUES ('glaukooma', 'silmät');

INSERT INTO indications(
name, type)
VALUES ('ahdaskulmaglaukooma', 'silmät');

INSERT INTO indications(
name, type)
VALUES ('mydriaattina ja sykloplegiittinä', 'silmät');

INSERT INTO indications(
name, type)
VALUES ('silmätulehdukset', 'silmät');

INSERT INTO indications(
name, type)
VALUES ('hypotensio', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('hypertensio', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('bradykardia', 'sydän ja verisuonet');
 
INSERT INTO indications(
name, type)
VALUES ('takykardia', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('rytmihäiriöt', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('sydämen vajaatoiminta', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('sydänpysähdys', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('sepelvaltimotauti', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('angina pectoris', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('sydäninfarkti', 'sydän ja verisuonet');

INSERT INTO indications(
name, type)
VALUES ('yskä', 'hengitystiet');

INSERT INTO indications(
name, type)
VALUES ('krooninen bronkiitti', 'hengitystiet');

INSERT INTO indications(
name, type)
VALUES ('astma', 'hengitystiet');

INSERT INTO indications(
name, type)
VALUES ('keuhkoahtaumatauti', 'hengitystiet');
