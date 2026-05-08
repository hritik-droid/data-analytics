# Requirements and Conceptual Model

**Group Members:** Jeremiah Goode, Hritik Zope, Stefanie Ramirez

Lana is the owner of a dog-walking business. She needs a database that helps her keep track of customers, their dogs, and the locations connected to those customers. The end user is Lana, and she needs to be able to store customer contact information, identify each dog, and organize address information for where customers are located.

The main categories of data that are important to track are:
- Customers
- Dogs
- Locations

## Customer
This category stores information about each customer who uses Lana’s dog-walking business.

Useful information to track:
- Customer_ID
- Customer_Name
- Customer_PhoneNumber
- Location_ID

## Dog
This category stores information about each dog that belongs to a customer.

Useful information to track:
- Dog_ID
- Dog_Name
- Dog_Breed
- Size
- Customer_ID

## Location
This category stores address information connected to customers.

Useful information to track:
- Location_ID
- Location_Address
- Location_City
- Location_State
- Location_Zipcode

# Logical Model

The main entities in this database are **Customer**, **Dog**, and **Location**.

## Entity: Location
The Location table stores address information. Each location has a unique ID and includes the address, city, state, and zipcode.

**Attributes:**
- Location_ID (Primary Key)
- Location_Address
- Location_City
- Location_State
- Location_Zipcode

## Entity: Customer
The Customer table stores information about each customer. Each customer has a unique ID, a name, and a phone number. Each customer is connected to one location.

**Attributes:**
- Customer_ID (Primary Key)
- Customer_Name
- Customer_PhoneNumber
- Location_ID (Foreign Key)

## Entity: Dog
The Dog table stores information about each dog. Each dog has a unique ID, a name, breed, and size. Each dog belongs to one customer.

**Attributes:**
- Dog_ID (Primary Key)
- Dog_Name
- Dog_Breed
- Size
- Customer_ID (Foreign Key)

# Relationships

- One **Location** can have many **Customers**
- One **Customer** belongs to one **Location**
- One **Customer** can have many **Dogs**
- One **Dog** belongs to one **Customer**

# Many-to-Many Relationships

There are no many-to-many relationships in this version of the model, so no resolving table is needed.

# Notes on Design Choices

The group chose to use unique ID columns as primary keys because names and addresses are not always unique. Foreign keys are used to connect related tables. The Customer table includes Location_ID to connect each customer to a location, and the Dog table includes Customer_ID to connect each dog to its owner.

This design keeps the data organized and avoids repeating the same address or customer information over and over. It also makes it easier to connect customers to dogs and locations when retrieving data from the database later.
