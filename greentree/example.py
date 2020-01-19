import wechatsogou

# 可配置参数

# 直连
ws_api = wechatsogou.WechatSogouAPI()

# 验证码输入错误的重试次数，默认为1
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)

# 所有requests库的参数都能在这用
# 如 配置代理，代理列表中至少需包含1个 HTTPS 协议的代理, 并确保代理可用
# ws_api = wechatsogou.WechatSogouAPI(proxies={
#     "http": "127.0.0.1:8888",
#     "https": "127.0.0.1:8888",
# })

# 如 设置超时
# ws_api = wechatsogou.WechatSogouAPI(timeout=0.1)

# 获取特定公众号信息
# data = ws_api.get_gzh_info('记忆承载')

# data = ws_api.search_gzh('记忆承载')
# for i in data:
#     print(i)
user1 = {'open_id': 'oIWsFtwb874c16EZHuTSUjf108EU',
         'profile_url': '', 'headimage': 'https://img01.sogoucdn.com/app/a/100520090/oIWsFtwb874c16EZHuTSUjf108EU', 'wechat_name': '',
         'wechat_id': 'wodqbs', 'qrcode': '',
         'introduction': '本号抱着说相声的态度,专说实话.请带着去德云社的心态来看本号的文章.', 'authentication': '', 'post_perm': -1, 'view_perm': -1}

user2 = {'open_id': 'oIWsFtyB2xQWsNV0LzzgYGsb_sQQ', 'profile_url': 'http://mp.weixin.qq.com/profile?src=3&timestamp=1578996926&ver=1&signature=gBoOc5R9PO2hYPhD4CYjzLMgKFRiJr3YYzB32ePOODbJIuqtt0TdmjZ8IDVoPd8wQPoPrh9vpIOsk*cc2ZvlVA==',
         'headimage': 'https://img01.sogoucdn.com/app/a/100520090/oIWsFtyB2xQWsNV0LzzgYGsb_sQQ', 'wechat_name': '3',
         'wechat_id': 'wodqbs3', 'qrcode': '', 'introduction': '像说相声一样说人生.', 'authentication': '\n', 'post_perm': -1,
         'view_perm': -1}

# 搜索微信文章
# ws_api.search_article('南京航空航天大学')

# 解析最近文章页
# data = ws_api.get_gzh_article_by_history(keyword=user1.get('wechat_id'))
# print(data)
