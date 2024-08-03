# Design Document

Nasir Adetokunbo Nasir

Video overview: <URL HERE>

## Scope

In this section you should answer the following questions:

* What is the purpose of your database?
Database to store information for cars

My CS50 python project is a web scraper which extracts data from autotrader.com a British platform for advertising cars.

I have combined both CS50P project and CS50 SQL project 
The scraped data is inserted into the "cars" database  (see the schema.sql file)

* Which people, places, things, etc. are you including in the scope of your database?
Internal combustion engine& hybrid cars which are advertised on AUTOTRADER.COM

* Which people, places, things, etc. are *outside* the scope of your database?

Fully electric cars are not included as the don't have the same dataset as internal combustion engine cars.

The car colour is also not included due to the way the information is stored on the website , it's not easily accesible.

## Functional Requirements

In this section you should answer the following questions:

* What should a user be able to do with your database?

They are able to derive insights and trends based on the car brand, year of production, engine performance, car shape, engine size, fuel type etc.

* What's beyond the scope of what a user should be able to do with your database?

The database does not include electric cars and car colours the user will not be able to derive any trends from this.

## Representation

### Entities

In this section you should answer the following questions:

* Which entities will you choose to represent in your database?
1) Body specifications of the car : visible parts of the car number of doors, type of gearbox (manual or automatic) e.t.c (see bodyspec table)

2) General specifications of the car : This includes general information such as body type, price, milage , year and brand/make.

3) Engine specifications of the car: This is the information that outlines the performance / non-visible aspects of the car such as engine size, horsepower, & fuel type.

* What attributes will those entities have?
1) bodytype: e.g saloon, coupe, SUV , hatchback, estate etc
2) doors: (number of doors the car has , including the boot door)
3) gearbox: e.g Automatic , Manual
4) enginesize: (specifies the size of the engine e.g 1.2 litre, 3.0 litre etc)
5) fueltype: (specifies the type of fuel e.g diesel, petrol, plugin hybrid), fully electric cars are not included as the don't have the same dataset as internal combustion engine cars.
6) horsepower: unit of measurement which expresses how quickly force is produced in the cars engine (e.g 100, 500, 1000)
7) make: this is the car brand e.g Audi,BMW, Mercedes, Ferrari etc.
8) reg: this number represents which half of the year the car was built in, e.g 23 would be Jan - Aug 2023 while 73 is Sep 2023 - Feb 2024.
Link with details (https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/359317/INF104_160914.pdf)
9) year: The year the car was built e.g 2020
10) price: The listed price of the car in british pounds
11) milage: hows many miles the car has been driven 
12) body_id: foreign key for id in bodyspec table
13) engine_id: foreign key for id in enginespec table
14) datetime: to record when entry was made into the table 

* Why did you choose the types you did?
All the attributes provide a base amount of information a user would require to make a purchasing decision on a car or to derive useful insights based on historical data.

* Why did you choose the constraints you did?
For the most part there aren't a lot of constraints because there is a good amount of error handling in my CS50P project (autotrader scraper) which ensures data inserted into this database is of good quality.

The only constraint is on the datetime column in the carspec table which sets the default to the current timestamp.

### Relationships

In this section you should include your entity relationship diagram and describe the relationships between the entities in your database.

![ER diagram cars](Entity relationship diagram.png)

carspec.body_id to bodyspec.id:
This is a one-to-many relationship where each carspec record references a specific bodyspec record via body_id. This means that a car specification can have one set of body specifications.

carspec.engine_id to enginespec.id:
This is also a one-to-many relationship where each carspec record references a specific enginespec record via engine_id. This indicates that a car specification can have one set of engine specifications.

The carspec entity is the central table holding detailed specifications of cars.

The bodyspec and enginespec entities store detailed specifications about car bodies and engines, respectively.

Relationships are established via foreign keys (body_id and engine_id) in the carspec entity, linking each car specification to its corresponding body and engine specifications.

## Optimizations

In this section you should answer the following questions:

* Which optimizations (e.g., indexes, views) did you create? Why?

## Limitations

In this section you should answer the following questions:

* What are the limitations of your design?
* What might your database not be able to represent very well?
































Database to store information for cars

My CS50 python project is a web scraper which extracts data from autotrader.com a British platform for advertising cars.

I have combined both CS50P project and CS50 SQL project 
The scraped data is inserted into the "cars" database  (see the schema.sql file)

The name of the database is "cars"

There are three tables each containing data about sections of the car 

Table 1 : bodyspec
This contains the following attributes:
1) bodytype: e.g saloon, coupe, SUV , hatchback, estate etc
2) doors: (number of doors the car has , including the boot door)
3) gearbox: e.g Automatic , Manual

Table 2 : enginespec
This contains the following attributes:
1) enginesize: (specifies the size of the engine e.g 1.2 litre, 3.0 litre etc)
2) fueltype: (specifies the type of fuel e.g diesel, petrol, plugin hybrid), fully electric cars are not included as the don't have the same dataset as internal combustion engine cars.
3) horsepower: unit of measurement which expresses how quickly force is produced in the cars engine (e.g 100, 500, 1000)

Table 3: carspec
This contains the following attributes:
1) make: this is the car brand e.g Audi,BMW, Mercedes, Ferrari etc.
2) reg: this number represents which half of the year the car was built in, e.g 23 would be Jan - Aug 2023 while 73 is Sep 2023 - Feb 2024.

Link with details (https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/359317/INF104_160914.pdf)

3) year: The year the car was built e.g 2020
4) price: The listed price of the car in british pounds
5) milage: hows many miles the car has been driven 
6) body_id: foreign key for id in bodyspec table
7) engine_id: foreign key for id in enginespec table
8) datetime: to record when entry was made into the table 

There are 3 views 

View 1: alltables
This view combines all the 3 tables into one in case all the information is required from the user at the same time.

View 2: engineinfo 
This view combines the carspec & enginespec tables in case the user cares mostly about the engine performance, general info  in the carspec table and not the outer physical features(body) of the of the car.

View 3: bodyinfo
This view combines the carspec & bodyspec tables in case the user cares mostly about the visible physical features of the car, general info  in the carspec table and not the performance(engine) of the of the car.

Indexes 
Indexes were created on the columns which are used to connect all the table together, logically this should make queries that involve multiple table faster 

Index 1 enginesearch : created on the id column of the enginespec table
Index 2 bodysearch : created on the id column of the bodyspec table 