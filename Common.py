import requests

# 定义一个common类，父类是object
class Common(object):
    def __init__(self,url_root):
        # 被测系统的根路由
        self.url_root = url_root

    #封装自己的get请求，url是访问路由，params是请求参数，如果没有默认为空
    def get(self,uri,headers="",params=""):
        # 拼凑访问地址
        url= self.url_root+uri+params
        # 通过get请求访问对应地址
        res= requests.get(url,headers=headers)
        # 返回请求结果
        return res.json()

    #封装自己的get请求，url是访问路由，data是请求参数，如果没有默认为空
    def post(self,uri,headers="",data=""):
        # 拼凑访问地址
        url=self.url_root+uri
        if len(data)>0:
            # 如果有参数，通过post方式访问，参数赋给默认参数data
            res=requests.post(url,headers=headers,data=data)
            # 返回请求结果
            return res.json()
        else:
            # 如果无参数，访问方式如下
            res=requests.post(url,headers=headers)
            return res.json()
