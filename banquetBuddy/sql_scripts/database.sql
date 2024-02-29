DROP TABLE IF EXISTS TaskEmployee CASCADE;
DROP TABLE IF EXISTS Offer CASCADE;
DROP TABLE IF EXISTS EmployeeWorkService CASCADE;
DROP TABLE IF EXISTS Review CASCADE;
DROP TABLE IF EXISTS Menu CASCADE;
DROP TABLE IF EXISTS Task CASCADE;
DROP TABLE IF EXISTS Event CASCADE;
DROP TABLE IF EXISTS CateringService CASCADE;
DROP TABLE IF EXISTS Message CASCADE;
DROP TABLE IF EXISTS JobApplication CASCADE;
DROP TABLE IF EXISTS Employee CASCADE;
DROP TABLE IF EXISTS CateringCompany CASCADE;
DROP TABLE IF EXISTS Particular CASCADE;
DROP TABLE IF EXISTS "User" CASCADE;

DROP TYPE IF EXISTS bookingState;
DROP TYPE IF EXISTS Priority;
DROP TYPE IF EXISTS ApplicationState;
DROP TYPE IF EXISTS PricePlan;
DROP TYPE IF EXISTS AssignmentState;


CREATE TYPE AssignmentState AS ENUM ('PENDING', 'IN_PROGRESS', 'COMPLETED');

CREATE TYPE PricePlan AS ENUM ('BASE', 'PREMIUM', 'PREMIUM_PRO', 'NO_SUBSCRIBED');

CREATE TYPE ApplicationState AS ENUM ('PENDING', 'IN_REVIEW', 'ACCEPTED');

CREATE TYPE Priority AS ENUM ('LOW', 'MEDIUM', 'HIGH');

CREATE TYPE bookingState AS ENUM ('CONFIRMED', 'CONTRACT_PENDING', 'CANCELLED');



CREATE TABLE "User" (
    username VARCHAR PRIMARY KEY,
    password VARCHAR  NOT NULL,
    email VARCHAR UNIQUE,
    first_name VARCHAR,
    last_name VARCHAR, 
    phone_number VARCHAR UNIQUE
);


CREATE TABLE Particular (
    username VARCHAR PRIMARY KEY REFERENCES "User"(username),
    preferences VARCHAR,
    address VARCHAR,
    is_subscribed Boolean
);


CREATE TABLE CateringCompany (
    username VARCHAR PRIMARY KEY REFERENCES "User"(username),
    name VARCHAR,
    service_description VARCHAR,
    logo BYTEA,
    cuisine_type VARCHAR[],
    is_verified BOOLEAN,
    price_plan PricePlan
);


CREATE TABLE Employee (
    username VARCHAR PRIMARY KEY REFERENCES "User"(username),
    profession VARCHAR,
    experience VARCHAR,
    skills VARCHAR,
    location VARCHAR,
    curriculum BYTEA,
    recommendation_letter BYTEA
);




CREATE TABLE Message (
    id SERIAL PRIMARY KEY,
    sender VARCHAR REFERENCES "User"(username),
    receiver VARCHAR REFERENCES "User"(username),
    date DATE,
    content VARCHAR,
    CHECK(sender <> receiver)
);



CREATE TABLE CateringService (
    id SERIAL PRIMARY KEY,
    cateringcompany_username VARCHAR REFERENCES CateringCompany(username), 
    name VARCHAR,
    description VARCHAR,
    location VARCHAR,
    capacity INTEGER, 
    price NUMERIC 
);

CREATE TABLE Event (
    id SERIAL PRIMARY KEY,
    cateringservice_id INTEGER REFERENCES CateringService(id),
    particular_username VARCHAR REFERENCES Particular(username),
    name VARCHAR,
    date DATE,
    details VARCHAR,
    booking_state bookingState, 
    numberGuests INTEGER
);

CREATE TABLE Task (
    id SERIAL PRIMARY KEY,
    event_id Integer REFERENCES Event(id),
    cateringservice_id Integer REFERENCES CateringService(id), 
    description VARCHAR,
    assignment_date DATE,
    assignment_state AssignmentState, 
    expiration_date DATE,
    priority Priority,
    CHECK(assignment_date < expiration_date)
);

CREATE TABLE Menu (
    id SERIAL PRIMARY KEY,
    cateringservice_id INTEGER REFERENCES CateringService(id), 
    name VARCHAR,
    description VARCHAR,
    price NUMERIC, 
    plates VARCHAR[], 
    diet_restrictions VARCHAR
);

CREATE TABLE Review (
    id SERIAL PRIMARY KEY,
    particular_username VARCHAR REFERENCES Particular(username), 
    cateringservice_id INTEGER REFERENCES CateringService(id), 
    rating INTEGER, 
    description VARCHAR,
    date DATE, 
    CHECK (rating >=1 AND rating <=5)
);

CREATE TABLE EmployeeWorkService (
    id SERIAL PRIMARY KEY,
    employee_username VARCHAR REFERENCES Employee(username), 
    cateringservice_id INTEGER REFERENCES CateringService(id) 
);    


CREATE TABLE Offer (
    id SERIAL PRIMARY KEY,
    cateringservice_id INTEGER REFERENCES CateringService(id), 
    title VARCHAR,
    description VARCHAR,
    requirements VARCHAR,
    location VARCHAR
);

CREATE TABLE JobApplication (
    id SERIAL PRIMARY KEY,
    employee_username VARCHAR REFERENCES Employee(username), 
    offer_id INTEGER REFERENCES Offer(id),
    date_application DATE,
    state ApplicationState 
);


CREATE TABLE TaskEmployee(
    id SERIAL PRIMARY KEY,
    employee_username VARCHAR REFERENCES Employee(username),
    task_id Integer REFERENCES Task(id)
); 


