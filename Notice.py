import requests
import unittest

'''
构造类变量作为全局变量，代替global
'''
class global_value():
    host = "http://api-cloud.st.chunhuahealth.com"
    headers = \
        {
            "X-Platform": "0",
            "X-Brand": "610"
        }
'''
查询功能测试
'''
class zhikang_getcheckIT(unittest.TestCase):
    '''
    获取公告列表接口
    '''
    def test_noticesIT(self):
        endpoint=r"/notices"
        url = "".join([global_value.host, endpoint])
        r = requests.get(url,headers=global_value.headers)
        print(r.status_code)
        self.assertEqual(200,r.status_code)
        res = r.json()
        print(res)
        data = res[0]
        print(data)
        id = data['id']
        print(id)
        self.assertEqual(2,id)

    '''
    按类别分组的服务列表
    '''
    def test_catalog_groupIT(self):
        endpoint=r"/services/catalog-group"
        url = "".join([global_value.host, endpoint])
        r = requests.get(url,headers=global_value.headers)
        print(r.status_code)
        self.assertEqual(200,r.status_code)
        res = r.json()
        print(res)
        data = res[0]['services'][0]["id"]
        print(data)
        self.assertEqual(2,data)
        # data = res[0]
        # print(data)
        # id = data['id']
        # print(id)

    '''
    查询套餐列表
    '''
    def test_service_packsIT(self):
        endpoint=r"/service-packs"
        url = "".join([global_value.host, endpoint])
        r = requests.get(url,headers=global_value.headers)
        print(r.status_code)
        self.assertEqual(200,r.status_code)
        res = r.json()
        print(res)
        data = res[0]['id']
        print(data)
        self.assertEqual(14,data)

    '''
    查询套餐详情
    '''
    def test_service_pzcks_idIT(self):
        endpoint=r"/service-packs/14"
        url = "".join([global_value.host, endpoint])
        r = requests.get(url,headers=global_value.headers)
        print(r.status_code)
        self.assertEqual(200,r.status_code)
        res = r.json()
        print(res)
        data = res['pack_name']
        print(data)
        self.assertEqual('小绿卡•个人版',data)


if __name__ == "__main__":
    '''
    利用python进行测试是，测试用例加载方式有2中
    1.通过unittest.main()来执行测试用例的方式,调试全部用例
    2.添加到testsuite集合中再加载所有的被测试对象，调试单个用例
    3.使用testLoader方式，同时测试多个类
    '''
    #  1.通过unittest.main()来执行测试用例的方式,调试全部用例
    # unittest.main()

    #  2.添加到testsuite集合中再加载所有的被测试对象，调试单个用例
    suite = unittest.TestSuite()
    # 添加单个测试用例到容器中
    suite.addTest(zhikang_getcheckIT('test_noticesIT'))
    # 添加多个测试用例
    # suite.addTests([zhikang_getcheckIT('test_noticesIT')])
    # 执行测试 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1；如果设为 0，则不输出每一用例的执行结果；如果设为 2，则输出详细的执行结果
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(suite)

    #  3.使用testLoader方式，同时测试多个类
    #     suite1 = unittest.TestLoader().loadTestsFromTestCase(zhikang_getcheckIT)
    #     suite2 = unittest.TestLoader().loadTestsFromTestCase(zhikang_getcheckIT)
    #     suite = unittest.TestSuite([suite1,suite2])
    #     unittest.TextTestRunner().run(suite)


