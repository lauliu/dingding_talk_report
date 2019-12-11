# dingding_talk_report
1.顶顶报警有两个版本，采用的是python脚本编写
版本一：调度服务器能连接网络，如uat，本机测试等地方，不需要代理服务器；
版本二：调度服务器不能连接外网，如prod集群的azkban，保险起见，使用代理版本；

2.python脚本路径：
版本一：ding_talk_warning_report_py\main\ding_talk_with_agency.py
版本二：ding_talk_warning_report_py\main\ding_talk_with_no_agency.py

3.代理服务器，钉钉配置表的配置信息(绝密)
ding_talk_warning_report_py\conf\myconfig.ini

4.dingding配置表在mysql
uat在
host = uat
port = 3306
user = dw_user_uat
db = dw_config_uat
table=cfg_ding_talk_warning_report

prod
host = prod
port = 3306
user = dw_user_prod
db = dw_config_prod
table=cfg_ding_talk_warning_report

切换哪一个环境，只需要打开ding_talk_warning_report_py\conf\myconfig.ini修改[mysql_dw_config] section下的配置信息即可。

5.调用方法：
在ding_talk_warning_report_py\main\路径内，根据mysql的配置信息
python ding_talk_with_agency.py 配置表内的id
如：
python ding_talk_with_agency.py 1  调取配置表id=1的钉钉代理报警
python ding_talk_with_no_agency.py 2 调取配置表id=2的钉钉非代理报警

6.顶顶机器人图片推荐
推荐使用：ding_talk_warning_report_py\pic\timg3.jpg

7.git ding_talk_warning_report_py\conf\mysql_dw_config] section下为了安全，我去掉了
dw_user和passwd的值，如果从git取，记得补上;
