/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3306
 Source Schema         : kqi_db

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 06/12/2018 11:28:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hefeixin_2018
-- ----------------------------
DROP TABLE IF EXISTS `hefeixin_2018`;
CREATE TABLE `hefeixin_2018`  (
  `id` int(100) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '自增主键，不用管',
  `product_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '产品名称',
  `client` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试端，android/ios/web/wap',
  `bussiness` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试业务的具体场景，用来做权重区分',
  `data_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '数据类型，参见test_type表',
  `data_value` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '测试值',
  `network` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '4G/Wifi/固网',
  `remark` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用于备注',
  `test_time` datetime(0) NOT NULL COMMENT '测试时间',
  `modify_time` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '数据最后一次修改时间',
  `is_delete` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '0' COMMENT '未删除：0/已删除：1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 125917 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
