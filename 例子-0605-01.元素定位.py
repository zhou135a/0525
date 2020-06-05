#coding=utf-8
#导入webdriver驱动
from selenium import webdriver
#定义驱动
br=webdriver.Chrome()
#打开网页
br.get("https://www.baidu.com")
#1.通过id定位元素进行操作
# br.find_element_by_id("kw").send_keys("新冠肺炎")
#2.通过name定位元素进行操作
# br.find_element_by_name("wd").send_keys("特朗普")
#3.通过class定位元素进行操作
# br.find_element_by_class_name("s_ipt").send_keys("弗洛伊德")
#4.通过tag定位
#html是通过tag来定义功能的，比如input是输入框等等...
#工作中使用比较少，很难通过tag区定位不同元素
# br.find_element_by_tag_name("input").send_keys("马丁路德金")
#5.通过link定位
#专门定位文本连接，比如百度新闻等
# br.find_element_by_link_text("新闻").click()
#5.通过partial_link定位
#超链接文本很长，全部输入浪费资源，这种方式就类似于模糊查询
# br.find_element_by_partial_link_text("闻").click()
#6.xpath
#理想状态下页面中都有id,name,class.超链接等等，但是实际情况并不是，属性相同刷新页面后值也会变量
# br.find_element_by_xpath("//*[@id='kw']").send_keys("美团")
#7.css
#相对xpath简洁，速度快
br.find_element_by_css_selector("#kw").send_keys("驾崩")


