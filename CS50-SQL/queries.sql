--TODO which is an annotated set of SELECT, INSERT, UPDATE, DELETE, etc. 
--statements that users will commonly run on your database.

--statements to insert data into tables 
INSERT INTO bodyspec(bodytype, doors, gearbox) VALUES(SUV,5,Automatic);
INSERT INTO enginespec(enginesize, fueltype, horsepower) VALUES(6.0, petrol, 154);
INSERT INTO carspec(make, reg, year, price, milage) VALUES(BMW, 23, 2023, 19000, 40000);

--statements to update foreign keys in carspec table
UPDATE `carspec` JOIN `bodyspec` ON `bodyspec`.`id`=`carspec`.`id` SET `carspec`.`body_id` = `bodyspec`.`id`;
UPDATE `carspec` JOIN `enginespec` ON `enginespec`.`id`=`carspec`.`id` SET `carspec`.`engine_id` = `enginespec`.`id`;


--Questions which can be asked 

-- 1) For the different shape of cars (SUV, hatchback, saloon etc ) 
-- which have the least milage and are less than 10 years old , 
-- organise by lowest milage and lowest age first

SELECT `make`, `year`,`price` ,`bodytype`
FROM `alltables` 
WHERE `year` BETWEEN '2014' AND '2024'
ORDER BY `bodytype`,`milage` ASC, `year` ASC ;

--2) What is the cheapest car with the largest engine 

SELECT `carspec`.`make`,`enginespec`.`enginesize`, `carspec`.`price` 
FROM `carspec`
JOIN `enginespec` ON `carspec`.`engine_id` = `enginespec`.`id`
ORDER BY `enginespec`.`enginesize` DESC, `carspec`.`price` ASC
LIMIT 1 ;


--3) What is the average price of each shape / size of car ?

SELECT AVG(`price`) AS `average price`, `bodytype` 
FROM `alltables`
GROUP BY `bodytype`;