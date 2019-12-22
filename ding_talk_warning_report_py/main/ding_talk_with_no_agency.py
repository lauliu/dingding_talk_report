import requests
import configparser
import json
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import sys
import os

def getcon():
    config = configparser.ConfigParser()
    file_path = os.path.dirname(__file__)
    ini_path = "%s/../conf/myconfig.ini"%file_path
    config.read(ini_path)
    config_host = config['mysql_dw_config']["host"]
    config_port = int(config['mysql_dw_config']["port"])
    config_user = config['mysql_dw_config']["user"]
    config_passwd = config['mysql_dw_config']["passwd"]
    config_db = config['mysql_dw_config']["db"]
    config_charset = config['mysql_dw_config']["charset"]

    ## print(config_host+'\t'+config_port+'\t'+config_user+'\t'+config_passwd+'\t'+config_db+'\t'+config_charset)

    try:
        print(1)
        conn = pymysql.Connect(host=config_host, port=config_port, database=config_db, user=config_user,password=config_passwd, charset=config_charset)
        return conn
    except Exception as e:
        print(e)

def ding_alert(web_hook, ding_text, at_mobile):
    url = web_hook
    msg = {
        "msgtype": "text",
        "text": {"content": ""},
        "at": {"atMobiles": [""], "isAtAll": 0}
    }
    msg["text"]["content"] = ding_text
    if not at_mobile:
        msg["at"]["isAtAll"] = 1
    else:
        msg["at"]["atMobiles"] = "[" + at_mobile + "]"
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(msg), headers=headers)

def main(argv):
    myid=int(argv[1])
    dw_config=getcon()
    sqlcmd = """ SELECT * FROM cfg_ding_talk_warning_report WHERE id=%d and is_enable=1"""
    sql1 = sqlcmd % (myid)
    ding_talk_dataframe=pd.read_sql(sql1,dw_config)
    ##print(ding_talk_dataframe)
    if ding_talk_dataframe.empty:
        print("no DingDingTalk Report")
    else:
        url=ding_talk_dataframe['robot_url'].values[0]
        print("url:"+url)
        text=ding_talk_dataframe['robot_name'].values[0]+":"+ding_talk_dataframe['warning_report_text'].values[0]+"    处理等级:"+ding_talk_dataframe['level_desc'].values[0]
        print("text:"+text)
        atMobile=ding_talk_dataframe['at_people_phone'].values[0]
        print("atMobile:"+atMobile)
        ding_alert(url, text, atMobile)

if __name__ == "__main__":
    main(sys.argv)
