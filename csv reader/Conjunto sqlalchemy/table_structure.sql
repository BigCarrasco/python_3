CREATE SCHEMA ACADEMY;

USE ACADEMY;

CREATE TABLE DEPARTMENT (
	DEPT_ID			INTEGER			PRIMARY KEY,
    DEPT_NM			VARCHAR(50),
    DATE_CREATED	TIMESTAMP,
    DATE_UPDATED	TIMESTAMP
);

CREATE TABLE POSITIONS (
	POS_ID			INTEGER			PRIMARY KEY,
    POS_NM			VARCHAR(100),
    DATE_CREATED	TIMESTAMP,
    DATE_UPDATED	TIMESTAMP
);

CREATE TABLE EMPLOYEE (
	EMP_ID		INTEGER			PRIMARY KEY,
    DEPT_ID 	INTEGER,
    POS_ID  	INTEGER,
    LAST_NAME	VARCHAR(100),
    FIRST_NAME	VARCHAR(100),
    EMAIL		VARCHAR(100),
    MANAGER_ID	INTEGER,
    DATE_CREATED	TIMESTAMP,
    DATE_UPDATED	TIMESTAMP,
    CONSTRAINT EMP_DEPT_FK FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(DEPT_ID),
    CONSTRAINT EMP_POS_FK FOREIGN KEY (POS_ID) REFERENCES POSITIONS(POS_ID)
);

CREATE TABLE SALARY(
	SAL_ID			INTEGER		PRIMARY KEY,
    EMP_ID			INTEGER,
    SALARY_PER_HR	FLOAT,
    TAX				FLOAT,
    DATE_CREATED	TIMESTAMP,
    DATE_UPDATED	TIMESTAMP,
    CONSTRAINT SAL_EMP_FK FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID)
);