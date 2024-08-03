--TODO which is an annotated set of SELECT, INSERT, UPDATE, DELETE, etc. 
--statements that users will commonly run on your database.

INSERT INTO bodyspec(bodytype, doors, gearbox) VALUES(SUV,5,Automatic);
INSERT INTO enginespec(enginesize, fueltype, horsepower) VALUES(6.0, petrol, 154);
INSERT INTO carspec(make, reg, year, price, milage) VALUES(BMW, 23, 2023, 19000, 40000);

UPDATE `carspec` JOIN `bodyspec` ON `bodyspec`.`id`=`carspec`.`id` SET `carspec`.`body_id` = `bodyspec`.`id`;
UPDATE `carspec` JOIN `enginespec` ON `enginespec`.`id`=`carspec`.`id` SET `carspec`.`engine_id` = `enginespec`.`id`;