/*
Navicat MySQL Data Transfer

Source Server         : guba
Source Server Version : 50731
Source Host           : localhost:3306
Source Database       : guba

Target Server Type    : MYSQL
Target Server Version : 50731
File Encoding         : 65001

Date: 2020-10-11 14:59:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for author_info
-- ----------------------------
DROP TABLE IF EXISTS `author_info`;
CREATE TABLE `author_info` (
  `author_url` varchar(255) CHARACTER SET utf8 NOT NULL,
  `following_number` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `follower_number` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`author_url`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for content_info
-- ----------------------------
DROP TABLE IF EXISTS `content_info`;
CREATE TABLE `content_info` (
  `title_url` varchar(255) CHARACTER SET utf8 NOT NULL,
  `content` text CHARACTER SET utf8,
  PRIMARY KEY (`title_url`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for main_info
-- ----------------------------
DROP TABLE IF EXISTS `main_info`;
CREATE TABLE `main_info` (
  `read_number` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `command_number` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `title_url` varchar(255) CHARACTER SET utf8 NOT NULL,
  `author` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `author_url` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `date` varchar(255) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`title_url`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
SET FOREIGN_KEY_CHECKS=1;
