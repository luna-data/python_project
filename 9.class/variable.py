# 전역 변수
global_var = "This is a global variable"

class MyClass:
# 인스턴스 변수
    def __init__(self):
        self.instance_var = "This is an instance variable"
    def my_function(self):
    # 지역 변수
        local_var = "This is a local variable"
        print(local_var)
        print(self.instance_var)
        print(global_var)
# 객체 생성
my_obj = MyClass()
# 메서드 호출
my_obj.my_function()