# coding=utf-8
'''
cnblog的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
'''
import unittest
from selenium import webdriver
from time import sleep


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('https://mail.qq.com/cgi-bin/loginpage')  # cnblog登录页面
        self.dr.switch_to.frame("login_frame")
        elem_click = self.dr.find_element_by_id("switcher_plogin")
        elem_click.click()
        self.dr.find_element_by_id("u").send_keys(username)
        self.dr.find_element_by_id("p").send_keys(password)
        loginClick = self.dr.find_element_by_id("login_button")
        # 登录成功
        loginClick.click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('252160922@qq.com', 'Shejiao521#')  # 正确用户名和密码
        sleep(3)
        link = self.dr.find_element_by_id('useralias')
        self.assertTrue(u'张伟' in link.text)  # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
        self.dr.get_screenshot_as_file("D:\cnblogtest\login_success.jpg")  # 截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('252160922@qq.com', 'xxxxxx')  # 正确用户名，错误密码
        sleep(2)
        error_message = self.dr.find_element_by_id('err_m').text
        self.assertIn(u'你输入的帐号或密码不正确，请重新输入。', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        self.dr.get_screenshot_as_file("D:\cnblogtest\login_pwd_error.jpg")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('252160922@qq.com', '')  # 密码为空
        error_message = self.dr.find_element_by_id('err_m').text
        self.assertEqual(error_message, u'你还没有输入密码！')  # 用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
        self.dr.get_screenshot_as_file("D:\cnblogtest\login_pwd_null.jpg")

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCase)
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suite))