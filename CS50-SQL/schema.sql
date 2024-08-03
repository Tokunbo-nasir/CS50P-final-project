CREATE TABLE `bodyspec`(
    `id` INT AUTO_INCREMENT,
    `bodytype` VARCHAR(100),
    `doors` VARCHAR(100),
    `gearbox` VARCHAR(100),
    PRIMARY KEY(`id`)
);

CREATE TABLE `enginespec`(
    `id` INT AUTO_INCREMENT,
    `enginesize` DECIMAL(2,2) NOT NULL,
    `fueltype` VARCHAR(100),
    `horsepower` INT,
    PRIMARY KEY (`id`)
 );

CREATE TABLE `carspec`(
    `id` INT AUTO_INCREMENT,
    `make` VARCHAR(100),
    `reg` INT,
    `year` YEAR,
    `price` BIGINT NOT NULL,
    `milage` BIGINT NOT NULL,
    `body_id` INT,
    `engine_id` INT,
    `datetime` DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`body_id`) REFERENCES `bodyspec`(`id`),
    FOREIGN KEY(`engine_id`) REFERENCES `enginespec`(`id`)
);

CREATE VIEW `alltables` AS
SELECT `carspec`.`id`, `carspec`.`make`, `carspec`.`reg`, `carspec`.`year`,
`carspec`.`price`,`carspec`.`milage`, `carspec`.`datetime`, `carspec`.`body_id`, `carspec`.`engine_id`,
`enginespec`.`enginesize`, `enginespec`.`fueltype`,`enginespec`.`horsepower`,
`bodyspec`.`bodytype`, `bodyspec`.`doors`, `bodyspec`.`gearbox`
FROM `carspec`
JOIN `bodyspec` ON `bodyspec`.`id` = `carspec`.`body_id`
JOIN `enginespec` ON `enginespec`.`id` = `carspec`.`engine_id`;

CREATE VIEW `engineinfo` AS 
SELECT  `carspec`.`id`, `carspec`.`make`, `carspec`.`reg`, `carspec`.`year`,
`carspec`.`price`,`carspec`.`milage`, `carspec`.`datetime`,`carspec`.`engine_id`,
`enginespec`.`enginesize`, `enginespec`.`fueltype`,`enginespec`.`horsepower`
FROM `carspec`
JOIN `enginespec` ON `enginespec`.`id` = `carspec`.`engine_id`;

CREATE VIEW `bodyinfo` AS
SELECT  `carspec`.`id`, `carspec`.`make`, `carspec`.`reg`, `carspec`.`year`,
`carspec`.`price`,`carspec`.`milage`, `carspec`.`datetime`, `carspec`.`body_id`, 
`bodyspec`.`bodytype`, `bodyspec`.`doors`, `bodyspec`.`gearbox`
FROM `carspec`
JOIN `bodyspec` ON `bodyspec`.`id` = `carspec`.`body_id`;

CREATE INDEX `enginesearch` ON `enginespec`(`id`);
CREATE INDEX `bodysearch` ON `bodyspec`(`id`);
