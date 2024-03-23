-- CREATE TABLE fosters(
-- foster_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- foster_status VARCHAR (20) NOT NULL,
-- foster_address VARCHAR (50) NOT NULL,
-- pet_preference VARCHAR (20) NOT NULL,
-- foster_tel VARCHAR (10) NOT NULL,
-- start_period DATE NOT NULL,
-- end_period DATE NOT NULL
-- )

-- CREATE TABLE pets (
-- pet_id SERIAL PRIMARY KEY,
-- pet_type VARCHAR (20) NOT NULL,
-- pet_name VARCHAR (50) NOT NULL,
-- breed VARCHAR (50) NOT NULL,
-- pet_status VARCHAR (50) NOT NULL,
-- shelter_address VARCHAR (50) NOT NULL,
-- shelter_tel VARCHAR (10) NOT NULL,
-- start_period DATE NOT NULL,
-- end_period DATE NOT NULL
-- )


-- CREATE TABLE care(
-- care_id SERIAL PRIMARY KEY,
-- pet_id INTEGER NOT NULL,
-- foster_id INTEGER NOT NULL,
-- start_period DATE NOT NULL,
-- end_period DATE NOT NULL,
-- FOREIGN KEY (pet_id) REFERENCES pets(pet_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- FOREIGN KEY (foster_id) REFERENCES fosters(foster_id) ON DELETE CASCADE ON UPDATE CASCADE)



