CREATE TABLE `internship` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `position` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `s_date` varchar(100) DEFAULT NULL,
  `duration` varchar(100) DEFAULT NULL,
  `stipend` int DEFAULT NULL,
  `skill_req` varchar(100) DEFAULT NULL,
  `end_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);


CREATE TABLE `rays_carear` (
  `position` varchar(500) DEFAULT NULL,
  `skil` varchar(5000) DEFAULT NULL,
  `mode` varchar(1000) DEFAULT NULL,
  `exp` varchar(100) DEFAULT NULL,
  `vacency` varchar(100) DEFAULT NULL,
  `clo_data` varchar(45) DEFAULT NULL,
  `place` varchar(500) DEFAULT NULL,
  `sal` varchar(45) DEFAULT NULL,
  `sn` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sn`)
);


CREATE TABLE `rays_contact_us` (
  `name` varchar(50) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `mo_no` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `message` longtext,
  `ai` int NOT NULL AUTO_INCREMENT,
  `d_t` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ai`)
);


CREATE TABLE `rays_intern_apply` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `name` varchar(500) DEFAULT NULL,
  `mo_no` varchar(500) DEFAULT NULL,
  `email` varchar(500) DEFAULT NULL,
  `resume` longblob,
  `position` varchar(500) DEFAULT NULL,
  `mode` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);


CREATE TABLE `rays_job_apply` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `name` varchar(500) DEFAULT NULL,
  `mo_no` varchar(500) DEFAULT NULL,
  `email` varchar(500) DEFAULT NULL,
  `resume` longblob,
  `position` varchar(500) DEFAULT NULL,
  `mode` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);


CREATE TABLE `rays_proj_solution_video` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(500) DEFAULT NULL,
  `guide` varchar(500) DEFAULT NULL,
  `topic` varchar(500) DEFAULT NULL,
  `technology` varchar(500) DEFAULT NULL,
  `link` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);


CREATE TABLE `rays_project_presentation` (
  `sn` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(500) DEFAULT NULL,
  `topic` varchar(500) DEFAULT NULL,
  `technology` varchar(500) DEFAULT NULL,
  `tl` varchar(100) DEFAULT NULL,
  `member` varchar(500) DEFAULT NULL,
  `link` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`sn`)
);


CREATE TABLE `test` (
  `subject` varchar(5000) DEFAULT NULL,
  `topic` varchar(500) DEFAULT NULL,
  `q` varchar(500) DEFAULT NULL,
  `a` varchar(500) DEFAULT NULL,
  `o1` varchar(500) DEFAULT NULL,
  `o2` varchar(500) DEFAULT NULL,
  `o3` varchar(500) DEFAULT NULL,
  `o4` varchar(500) DEFAULT NULL,
  `sn` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sn`)
);