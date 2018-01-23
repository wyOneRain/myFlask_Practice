from Models import Users

def validate(username,password1,passwoed2=None):
    User=Users()
    user=User.select_user(username)
    try:
        if passwoed2:
            if user==None:
                if len(username)<4 or len(username)>12:
                    return '用户名长度应在4-12个字符之间'
                elif password1!=passwoed2:
                    return '两次密码不一致'
                elif len(password1)<6:
                    return '密码长度至少6个字符'
                else:
                    return '注册成功'
            else:
                return '用户名已经存在'
        else:
            if user==None:
                return '用户名不存在'
            else:
                if user['password'] == password1:
                    return '登录成功'
                else:
                    return '密码错误'
    finally:
        User.close()
# print(validate('OneRain','312','312'))