# ================
# 2022/9/9 18:20
# test_login.PY
# author:Meffa
# ================
class Test_Login():
    def test_login_success(self):
        print("登录成功")
        assert 1 == 1
    def test_login_fail(self):
        print("登录失败")
        pass
if __name__ == '__main__':
    Test_Login().test_login_fail()