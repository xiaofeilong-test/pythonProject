import requests
import unittest
from Common import Common

'''
查询功能测试，调用Common实现
'''
class zhikang_getcheckIT(unittest.TestCase):
    '''
    获取公告列表接口
    '''
    def test_noticesIT(self):
        Comm=Common("http://api-cloud.st.chunhuahealth.com")
        uri=r"/notices"
        headers=\
            {
                "X-Platform":"0",
                "X-Brand":"610"
            }
        r = Comm.get(uri,headers=headers)
        id = r[0]["id"]
        print(id)
        self.assertEqual(2,id)
        # self.assertEqual(200,r.status_code)
        # res = r.json()
        # print(res)
        # data = res[0]
        # print(data)
        # id = data['id']
        # print(id)
        # self.assertEqual(2,id)


if __name__ == "__main__":
    '''
    TODO
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
    # suite.addTest(zhikang_getcheckIT('test_service_pzcks_idIT'))
    # 添加多个测试用例
    suite.addTests([zhikang_getcheckIT('test_noticesIT')])
    # 执行测试 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1；如果设为 0，则不输出每一用例的执行结果；如果设为 2，则输出详细的执行结果
    runer = unittest.TextTestRunner(verbosity=2)
    runer.run(suite)

    #  3.使用testLoader方式，同时测试多个类
    #     suite1 = unittest.TestLoader().loadTestsFromTestCase(zhikang_getcheckIT)
    #     suite2 = unittest.TestLoader().loadTestsFromTestCase(zhikang_getcheckIT)
    #     suite = unittest.TestSuite([suite1,suite2])
    #     unittest.TextTestRunner().run(suite)

# '''
# 查询功能测试
# '''
# class zhikang_getcheckIT(unittest.TestCase):
#     '''
#     获取公告列表接口
#     '''
#     def test_noticesIT(self):
#         host="http://api-cloud.st.chunhuahealth.com"
#         endpoint=r"/notices"
#         url = "".join([host, endpoint])
#         headers=\
#             {
#                 "X-Platform":"0",
#                 "X-Brand":"610"
#             }
#         r = requests.get(url,headers=headers)
#         print(r.status_code)
#         self.assertEqual(200,r.status_code)
#         res = r.json()
#         print(res)
#         data = res[0]
#         print(data)
#         id = data['id']
#         print(id)
#         self.assertEqual(2,id)
#
#     '''
#     按类别分组的服务列表
#     '''
#     def test_catalog_groupIT(self):
#         host="http://api-cloud.st.chunhuahealth.com"
#         endpoint=r"/services/catalog-group"
#         url = "".join([host, endpoint])
#         headers=\
#             {
#                 "X-Platform":"0",
#                 "X-Brand":"610"
#             }
#         r = requests.get(url,headers=headers)
#         print(r.status_code)
#         self.assertEqual(200,r.status_code)
#         res = r.json()
#         print(res)
#         data = res[0]['services'][0]["id"]
#         print(data)
#         self.assertEqual(2,data)
#         # data = res[0]
#         # print(data)
#         # id = data['id']
#         # print(id)
#
#     '''
#     查询套餐列表
#     '''
#     def test_service_packsIT(self):
#         host="http://api-cloud.st.chunhuahealth.com"
#         endpoint=r"/service-packs"
#         url = "".join([host, endpoint])
#         headers=\
#             {
#                 "X-Platform":"0",
#                 "X-Brand":"610"
#             }
#         r = requests.get(url,headers=headers)
#         print(r.status_code)
#         self.assertEqual(200,r.status_code)
#         res = r.json()
#         print(res)
#         data = res[0]['id']
#         print(data)
#         self.assertEqual(14,data)
#
#     '''
#     查询套餐详情
#     '''
#     def test_service_pzcks_idIT(self):
#         host="http://api-cloud.st.chunhuahealth.com"
#         endpoint=r"/service-packs/14"
#         url = "".join([host, endpoint])
#         headers=\
#             {
#                 "X-Platform":"0",
#                 "X-Brand":"610"
#             }
#         r = requests.get(url,headers=headers)
#         print(r.status_code)
#         self.assertEqual(200,r.status_code)
#         res = r.json()
#         print(res)
#         data = res['pack_name']
#         print(data)
#         self.assertEqual('小绿卡•个人版',data)
#
#
# if __name__ == "__main__":
#     '''
#     TODO
#     利用python进行测试是，测试用例加载方式有2中
#     1.通过unittest.main()来执行测试用例的方式,调试全部用例
#     2.添加到testsuite集合中再加载所有的被测试对象，调试单个用例
#     3.使用testLoader方式，同时测试多个类
#     '''
#     #  1.通过unittest.main()来执行测试用例的方式,调试全部用例
#     # unittest.main()
#
#     #  2.添加到testsuite集合中再加载所有的被测试对象，调试单个用例
#     suite = unittest.TestSuite()
#     # 添加单个测试用例到容器中
#     # suite.addTest(zhikang_getcheckIT('test_service_pzcks_idIT'))
#     # 添加多个测试用例
#     suite.addTests([zhikang_getcheckIT('test_service_pzcks_idIT'),zhikang_getcheckIT('test_service_packsIT')])
#     # 执行测试 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1；如果设为 0，则不输出每一用例的执行结果；如果设为 2，则输出详细的执行结果
#     runer = unittest.TextTestRunner(verbosity=2)
#     runer.run(suite)
#
#     #  3.使用testLoader方式，同时测试多个类
#     #     suite1 = unittest.TestLoader().loadTestsFromTestCase(zhikang_getcheckIT)
#     #     suite2 = unittest.TestLoader().loadTestsFromTestCase(zhikang_getcheckIT)
#     #     suite = unittest.TestSuite([suite1,suite2])
#     #     unittest.TextTestRunner().run(suite)


