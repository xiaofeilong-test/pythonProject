import requests
import unittest
from LoginIT import loginIT


class FamilyMembersIT(unittest.TestCase):
    '''
    新增成员信息
    '''
    # def test_family_membersIT(self):
    #     host = "http://api-cloud.st.chunhuahealth.com"
    #     endpoint = r"/family-members"
    #     url="".join([host,endpoint])
    #     token = loginIT().test_login_phone_codeIT()
    #     headers=\
    #         {
    #             "X-Platform":"2",
    #             "X-Brand":"100",
    #             'Authorization':"Bearer"+token
    #         }
    #     body=\
    #         {
    #             "relationship":'1',
    #             "name":"王一",
    #             "title":"dad",
    #             "gender":"1",
    #             "birth_date":"1965-01-01",
    #             "phone":"15688888888"
    #         }
    #
    #     r = requests.post(url, headers=headers,data=body)
    #     res = r.json()
    #     print(res)
    #     # self.assertEqual(200, r.status_code)
    '''
    获取家庭成员列表
    '''
    def test_family_memberslistIT(self):
        host = "http://api-cloud.st.chunhuahealth.com"
        endpoint = r"/family-members"
        url="".join([host,endpoint])
        token = loginIT().test_login_phone_codeIT()
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"100",
                'Authorization':"Bearer"+token
            }

        r = requests.get(url, headers=headers)
        id = r.json()[1]['id']
        print(id)
        return (id)
        self.assertEqual(200, r.status_code)
        # self.assertEqual(3, id)
    '''
    查询指定家庭成员列表
    '''
    def test_getmembersIdIT(self):
        id = self.test_family_memberslistIT()
        host = "http://api-cloud.st.chunhuahealth.com"
        endpoint = r"/family-members/{}".format(id)
        url="".join([host,endpoint])
        print(url)
        token = loginIT().test_login_phone_codeIT()
        headers=\
            {
                "X-Platform":"2",
                "X-Brand":"100",
                'Authorization':"Bearer"+token
            }
        r = requests.get(url, headers=headers)
        res=r.json()
        print(res)
        self.assertEqual(200, r.status_code)
    '''
    修改制定家庭成员列表
    '''
    # def test_post_membersIdIT(self):
    #     id = self.test_family_memberslistIT()
    #     host = "http://api-cloud.st.chunhuahealth.com"
    #     endpoint = r"/family-members/{}".format(id)
    #     url="".join([host,endpoint])
    #     print(url)
    #     token = loginIT().test_login_phone_codeIT()
    #     headers=\
    #         {
    #             "X-Platform":"2",
    #             "X-Brand":"100",
    #             'Authorization':"Bearer"+token
    #         }
    #     body=\
    #         {
    #             "relationship":'1',
    #             "name":"王er",
    #             "title":"dad",
    #             "gender":"1",
    #             "birth_date":"1965-01-01",
    #             "phone":"15688888888"
    #         }
    #     r = requests.post(url, headers=headers, data=body)
    #     res=r.json()
    #     print(res)

if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    test_cases = map(FamilyMembersIT,["test_family_memberslistIT",'test_getmembersIdIT'])
    # test_cases = [FamilyMembersIT("test_family_memberslistIT")]
    suite.addTest(test_cases)

    # 执行测试
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(suite)
