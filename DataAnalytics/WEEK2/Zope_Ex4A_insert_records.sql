USE lana_dog_walking;

INSERT INTO Location (Location_Address, Location_City, Location_State, Location_Zipcode)
VALUES
('123 Main St', 'San Francisco', 'CA', '94105'),
('456 Oak Ave', 'Oakland', 'CA', '94607'),
('789 Pine Rd', 'San Jose', 'CA', '95112'),
('101 Maple Dr', 'Berkeley', 'CA', '94704'),
('202 Cedar Ln', 'Daly City', 'CA', '94014'),
('303 Birch St', 'Fremont', 'CA', '94536'),
('404 Walnut Ave', 'Hayward', 'CA', '94541'),
('505 Cherry Blvd', 'San Mateo', 'CA', '94401'),
('606 Aspen Ct', 'Richmond', 'CA', '94804'),
('707 Redwood Way', 'Palo Alto', 'CA', '94301'),
('808 Spruce Pl', 'Sunnyvale', 'CA', '94085');

SELECT * FROM Location;

-- Insert records into Customer
INSERT INTO Customer (Customer_Name, Customer_PhoneNumber, Location_ID)
VALUES
('Lana Brooks', '415-555-0198', 1),
('Maya Patel', '510-555-0112', 2),
('Carlos Ramirez', '408-555-0177', 3),
('Emily Chen', '510-555-0134', 4),
('Jordan Smith', '650-555-0148', 5),
('Priya Shah', '510-555-0166', 6),
('Noah Williams', '510-555-0183', 7),
('Sophia Johnson', '650-555-0191', 8),
('Daniel Lee', '510-555-0127', 9),
('Olivia Martinez', '650-555-0155', 10),
('Ethan Brown', '408-555-0109', 11);


SELECT * FROM Customer;


INSERT INTO Dog (Dog_Name, Dog_Breed, Size, Customer_ID)
VALUES
('Max', 'Golden Retriever', 'Large', 1),
('Bella', 'Poodle', 'Medium', 2),
('Rocky', 'Beagle', 'Medium', 3),
('Luna', 'German Shepherd', 'Large', 4),
('Charlie', 'French Bulldog', 'Small', 5),
('Daisy', 'Labrador Retriever', 'Large', 6),
('Milo', 'Shih Tzu', 'Small', 7),
('Coco', 'Boxer', 'Large', 8),
('Buddy', 'Dachshund', 'Small', 9),
('Lucy', 'Siberian Husky', 'Large', 10),
('Teddy', 'Cocker Spaniel', 'Medium', 11);


SELECT * FROM Dog;