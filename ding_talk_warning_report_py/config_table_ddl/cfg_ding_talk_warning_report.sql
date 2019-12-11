CREATE TABLE `cfg_ding_talk_warning_report` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `ding_talk_group_id` bigint(20) NOT NULL COMMENT '钉钉组名id',
  `ding_talk_group_name` varchar(200) NOT NULL COMMENT '钉钉组名',
  `robot_url` varchar(500) NOT NULL COMMENT '机器人ulr',
  `robot_name` varchar(500) DEFAULT NULL COMMENT '机器人名字',
  `warning_report_text` varchar(500) NOT NULL COMMENT '报警内容',
  `at_people_phone` varchar(500) DEFAULT NULL COMMENT '提醒谁看',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `create_by` varchar(50) NOT NULL COMMENT '创建人',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `update_by` varchar(50) NOT NULL COMMENT '修改人',
  `is_enable` int(11) NOT NULL COMMENT '是否有效',
  `level_desc` varchar(50) NOT NULL COMMENT '紧急等级:普通，中等，紧急',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8