-- -----------------------------------------------------
-- Schema default_schema
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ODMS (Open Data Management System) 
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS "ODMS" ;

-- -----------------------------------------------------
-- Schema ODMS 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS "ODMS";
SET search_path TO "ODMS";

-- -----------------------------------------------------
-- Enum DatasetStatus 
-- -----------------------------------------------------
CREATE TYPE DatasetStatus AS ENUM ('Draft', 'Published', 'Archived');

-- -----------------------------------------------------
-- Enum UserRole 
-- -----------------------------------------------------
CREATE TYPE UserRole AS ENUM ('Admin', 'Publisher', 'Viewer');

-- -----------------------------------------------------
-- Table "ODMS"."Organization"
-- -----------------------------------------------------
DROP TABLE IF EXISTS Organization;

CREATE TABLE IF NOT EXISTS Organization (
    id UUID PRIMARY KEY,
    name VARCHAR (256) NOT NULL,
    description TEXT NOT NULL,
    contact_email VARCHAR (256) NOT NULL,
    website VARCHAR (256) NOT NULL
);

-- -----------------------------------------------------
-- Table "ODMS"."Category"
-- -----------------------------------------------------
DROP TABLE IF EXISTS Category;

CREATE TABLE IF NOT EXISTS Category (
    id UUID PRIMARY KEY,
    name VARCHAR (256) NOT NULL
);

-- -----------------------------------------------------
-- Table "ODMS"."User"
-- -----------------------------------------------------
DROP TABLE IF EXISTS ODMS_User;

CREATE TABLE IF NOT EXISTS ODMS_User (
    id UUID PRIMARY KEY,
    username VARCHAR (256) NOT NULL,
    email VARCHAR (256) NOT NULL,
    role UserRole NOT NULL
);

-- -----------------------------------------------------
-- Table "ODMS"."Tag"
-- -----------------------------------------------------
DROP TABLE IF EXISTS Tag;

CREATE TABLE IF NOT EXISTS Tag (
    id UUID PRIMARY KEY,
    name VARCHAR (256) NOT NULL
);

-- -----------------------------------------------------
-- Table "ODMS"."DatasetTag"
-- -----------------------------------------------------
DROP TABLE IF EXISTS DatasetTag;

CREATE TABLE IF NOT EXISTS DatasetTag (
    dataset_id UUID PRIMARY KEY,
    tag_id UUID REFERENCES Tag(id) 
);

-- -----------------------------------------------------
-- Table "ODMS"."Dataset"
-- -----------------------------------------------------
DROP TABLE IF EXISTS Dataset ;

CREATE TABLE IF NOT EXISTS Dataset (
    id UUID PRIMARY KEY,
    title VARCHAR (219) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    format VARCHAR (255) NOT NULL,
    license VARCHAR (255) NOT NULL,
    status DatasetStatus NOT NULL,
    organization_id UUID REFERENCES Organization(id),
    category_id UUID REFERENCES Category(id), 
    user_id UUID REFERENCES ODMS_User(id)
);

-- -----------------------------------------------------
-- Table "ODMS"."DataResource"
-- -----------------------------------------------------
DROP TABLE IF EXISTS DataResource;

DROP TABLE IF EXISTS DataResource;
CREATE TABLE IF NOT EXISTS DataResource (
    id UUID PRIMARY KEY,
    file_name VARCHAR NOT NULL,
    file_type VARCHAR NOT NULL,
    size INTEGER NOT NULL,
    url VARCHAR NOT NULL,
    uploaded_at TIMESTAMP NOT NULL,
    dataset_id UUID REFERENCES Dataset(id)
);

-- -----------------------------------------------------
-- Table "ODMS"."AccessLog"
-- -----------------------------------------------------
DROP TABLE IF EXISTS AccessLog;

CREATE TABLE IF NOT EXISTS AccessLog (
    id UUID PRIMARY KEY,
    accessed_at TIMESTAMP NOT NULL,
    user_id UUID REFERENCES ODMS_User(id),
    dataset_id UUID REFERENCES Dataset(id)
);

-- -----------------------------------------------------
-- Start data 
-- -----------------------------------------------------

INSERT INTO Organization (id, name, description, contact_email, website) VALUES
  ('11111111-1111-1111-1111-111111111111', 'OpenGov', 'Open government data portal', 'info@opengov.org', 'https://opengov.org'),
  ('22222222-2222-2222-2222-222222222222', 'DataWorld', 'Global data sharing platform', 'contact@dataworld.io', 'https://dataworld.io');

INSERT INTO ODMS_User (id, username, email, role) VALUES
  ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'alice', 'alice@example.com', 'Admin'),
  ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 'bob', 'bob@example.com', 'Publisher'),
  ('cccccccc-cccc-cccc-cccc-cccccccccccc', 'carol', 'carol@example.com', 'Viewer');

INSERT INTO Category (id, name) VALUES
  ('33333333-3333-3333-3333-333333333333', 'Healthcare'),
  ('44444444-4444-4444-4444-444444444444', 'Transportation');

INSERT INTO Tag (id, name) VALUES
  ('55555555-5555-5555-5555-555555555555', 'open'),
  ('66666666-6666-6666-6666-666666666666', 'csv'),
  ('77777777-7777-7777-7777-777777777777', 'api');

INSERT INTO Dataset (
  id, title, description, created_at, updated_at, format, license, status,
  organization_id, category_id, user_id
) VALUES
  ('88888888-8888-8888-8888-888888888888',
   'COVID-19 Statistics 2024', 'Up-to-date statistics on COVID-19 cases and vaccination rates', 
   '2024-01-01 10:00:00', '2024-02-01 12:00:00', 'CSV', 'ODC-BY', 'Published',
   '11111111-1111-1111-1111-111111111111', '33333333-3333-3333-3333-333333333333', 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'
  );

INSERT INTO DatasetTag (dataset_id, tag_id) VALUES
  ('88888888-8888-8888-8888-888888888888', '55555555-5555-5555-5555-555555555555'),
  ('22222222-2222-2222-2222-222222222222', '66666666-6666-6666-6666-666666666666');

INSERT INTO AccessLog (
  id, accessed_at, user_id, dataset_id
) VALUES
  ('aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
   '2025-05-20 14:30:00', 'cccccccc-cccc-cccc-cccc-cccccccccccc', '88888888-8888-8888-8888-888888888888');
