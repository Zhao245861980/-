"""各个第三方平台的接入配置"""

# 互亿无限短信配置
HY_SMS_URL = 'https://106.ihuyi.com/webservice/sms.php?method=SubmitBatch'
HY_SMS_PARAMS = {
    'account': 'C28888145',
    'password': 'fea6be16ef4306f025d227d7a37e415e',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}

# 七牛云配置
QN_ACCESS_KEY = 'JkXPH0DRZmj7rSFZSizjFMYTFLUMQZyYnCVEmoOx'
QN_SECRET_KEY = 'NgwKyHhU1CH0VQRSfG7i0BYVyQOsQuWtPAY8UVmX'
QN_BUCKET_NAME = 'swiper1111'
QN_BASE_URL = 'http://sowqniy2h.hd-bkt.clouddn.com'