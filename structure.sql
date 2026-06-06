-- PLANNATE Database Structure

CREATE DATABASE user_name;
USE user_name;

CREATE TABLE JEE_TIME (
    subject VARCHAR(250),
    monday INT(4) NOT NULL,
    tuesday INT(4) NOT NULL,
    wednesday INT(4) NOT NULL,
    thursday INT(4) NOT NULL,
    friday INT(4) NOT NULL,
    saturday INT(4) NOT NULL,
    sunday INT(4) NOT NULL
);

CREATE TABLE JEE_SPEED (
    subject VARCHAR(250),
    monday INT(4) NOT NULL,
    tuesday INT(4) NOT NULL,
    wednesday INT(4) NOT NULL,
    thursday INT(4) NOT NULL,
    friday INT(4) NOT NULL,
    saturday INT(4) NOT NULL,
    sunday INT(4) NOT NULL
);

CREATE TABLE JEE_MARKS (
    date DATE,
    nques INT,
    c_phy INT,
    na_phy INT,
    in_phy INT,
    c_chem INT,
    na_chem INT,
    in_chem INT,
    c_maths INT,
    na_maths INT,
    in_maths INT,
    prcnt FLOAT
);