CREATE TABLE `equalto`.`HOD_vision17_equalto` (
  `qID` INT default 0,
  `email` VARCHAR(200) UNIQUE,
  `startTime` TIMESTAMP,
  `endTime` TIMESTAMP,
  `count` INT default 0,
  `q1` INT default NULL,
  `q2` INT default NULL,
  `q3` INT default NULL,
  `q4` INT default NULL,
  `q5` INT default NULL,
  `q6` INT default NULL,
  `q7` INT default NULL,
  `q8` INT default NULL,
  `q9` INT default NULL,
  `q10` INT default NULL,
  `q11` INT default NULL,
  `q12` INT default NULL,
  `q13` INT default NULL,
  `q14` INT default NULL,
  `q15` INT default NULL,
  PRIMARY KEY (`email`));