#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import unittest

'''
登陆功能
'''
class loginIT(unittest.TestCase):
    '''
    用户手机验证码登陆
    短信验证码使用万能码1111
    '''
    def test_login_phone_codeIT(self):
        host="http://api-cloud.st.chunhuahealth.com"
        endpoint=r"/login/phone-code"
        url="".join([host,endpoint])
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"610"
            }
        body=\
            {
                "phone":"15656072722",
                "code":"1111",
                "platform":"2"
            }
        #调用post方法，拼接入参，发送请求
        r=requests.post(url,headers=headers,data=body)
        self.assertEqual(200, r.status_code)
        #获取范围id
        id = r.json()["id"]
        token = r.json()["token"]
        return (token)
        self.assertEqual(10,id)#检验字段值
        print(token)

    '''
    医生手机账号密码登录
    '''
    def test_loginIT(self):
        host="http://api-cloud.st.chunhuahealth.com"
        endpoint=r"/login"
        url="".join([host,endpoint])
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"100"
            }
        body=\
            {
                "phone":"15656072722",
                "password":"111111",
            }
        #调用post方法，拼接入参，发送请求
        r=requests.post(url,headers=headers,data=body)
        self.assertEqual(200, r.status_code)
        #获取范围id
        res = r.json()
        # print(res)
        token = r.json()["token"]
        # print(token)
        return (token)
        # self.assertEqual(10,id)#检验字段值
        # print(token)
        # print(r.text)
        # # print(r.url)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(loginIT("test_loginIT"))
    unittest.TextTestRunner().run(suite)
