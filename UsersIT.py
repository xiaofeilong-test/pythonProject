import requests
import unittest
from LoginIT import loginIT

class usersIT(unittest.TestCase):
    def test_user_meIT(self):
        me = "http://api-cloud.st.chunhuahealth.com"
        endpoint=r"/users/me"
        token = loginIT().test_login_phone_codeIT()
        url="".join([me,endpoint])
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"100",
                'Authorization':"Bearer"+token
            }
        #调用post方法，拼接入参，发送请求
        r=requests.get(url,headers=headers)
        #获取范围id
        res = r.json()
        print(res)
        # self.assertEqual(200, r.status_code)

        # token = r.json()["token"]
        # print(token)
        # self.assertEqual(10,id)#检验字段值
        # print(token)
        # print(r.text)

    def test_user_imIT(self):
        me = "http://api-cloud.st.chunhuahealth.com"
        endpoint=r"/user/im"
        token = loginIT().test_login_phone_codeIT()
        url="".join([me,endpoint])
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"100",
                'Authorization':"Bearer"+token
            }
        #调用post方法，拼接入参，发送请求
        r=requests.get(url,headers=headers)
        #获取范围id
        res = r.json()
        print(res)
        # self.assertEqual(200, r.status_code)

        # token = r.json()["token"]
        # print(token)
        # self.assertEqual(10,id)#检验字段值
        # print(token)
        # print(r.text)
        # # print(r.url)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests([usersIT("test_user_meIT"),usersIT("test_user_imIT")])
    unittest.TextTestRunner().run(suite)
