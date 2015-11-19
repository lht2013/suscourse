SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `sus_cource` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `sus_cource` ;



-- -----------------------------------------------------
-- Table `sus_cource`.`sus_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_user` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_user` (
  `uid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `rid` INT UNSIGNED NOT NULL DEFAULT 0,
  `username` CHAR(20) NOT NULL,
  `userpwd` CHAR(40) NOT NULL,
  `realname` CHAR(20) NOT NULL,
  `sex` TINYINT(1) UNSIGNED NOT NULL DEFAULT 0,
  `mobile` CHAR(20) NULL,
  `qq` CHAR(20) NULL,
  `email` CHAR(50) NULL,
  `status` INT UNSIGNED NOT NULL DEFAULT 0,
  `teachertype` INT UNSIGNED NOT NULL DEFAULT 0 '老师类型，0，无，1：笔试，2，面试',
  `createtime` INT UNSIGNED NOT NULL,
  `edittime` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC))
ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table `sus_cource`.`sus_role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_role` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_role` (
  `rid` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `rolename` CHAR(20) NOT NULL DEFAULT 0,
  `createtime` INT UNSIGNED NOT NULL,
  `edittime` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`rid`),
  UNIQUE INDEX `rolename_UNIQUE` (`rolename` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sus_cource`.`sus_course_shift`  班次表
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_course_shift` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_course_shift` (
  `csid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `shiftyear` CHAR(50) NOT NULL COMMENT '班次年份',
  `shiftname` CHAR(50) NOT NULL COMMENT '班次名字',
  `shifttype` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '班次类型，1：笔试，2，面试',
  `classtime` CHAR(50) NOT NULL COMMENT '上课时间',
  `classplace` CHAR(50) NOT NULL COMMENT '上课地点',
  `busroute` text COMMENT '乘车路线',
  `tid` INT UNSIGNED NOT NULL COMMENT '班主任/导师',
  `teachermobile` CHAR(20) NULL  COMMENT '班主任/导师 手机号',
  `status` INT UNSIGNED NOT NULL DEFAULT 0,
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`csid`),
  UNIQUE INDEX `shiftname_UNIQUE` (`shiftname` ASC))
ENGINE = InnoDB;




--if 笔试
-- -----------------------------------------------------
-- Table `sus_cource`.`sus_sub_classes`  班型表
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_course_class` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_course_class` (
  `ccid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `csid` INT UNSIGNED NOT NULL  COMMENT '班次ID',
  `classesname` CHAR(50) NOT NULL COMMENT '班型名称',
  `status` INT UNSIGNED NOT NULL DEFAULT 0,
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`ccid`))
ENGINE = InnoDB;




DROP TABLE IF EXISTS `sus_cource`.`sus_course_relation` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_course_relation` (
  `crid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `csid` INT UNSIGNED NOT NULL ,
  `ccid` INT UNSIGNED NOT NULL ,
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`crid`))
ENGINE = InnoDB;

--联合唯一索引
-- -----------------------------------------------------
-- Table `sus_cource`.`sus_course_class`  课表
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_course` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_course` (
  `cid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `tid` INT UNSIGNED NOT NULL COMMENT '主讲老师ID',
  `csid` INT UNSIGNED NOT NULL COMMENT '班次ID',
  `ccid` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '班级ID',
  `coursetime` INT UNSIGNED NOT NULL COMMENT '上课日期',
  `intervaltime` CHAR(50) NOT NULL DEFAULT '' COMMENT '上午/下午/晚间',
  `coursename` CHAR(50) NOT NULL COMMENT '课程名字',
  `status` INT UNSIGNED NOT NULL DEFAULT 0,
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`cid`))
ENGINE = InnoDB;

--核心业务
--辅助业务
-- -----------------------------------------------------
-- Table `sus_cource`.`sus_base_course`  基本课程表
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_base_course` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_base_course` (
  `bcid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `coursename` CHAR(50) NOT NULL DEFAULT ''COMMENT '课程名称',
  `coursetype` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '课程类型，1：笔试，2，面试，3，其他',
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`cid`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `sus_cource`.`sus_base_course`  老师表
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_base_course` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_base_course` (
  `bcid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `coursename` CHAR(50) NOT NULL DEFAULT ''COMMENT '课程名称',
  `coursetype` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '课程类型，1：笔试，2，面试，3，其他',
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`cid`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `sus_cource`.`sus_course_year`  课程年度表
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sus_cource`.`sus_shift_year` ;

CREATE TABLE IF NOT EXISTS `sus_cource`.`sus_shift_year` (
  `syid` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `shiftyear` CHAR(50) NOT NULL DEFAULT ''COMMENT '课程年度',
  `flag` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '1:默认',
  `createtime` INT UNSIGNED NOT NULL DEFAULT 0,
  `edittime` INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`syid`))
ENGINE = InnoDB;

insert into sus_user(rid,username,userpwd,status,realname,sex,mobile,qq,email,createtime,edittime) values ('1','admin','96e79218965eb72c92a549dd5a330112','1','1','1','13920855675','2357071','lhtlj2002@163.com','1299801600','1299801600');
insert into sus_role(rolename,createtime,edittime) values ('超级管理员','1299801600','1299801600')
insert into sus_role(rolename,createtime,edittime) values ('面试部老师','1299801600','1299801600')
insert into sus_role(rolename,createtime,edittime) values ('笔试部老师','1299801600','1299801600')
insert into sus_role(rolename,createtime,edittime) values ('授课老师','1299801600','1299801600')

insert into sus_role(rolename,createtime,edittime) values ('授课老师','1299801600','1299801600')