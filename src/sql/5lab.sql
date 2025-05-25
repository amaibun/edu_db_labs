SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema default_schema
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ODMS (Open Data Management System) 
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ODMS` ;

-- -----------------------------------------------------
-- Schema ODMS 
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ODMS` DEFAULT CHARACTER SET utf8 ;
USE `ODMS`;

-- -----------------------------------------------------
-- Enum DatasetStatus 
-- -----------------------------------------------------
CREATE TYPE DatasetStatus AS ENUM ('Draft', 'Published', 'Archived');

-- -----------------------------------------------------
-- Enum UserRole 
-- -----------------------------------------------------
CREATE TYPE UserRole AS ENUM ('Admin', "Publisher", "Viewer");

-- -----------------------------------------------------
-- Table `ODMS`.`Dataset`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Lab4`.`Dataset` ;

CREATE TABLE IF NOT EXISTS `Lab4`.`Dataset` (
    id UUID PRIMARY KEY,
    title VARCHAR (220) NOT NULL,
    description TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    format VARCHAR (256) NOT NULL,
    license VARCHAR (256) NOT NULL,
    status DatasetStatus NOT NULL,
    organization_id UUID REFERENCES Organization(id),
    category_id UUID REFERENCES Category(id), 
    user_id UUID REFERENCES User(id)
);

 
-- -----------------------------------------------------
-- Table `ODMS`.`Organization`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Lab4`.`Organization`;

CREATE TABLE IF NOT EXISTS `Lab4`.`Organization` (
    id UUID PRIMARY KEY,
    name VARCHAR (256) NOT NULL,
    description TEXT NOT NULL,
    contact_email VARCHAR (256) NOT NULL,
    website VARCHAR (256) NOT NULL,
);

-- -----------------------------------------------------
-- Table `ODMS`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Lab4`.`Category`;

CREATE TABLE IF NOT EXISTS `Lab4`.`Category` (
    id UUID PRIMARY KEY,
    name VARCHAR (256) NOT NULL,
);

-- -----------------------------------------------------
-- Table `ODMS`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Lab4`.`User`;

CREATE TABLE IF NOT EXISTS `Lab4`.`User` (
    id UUID PRIMARY KEY,
    username VARCHAR (256) NOT NULL,
    email VARCHAR (256) NOT NULL,
    role UserRole NOT NULL,
);

-- -----------------------------------------------------
-- Table `ODMS`.`DatasetTag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Lab4`.`DatasetTag`;


CREATE TABLE IF NOT EXISTS `Lab4`.`DatasetTag` (
    dataset_id UUID PRIMARY KEY,
    tag_id UUID REFERENCES Tag(id), 
);

-- -----------------------------------------------------
-- Table `ODMS`.`Tag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Lab4`.`Tag`;

CREATE TABLE IF NOT EXISTS `Lab4`.`Tag` (
    id UUID PRIMARY KEY,
    name VARCHAR (256) NOT NULL, 
);

-- -----------------------------------------------------
-- Table `ODMS`.`DataResource`
-- -----------------------------------------------------
DROP TABLE IF NOT EXISTS `Lab4`.`DataResource`;

DROP TABLE IF EXISTS `Lab4`.`DataResource`;
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
-- Table `ODMS`.`AccessLog`
-- -----------------------------------------------------
DROP TABLE IF NOT EXISTS `Lab4`.`AccessLog`;

CREATE TABLE IF NOT EXISTS `Lab4`.`AccessLog` (
    id UUID PRIMARY KEY,
    accessed_at DATETIME NOT NULL,
    user_id UUID REFERENCES User(id),
    dataset_id UUID REFERENCES Dataset(id),
);

-- -----------------------------------------------------
-- Start data 
-- -----------------------------------------------------

INSERT INTO "Lab4"."Organization" (id, name, description, contact_email, website) VALUES
  ('11111111-1111-1111-1111-111111111111', 'OpenGov', 'Open government data portal', 'info@opengov.org', 'https://opengov.org'),
  ('22222222-2222-2222-2222-222222222222', 'DataWorld', 'Global data sharing platform', 'contact@dataworld.io', 'https://dataworld.io');

INSERT INTO "Lab4"."User" (id, username, email, role) VALUES
  ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'alice', 'alice@example.com', 'Admin'),
  ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', 'bob', 'bob@example.com', 'Publisher'),
  ('cccccccc-cccc-cccc-cccc-cccccccccccc', 'carol', 'carol@example.com', 'Viewer');

INSERT INTO "Lab4"."Category" (id, name) VALUES
  ('33333333-3333-3333-3333-333333333333', 'Healthcare'),
  ('44444444-4444-4444-4444-444444444444', 'Transportation');

INSERT INTO "Lab4"."Tag" (id, name) VALUES
  ('55555555-5555-5555-5555-555555555555', 'open'),
  ('66666666-6666-6666-6666-666666666666', 'csv'),
  ('77777777-7777-7777-7777-777777777777', 'api');

INSERT INTO "Lab4"."Dataset" (
  id, title, description, created_at, updated_at, format, license, status,
  organization_id, category_id, user_id
) VALUES
  ('88888888-8888-8888-8888-888888888888',
   'COVID-19 Statistics 2024', 'Up-to-date statistics on COVID-19 cases and vaccination rates', 
   '2024-01-01 10:00:00', '2024-02-01 12:00:00', 'CSV', 'ODC-BY', 'Published',
   '11111111-1111-1111-1111-111111111111', '33333333-3333-3333-3333-333333333333', 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'
  );

INSERT INTO "Lab4"."DatasetTag" (dataset_id, tag_id) VALUES
  ('88888888-8888-8888-8888-888888888888', '55555555-5555-5555-5555-555555555555'),
  ('88888888-8888-8888-8888-888888888888', '66666666-6666-6666-6666-666666666666');

INSERT INTO "Lab4"."AccessLog" (
  id, accessed_at, user_id, dataset_id
) VALUES
  ('aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee',
   '2025-05-20 14:30:00', 'cccccccc-cccc-cccc-cccc-cccccccccccc', '88888888-8888-8888-8888-888888888888');
