
-- Database - example

CREATE DATABASE IF NOT EXISTS `example` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Table structure for table `example`.`t_item`

DROP TABLE IF EXISTS `example`.`t_item`;

CREATE TABLE `example`.`t_item` (
	`id` INT(11) UNSIGNED NOT NULL COMMENT 'ID',
	`name_chs` VARCHAR(64) COLLATE utf8_general_ci NOT NULL COMMENT '名称',
	`name_eng` VARCHAR(64) COLLATE utf8_general_ci NOT NULL COMMENT '名称',
	`dscp_chs` VARCHAR(128) COLLATE utf8_general_ci NOT NULL COMMENT '描述',
	`dscp_eng` VARCHAR(128) COLLATE utf8_general_ci NOT NULL COMMENT '描述',
	`icon` VARCHAR(64) COLLATE utf8_general_ci NOT NULL COMMENT '图标',
	`type` INT(11) UNSIGNED NOT NULL COMMENT '类型',
	`quality` INT(11) UNSIGNED NOT NULL COMMENT '品质',
	`pack_limit` INT(11) UNSIGNED NOT NULL COMMENT '叠加上限',
	`price` INT(11) UNSIGNED NOT NULL COMMENT '出售价格',
	PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_general_ci COMMENT '物品表';

-- Dumping data for table `example`.`t_item`

TRUNCATE TABLE `example`.`t_item`;

INSERT INTO `example`.`t_item` (`id`, `name_chs`, `name_eng`, `dscp_chs`, `dscp_eng`, `icon`, `type`, `quality`, `pack_limit`, `price`)
VALUES
(1, '物品_1', 'item_1', '描述_1', 'dscp_1', 'icon_1', 11, 1, 99, 100),
(2, '物品_2', 'item_2', '描述_2', 'dscp_2', 'icon_2', 11, 2, 99, 100),
(3, '物品_3', 'item_3', '描述_3', 'dscp_3', 'icon_3', 11, 3, 99, 100),
(4, '物品_4', 'item_4', '描述_4', 'dscp_4', 'icon_4', 11, 4, 99, 100),
(5, '物品_5', 'item_5', '描述_5', 'dscp_5', 'icon_5', 12, 1, 99, 100),
(6, '物品_6', 'item_6', '描述_6', 'dscp_6', 'icon_6', 12, 2, 99, 100),
(7, '物品_7', 'item_7', '描述_7', 'dscp_7', 'icon_7', 12, 3, 99, 100),
(8, '物品_8', 'item_8', '描述_8', 'dscp_8', 'icon_8', 12, 4, 99, 100),
(9, '物品_9', 'item_9', '描述_9', 'dscp_9', 'icon_9', 13, 1, 99, 100),
(10, '物品_10', 'item_10', '描述_10', 'dscp_10', 'icon_10', 13, 2, 99, 100),
(11, '物品_11', 'item_11', '描述_11', 'dscp_11', 'icon_11', 13, 3, 99, 100),
(12, '物品_12', 'item_12', '描述_12', 'dscp_12', 'icon_12', 13, 4, 99, 100),
(13, '物品_13', 'item_13', '描述_13', 'dscp_13', 'icon_13', 14, 1, 99, 100),
(14, '物品_14', 'item_14', '描述_14', 'dscp_14', 'icon_14', 14, 2, 99, 100),
(15, '物品_15', 'item_15', '描述_15', 'dscp_15', 'icon_15', 14, 3, 99, 100),
(16, '物品_16', 'item_16', '描述_16', 'dscp_16', 'icon_16', 14, 4, 99, 100),
(17, '物品_17', 'item_17', '描述_17', 'dscp_17', 'icon_17', 21, 1, 99, 100),
(18, '物品_18', 'item_18', '描述_18', 'dscp_18', 'icon_18', 21, 2, 99, 100),
(19, '物品_19', 'item_19', '描述_19', 'dscp_19', 'icon_19', 21, 3, 99, 100),
(20, '物品_20', 'item_20', '描述_20', 'dscp_20', 'icon_20', 21, 4, 99, 100),
(21, '物品_21', 'item_21', '描述_21', 'dscp_21', 'icon_21', 22, 1, 99, 100),
(22, '物品_22', 'item_22', '描述_22', 'dscp_22', 'icon_22', 22, 2, 99, 100),
(23, '物品_23', 'item_23', '描述_23', 'dscp_23', 'icon_23', 22, 3, 99, 100),
(24, '物品_24', 'item_24', '描述_24', 'dscp_24', 'icon_24', 22, 4, 99, 100),
(25, '物品_25', 'item_25', '描述_25', 'dscp_25', 'icon_25', 23, 1, 99, 100),
(26, '物品_26', 'item_26', '描述_26', 'dscp_26', 'icon_26', 23, 2, 99, 100),
(27, '物品_27', 'item_27', '描述_27', 'dscp_27', 'icon_27', 23, 3, 99, 100),
(28, '物品_28', 'item_28', '描述_28', 'dscp_28', 'icon_28', 23, 4, 99, 100),
(29, '物品_29', 'item_29', '描述_29', 'dscp_29', 'icon_29', 24, 1, 99, 100),
(30, '物品_30', 'item_30', '描述_30', 'dscp_30', 'icon_30', 24, 2, 99, 100),
(31, '物品_31', 'item_31', '描述_31', 'dscp_31', 'icon_31', 24, 3, 99, 100),
(32, '物品_32', 'item_32', '描述_32', 'dscp_32', 'icon_32', 24, 4, 99, 100);

