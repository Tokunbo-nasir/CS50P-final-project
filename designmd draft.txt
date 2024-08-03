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