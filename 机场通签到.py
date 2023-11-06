import requests


def run(openid):
  url='https://api.baiyunairport.top/member/activityTask/web/dailyAttendance?openIdEnc='+openid
  headers={
      "Accept-Encoding":"gzip,compress,br,deflate",
      "Connection":"keep-alive",
      "Host":"api.baiyunairport.top",
      "Referer":"https://servicewechat.com/wx840bed0d9162e942/412/page-frame.html",
      "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.42(0x18002a31) NetType/WIFI Language/zh_CN",
      "content-type":"application/json"
  }
  
  r=requests.get(url,headers=headers)
  print(r.text)

if __name__ == '__main__':
    openid=''
    run(openid)
