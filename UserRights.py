import requests
import unittest
from LoginIT import loginIT

class UserRights(unittest.TestCase):
    def test_rights(self):
        me = "http://api-cloud.st.chunhuahealth.com"
        endpoint=r"/rights"
        token = loginIT().test_login_phone_codeIT()
        url="".join([me,endpoint])
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"610",
                'Authorization':"Bearer "+token
            }
        #调用post方法，拼接入参，发送请求
        r=requests.get(url,headers=headers)
        #获取范围id
        res = r.json()
        print(res)
        self.assertEqual(200, r.status_code)


if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    test_cases = map(UserRights,["test_rights"])
    suite.addTests(test_cases)

    # 执行测试
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(suite)
