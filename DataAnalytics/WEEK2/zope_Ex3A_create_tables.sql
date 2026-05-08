DROP SCHEMA IF EXISTS lana_dog_walking;
CREATE SCHEMA lana_dog_walking;
USE lana_dog_walking;


CREATE TABLE Owners (
    OwnerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(255)
);


CREATE TABLE Walkers (
    WalkerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Phone VARCHAR(15),
    Email VARCHAR(100)
);


CREATE TABLE Pets (
    PetID INT AUTO_INCREMENT PRIMARY KEY,
    OwnerID INT,
    PetName VARCHAR(50) NOT NULL,
    Breed VARCHAR(50),
    Age INT,
    Notes TEXT,
    FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID)
);

-- Table: Walks
CREATE TABLE Walks (
    WalkID INT AUTO_INCREMENT PRIMARY KEY,
    PetID INT,
    WalkerID INT,
    WalkDate DATETIME,
    DurationMinutes INT,
    Fee DECIMAL(10, 2),
    FOREIGN KEY (PetID) REFERENCES Pets(PetID),
    FOREIGN KEY (WalkerID) REFERENCES Walkers(WalkerID)
);
