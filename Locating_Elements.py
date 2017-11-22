# coding=utf-8
from selenium import webdriver

#选择Chrome浏览器
driver = webdriver.Chrome()
# 最大化
driver.maximize_window()
# 当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
# 换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
driver.implicitly_wait(2)
# 浏览器输入网址 打开网页
driver.get("https://mail.qq.com/cgi-bin/loginpage")
#定位到对应的frame  页面其实是由多个frame拼成的
driver.switch_to_frame("login_frame")
#定位单个元素
#find_element_by_id 通过id定位元素
elem_click = driver.find_element_by_id("switcher_plogin")
elem_click.click()

elem_user = driver.find_element_by_id("u")
elem_user.send_keys("252160922@qq.com")
elem_password = driver.find_element_by_id("p")
elem_password.send_keys("Shejiao521#")

loginClick = driver.find_element_by_id("login_button")
# 登录成功
loginClick.click()
# 等5秒
driver.implicitly_wait(5)
#此行代码用来定位当前页面
mail_window=driver.current_window_handle
print(mail_window)
#打开我的邮件
my_email = driver.find_element_by_id("folder_1")
my_email.click()

driver.switch_to_frame("mainFrame")
my_all_email = driver.find_elements_by_class_name("cx")
#email = my_all_email[0].find_element_by_tag_name("input")
# for email in my_all_email:
#     print(email.find_elements_by_xpath("//input[@type='checkbox']"))
#     if email.find_element_by_tag_name("input").get_attribute("unread") == 'true':
#         email.find_element_by_tag_name("input").get_attribute("unread").selected()
for email in my_all_email:
    if email.find_element_by_tag_name("input").get_attribute("unread") == 'true':
        email.find_element_by_tag_name("input").click()
delete_butten = driver.find_element_by_id("quick_completelydel").click()

pop_window=driver.current_window_handle

driver.switch_to.default_content()
driver.find_element_by_id("QMconfirm_QMDialog_confirm").click()
#定义新的野蛮奶奶
driver.current_window_handle