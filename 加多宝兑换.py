import requests
import threading
import time
import random
import json
'''
仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。

================================================================================
 id=24 创意城市徽章

 id=10 城市元素冰箱贴

 id=25 加多宝城市罐产品 一箱

 id=26 创意徽章展示集合

 id=0 惊喜杭州游
 
 token填入data中 用#分割 没有技巧 全靠并发
================================================================================

 v:zhangzhrnn tg:@Arabot
'''
def run(tk,id):
    while 1:
            try:
                headers={
                    "Accept-Encoding":"gzip,compress,br,deflate",
                    "Connection":"keep-alive",
                    "Content-Length":"23",
                    "Host":"wb.onlineweixin.com",
                    "Referer":"https://servicewechat.com/wxe24d221322c28b78/5/page-frame.html",
                    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a2c) NetType/WIFI Language/zh_CN",
                    "content-type":"application/json;charset=utf-8",
                    "token":tk
                }
                url='https://wb.onlineweixin.com/jdbcms/user/queryById'
                r=requests.post(url,json={},headers=headers)
                print(r.json()["data"]["residue"])
                url='https://wb.onlineweixin.com/jdbcms/exchange/save'
                data={"id":id,"digit":"1"}
                r=requests.post(url,headers=headers,json=data)
                print(r.text)
                if '502' not in r.text:
                    print(r.text)
            except:
                pass
if __name__ == '__main__':
    data= []
    id='25'
    myT=[]
    for tk in data[0].split('#'):
        th=threading.Thread(target=run,args=(tk,id))
        myT.append(th)
    for T in myT:
        T.start()
    for T in myT:
        T.join()
