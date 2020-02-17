# 导入requests包
import requests
'''发送请求'''
'''get请求============================================'''

# 1. 组装请求
url = "http://httpbin.org/get"  # 这里只有url，字符串格式
# 2. 发送请求，获取响应
res = requests.get(url) # res即返回的响应对象
# 3. 解析响应
print(res.text)  # 输出响应的文本

# r=requests.get('https://api.github.com/events') #get请求
# print(r.text)
# print(r.json())

'''带参数的GET请求'''''
url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"  # 参数可以写到url里
res = requests.get(url=url) # 第一个url指get方法的参数，第二个url指上一行我们定义的接口地址
print(res.text)
#或
url = "http://www.tuling123.com/openapi/api"
params = {"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"} # 字典格式，单独提出来，方便参数的添加修改等操作
res = requests.get(url=url, params=params)
print(res.text)


'''post请求==========================================================='''
# post请求  r = requests.post('http://httpbin.org/post', data = {'key':'value'})


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
print(r.json())


'''带安全认证的请求===============================================
需要登录的请求（Cookie/Session认证）'''

'''使用会话保持
#如果不使用session()而单独发一个post登录请求一个get请求是否可以呢？你可以自己试一下（requests.get()或post()每次都会建立一个新会话）
'''
s = requests.session() # 新建一个会话
s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs") # 使用同一个会话发送get请求，可以保持登录状态
print(res.text)

'''抓取cookies
# 使用Chrome浏览器访问https://demo.fastadmin.net/admin/index/login.html，登录
# 打开开发者工具刷新当前页面（https://demo.fastadmin.net/admin/index/login.html）
# Network面包查看当前请求，将cookie后面的值复制出来，组装成字典格式'''
url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
cookies = {"PHPSESSID":"9bf6b19ddb09938cf73d55a094b36726"}
res = requests.get(url=url, cookies=cookies) # 携带cookies发送请求
print(res.text)

'''两种方式的对比

使用session方式：每次都要发送两次请求，效率较低
使用携带cookies方式：需要手动抓包，提取组装，cookies中是session有一定有效期，过期之后要重新抓取和更换cookies
如果很多或所有请求都需要登录，可以发一次请求，保持该session为全局变量，其他接口都使用该session发送请求（同样要注意登录过期时间）

'''