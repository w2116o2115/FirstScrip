# coding=utf-8
"""
xpath 是XML Path的简称， 由于HTML文档本身就是一个标准的XML页面，所以我们可以使用Xpath 的用法来定位页面元素。

xpath定位的缺点
xpath 这种定位方式， webdriver会将整个页面的所有元素进行扫描以定位我们所需要的元素， 这是个非常费时的操作，
如果脚本中大量使用xpath做元素定位的话， 脚本的执行速度可能会稍慢

第一种方法：通过绝对路径做定位（相信大家不会使用这种方式）

By.xpath("html/body/div/form/input")
By.xpath("//input")
第三种方法：通过元素索引定位
By.xpath("//input[4]")
第四种方法：使用xpath属性定位（结合第2、第3中方法可以使用）
By.xpath("//input[@id='kw1']")
By.xpath("//input[@type='name' and @name='kw1']")
第五种方法：使用部分属性值匹配（最强大的方法）
By.xpath("//input[start-with(@id,'nice')
By.xpath("//input[ends-with(@id,'很漂亮')
By.xpath("//input[contains(@id,'那么美')]")
"""

from selenium import webdriver

driver = webdriver.Chrome()  # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()
driver.maximize_window()  # 最大化浏览器窗口
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("http://www.atcdeal.com/")  # 地址栏输入百度地址
"""
相对路径定位方式
"""
button = driver.find_element_by_xpath("//p[@class='f18 colOrange borbot lh45 h45 pl15']")
print(button.text)